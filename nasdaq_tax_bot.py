#!/usr/bin/env python3
import argparse
import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from urllib.error import URLError
from urllib.request import urlopen


PLATFORM_CONFIG: Dict[str, Dict[str, float]] = {
    "vested": {
        "convenience_fee_pct": 0.004,
        "compliance_fee_inr": 499.0,
        "brokerage_pct": 0.001,
        "platform_fee_pct": 0.0005,
        "min_brokerage_usd": 1.0,
    },
    "indmoney": {
        "convenience_fee_pct": 0.0035,
        "compliance_fee_inr": 399.0,
        "brokerage_pct": 0.0008,
        "platform_fee_pct": 0.0004,
        "min_brokerage_usd": 1.0,
    },
    "stockal": {
        "convenience_fee_pct": 0.005,
        "compliance_fee_inr": 599.0,
        "brokerage_pct": 0.0012,
        "platform_fee_pct": 0.0006,
        "min_brokerage_usd": 2.0,
    },
}


@dataclass
class CalculationInput:
    amount_inr: float
    platform: str
    expected_return_pct: float = 0.10
    dividend_yield_pct: float = 0.01
    holding_period_years: float = 1.0
    indian_income_tax_rate: float = 0.30
    remittance_so_far_inr: float = 0.0
    tcs_rate: float = 0.20
    lrs_tcs_threshold_inr: float = 700000.0


def _fetch_json(url: str, timeout: int = 10) -> Dict[str, Any]:
    with urlopen(url, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def get_usd_inr_rate() -> float:
    try:
        data = _fetch_json("https://open.er-api.com/v6/latest/USD")
    except URLError as err:
        raise ValueError(
            "Unable to fetch live USD/INR rate. Check internet connectivity or pass --usd-inr-rate."
        ) from err
    rates = data.get("rates", {})
    rate = rates.get("INR")
    if not rate:
        raise ValueError("Could not fetch USD/INR rate")
    return float(rate)


def get_live_quote_usd(symbol: str) -> Dict[str, Any]:
    safe_symbol = symbol.strip().upper()
    if not safe_symbol:
        raise ValueError("Ticker symbol is required")
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={safe_symbol}"
    data = _fetch_json(url)
    result = data.get("quoteResponse", {}).get("result", [])
    if not result:
        raise ValueError(f"No market quote found for {safe_symbol}")
    quote = result[0]
    return {
        "symbol": quote.get("symbol", safe_symbol),
        "name": quote.get("longName") or quote.get("shortName") or safe_symbol,
        "currency": quote.get("currency", "USD"),
        "price": float(quote.get("regularMarketPrice", 0.0)),
        "time": quote.get("regularMarketTime"),
    }


def list_us_market_companies(limit: int = 50) -> List[Dict[str, str]]:
    data = _fetch_json("https://www.sec.gov/files/company_tickers.json")
    companies: List[Dict[str, str]] = []
    for _, item in data.items():
        ticker = item.get("ticker", "")
        title = item.get("title", "")
        if ticker and title:
            companies.append({"ticker": str(ticker), "name": str(title)})
    companies.sort(key=lambda x: x["ticker"])
    return companies[: max(limit, 0)]


def _calculate_tcs(remittance_so_far_inr: float, amount_inr: float, threshold_inr: float, tcs_rate: float) -> float:
    previous_excess = max(remittance_so_far_inr - threshold_inr, 0.0)
    current_excess = max(remittance_so_far_inr + amount_inr - threshold_inr, 0.0)
    tcs_base = max(current_excess - previous_excess, 0.0)
    return tcs_base * tcs_rate


def calculate_investment_breakdown(calc_input: CalculationInput, usd_inr_rate: Optional[float] = None) -> Dict[str, Any]:
    platform = calc_input.platform.lower()
    if platform not in PLATFORM_CONFIG:
        raise ValueError(f"Unsupported platform '{calc_input.platform}'. Supported: {', '.join(PLATFORM_CONFIG)}")
    if calc_input.amount_inr <= 0:
        raise ValueError("amount_inr must be > 0")

    config = PLATFORM_CONFIG[platform]
    fx = usd_inr_rate if usd_inr_rate is not None else get_usd_inr_rate()

    convenience_fee_inr = calc_input.amount_inr * config["convenience_fee_pct"]
    compliance_fee_inr = config["compliance_fee_inr"]
    tcs_inr = _calculate_tcs(
        remittance_so_far_inr=calc_input.remittance_so_far_inr,
        amount_inr=calc_input.amount_inr,
        threshold_inr=calc_input.lrs_tcs_threshold_inr,
        tcs_rate=calc_input.tcs_rate,
    )

    investable_inr = max(calc_input.amount_inr - convenience_fee_inr - compliance_fee_inr, 0.0)
    gross_usd = investable_inr / fx
    brokerage_usd = max(gross_usd * config["brokerage_pct"], config["min_brokerage_usd"])
    platform_fee_usd = gross_usd * config["platform_fee_pct"]
    net_invested_usd = max(gross_usd - brokerage_usd - platform_fee_usd, 0.0)

    expected_gain_usd = net_invested_usd * calc_input.expected_return_pct
    capital_gains_tax_rate = 0.30 if calc_input.holding_period_years < 2 else 0.125
    indian_capital_gains_tax_inr = max(expected_gain_usd, 0.0) * capital_gains_tax_rate * fx

    gross_dividend_usd = net_invested_usd * calc_input.dividend_yield_pct
    us_dividend_tax_usd = gross_dividend_usd * 0.25
    india_dividend_tax_usd = max(gross_dividend_usd * calc_input.indian_income_tax_rate - us_dividend_tax_usd, 0.0)
    total_dividend_tax_inr = (us_dividend_tax_usd + india_dividend_tax_usd) * fx

    total_estimated_cost_inr = (
        convenience_fee_inr
        + compliance_fee_inr
        + tcs_inr
        + indian_capital_gains_tax_inr
        + total_dividend_tax_inr
    )

    return {
        "platform": platform,
        "amount_inr": round(calc_input.amount_inr, 2),
        "usd_inr_rate": round(fx, 4),
        "fees": {
            "convenience_fee_inr": round(convenience_fee_inr, 2),
            "compliance_fee_inr": round(compliance_fee_inr, 2),
            "brokerage_usd": round(brokerage_usd, 4),
            "platform_fee_usd": round(platform_fee_usd, 4),
        },
        "taxes": {
            "lrs_tcs_inr": round(tcs_inr, 2),
            "indian_capital_gains_tax_inr": round(indian_capital_gains_tax_inr, 2),
            "dividend_taxes_inr": round(total_dividend_tax_inr, 2),
        },
        "investable": {
            "investable_inr_after_entry_fees": round(investable_inr, 2),
            "net_invested_usd": round(net_invested_usd, 4),
            "expected_gain_usd": round(expected_gain_usd, 4),
        },
        "estimated_total_cost_inr": round(total_estimated_cost_inr, 2),
    }


def _print_json(payload: Any) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="NASDAQ India Investor Bot: taxes, compliance and convenience fee calculator with live rates."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    fx_parser = subparsers.add_parser("fx", help="Get live USD/INR rate")
    fx_parser.set_defaults(command="fx")

    quote_parser = subparsers.add_parser("quote", help="Get live US market quote for a ticker")
    quote_parser.add_argument("--ticker", required=True)
    quote_parser.set_defaults(command="quote")

    companies_parser = subparsers.add_parser("companies", help="List US market companies")
    companies_parser.add_argument("--limit", type=int, default=50)
    companies_parser.set_defaults(command="companies")

    calc_parser = subparsers.add_parser("calculate", help="Calculate taxes and fee impact for NASDAQ investing")
    calc_parser.add_argument("--amount-inr", type=float, required=True)
    calc_parser.add_argument("--platform", choices=sorted(PLATFORM_CONFIG.keys()), required=True)
    calc_parser.add_argument("--expected-return-pct", type=float, default=0.10)
    calc_parser.add_argument("--dividend-yield-pct", type=float, default=0.01)
    calc_parser.add_argument("--holding-period-years", type=float, default=1.0)
    calc_parser.add_argument("--indian-income-tax-rate", type=float, default=0.30)
    calc_parser.add_argument("--remittance-so-far-inr", type=float, default=0.0)
    calc_parser.add_argument("--usd-inr-rate", type=float, default=None, help="Optional USD/INR override when live API is unavailable")
    calc_parser.add_argument("--ticker", default=None, help="Optional ticker to include live price context")
    calc_parser.set_defaults(command="calculate")

    args = parser.parse_args()

    try:
        if args.command == "fx":
            _print_json({"usd_inr_rate": get_usd_inr_rate()})
        elif args.command == "quote":
            _print_json(get_live_quote_usd(args.ticker))
        elif args.command == "companies":
            _print_json({"count": args.limit, "companies": list_us_market_companies(limit=args.limit)})
        elif args.command == "calculate":
            payload = calculate_investment_breakdown(
                CalculationInput(
                    amount_inr=args.amount_inr,
                    platform=args.platform,
                    expected_return_pct=args.expected_return_pct,
                    dividend_yield_pct=args.dividend_yield_pct,
                    holding_period_years=args.holding_period_years,
                    indian_income_tax_rate=args.indian_income_tax_rate,
                    remittance_so_far_inr=args.remittance_so_far_inr,
                ),
                usd_inr_rate=args.usd_inr_rate,
            )
            if args.ticker:
                payload["live_quote"] = get_live_quote_usd(args.ticker)
            _print_json(payload)
        return 0
    except (ValueError, URLError) as err:
        _print_json({"error": str(err)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
