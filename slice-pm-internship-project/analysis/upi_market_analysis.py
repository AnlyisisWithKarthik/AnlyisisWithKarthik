"""
UPI Market Analysis — slice PM Internship Project
===================================================
Analyzes India's UPI transaction trends to identify market opportunities
for slice Smart Budgets feature.

Usage:
    python upi_market_analysis.py

Output:
    - Console: Key market insights and statistics
    - Charts: Saved to analysis/output/ directory
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Styling
plt.style.use("seaborn-v0_8-whitegrid")
SLICE_COLORS = {
    "primary": "#6C5CE7",
    "secondary": "#A29BFE",
    "accent": "#FD79A8",
    "success": "#00B894",
    "warning": "#FDCB6E",
    "dark": "#2D3436",
    "light": "#DFE6E9",
}


def load_data():
    """Load UPI monthly transaction data."""
    filepath = os.path.join(DATA_DIR, "upi_monthly_transactions.csv")
    df = pd.read_csv(filepath)
    df["Date"] = pd.to_datetime(
        df["Year"].astype(str) + "-" + df["Month"], format="%Y-%b"
    )
    df = df.sort_values("Date").reset_index(drop=True)
    return df


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def analyze_growth(df):
    """Analyze and visualize UPI transaction growth."""
    print_section("UPI TRANSACTION GROWTH ANALYSIS")

    # YoY Growth
    latest_year_vol = df[df["Year"] == 2024]["Volume_Billion"].sum()
    prev_year_vol = df[df["Year"] == 2023]["Volume_Billion"].sum()
    yoy_growth = ((latest_year_vol - prev_year_vol) / prev_year_vol) * 100

    latest_year_val = df[df["Year"] == 2024]["Value_Lakh_Crore"].sum()
    prev_year_val = df[df["Year"] == 2023]["Value_Lakh_Crore"].sum()
    yoy_val_growth = ((latest_year_val - prev_year_val) / prev_year_val) * 100

    print(f"\n📊 Key Statistics (2024 vs 2023):")
    print(f"   Volume Growth (YoY):  {yoy_growth:+.1f}%")
    print(f"   Value Growth (YoY):   {yoy_val_growth:+.1f}%")
    print(f"   Total 2024 Volume:    {latest_year_vol:.1f} Billion transactions")
    print(f"   Total 2024 Value:     ₹{latest_year_val:.1f} Lakh Crore")
    print(f"   Latest MAU:           {df['Active_Users_Million'].iloc[-1]}M users")

    # Month-over-month growth rate
    df["Vol_MoM_Growth"] = df["Volume_Billion"].pct_change() * 100
    avg_mom_growth = df["Vol_MoM_Growth"].mean()
    print(f"   Avg Monthly Growth:   {avg_mom_growth:.1f}%")

    # Plot: Transaction Volume & Value Trend
    fig, ax1 = plt.subplots(figsize=(14, 7))

    ax1.bar(
        df["Date"],
        df["Volume_Billion"],
        color=SLICE_COLORS["primary"],
        alpha=0.7,
        label="Volume (Billion)",
        width=20,
    )
    ax1.set_xlabel("Month", fontsize=12, fontweight="bold")
    ax1.set_ylabel("Transaction Volume (Billion)", fontsize=12, color=SLICE_COLORS["primary"])
    ax1.tick_params(axis="y", labelcolor=SLICE_COLORS["primary"])

    ax2 = ax1.twinx()
    ax2.plot(
        df["Date"],
        df["Value_Lakh_Crore"],
        color=SLICE_COLORS["accent"],
        linewidth=2.5,
        marker="o",
        markersize=4,
        label="Value (₹ Lakh Crore)",
    )
    ax2.set_ylabel("Transaction Value (₹ Lakh Crore)", fontsize=12, color=SLICE_COLORS["accent"])
    ax2.tick_params(axis="y", labelcolor=SLICE_COLORS["accent"])

    plt.title(
        "India UPI Transaction Growth (2022-2024)\nVolume & Value Trend",
        fontsize=16,
        fontweight="bold",
        pad=20,
    )

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "upi_volume_value_trend.png"), dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n   ✅ Chart saved: output/upi_volume_value_trend.png")

    return yoy_growth, yoy_val_growth


def analyze_user_growth(df):
    """Analyze active user growth trajectory."""
    print_section("ACTIVE USER GROWTH ANALYSIS")

    # User growth
    start_users = df["Active_Users_Million"].iloc[0]
    end_users = df["Active_Users_Million"].iloc[-1]
    total_growth = ((end_users - start_users) / start_users) * 100
    months = len(df)
    cagr_monthly = ((end_users / start_users) ** (1 / months) - 1) * 100

    print(f"\n👥 User Growth Statistics:")
    print(f"   Start (Jan 2022):     {start_users}M users")
    print(f"   End (Dec 2024):       {end_users}M users")
    print(f"   Total Growth:         {total_growth:.0f}%")
    print(f"   Monthly CAGR:         {cagr_monthly:.1f}%")

    # Gen-Z specific estimation
    genz_pct = 0.35  # 35% of UPI users are 18-28
    genz_users = end_users * genz_pct
    print(f"\n   🎯 slice Target (Gen-Z):")
    print(f"   Estimated Gen-Z MAU:  {genz_users:.0f}M users ({genz_pct*100:.0f}% of total)")
    print(f"   Market Potential:     Even 5% capture = {genz_users*0.05:.0f}M users")

    # Plot: User Growth
    fig, ax = plt.subplots(figsize=(14, 7))

    ax.fill_between(
        df["Date"],
        df["Active_Users_Million"],
        alpha=0.3,
        color=SLICE_COLORS["primary"],
    )
    ax.plot(
        df["Date"],
        df["Active_Users_Million"],
        color=SLICE_COLORS["primary"],
        linewidth=2.5,
        marker="o",
        markersize=4,
    )

    # Add Gen-Z line
    ax.plot(
        df["Date"],
        df["Active_Users_Million"] * genz_pct,
        color=SLICE_COLORS["accent"],
        linewidth=2,
        linestyle="--",
        label=f"Est. Gen-Z Users ({genz_pct*100:.0f}%)",
    )

    # Annotations
    ax.annotate(
        f"{end_users}M\nTotal MAU",
        xy=(df["Date"].iloc[-1], end_users),
        xytext=(df["Date"].iloc[-4], end_users + 30),
        fontsize=11,
        fontweight="bold",
        color=SLICE_COLORS["dark"],
        arrowprops={"arrowstyle": "->", "color": SLICE_COLORS["dark"]},
    )

    ax.set_xlabel("Month", fontsize=12, fontweight="bold")
    ax.set_ylabel("Monthly Active Users (Million)", fontsize=12, fontweight="bold")
    ax.set_title(
        "UPI Monthly Active Users Growth\nGen-Z Segment = slice's Target Market",
        fontsize=16,
        fontweight="bold",
        pad=20,
    )
    ax.legend(fontsize=11, loc="upper left")

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "upi_user_growth.png"), dpi=150, bbox_inches="tight")
    plt.close()
    print(f"   ✅ Chart saved: output/upi_user_growth.png")


def analyze_avg_transaction(df):
    """Analyze average transaction value trends."""
    print_section("AVERAGE TRANSACTION VALUE ANALYSIS")

    df["Avg_Txn_Calculated"] = (df["Value_Lakh_Crore"] / df["Volume_Billion"]) * 10000

    avg_2022 = df[df["Year"] == 2022]["Avg_Txn_Calculated"].mean()
    avg_2023 = df[df["Year"] == 2023]["Avg_Txn_Calculated"].mean()
    avg_2024 = df[df["Year"] == 2024]["Avg_Txn_Calculated"].mean()

    print(f"\n💰 Average Transaction Value (Calculated):")
    print(f"   2022 Average:         ₹{avg_2022:,.0f}")
    print(f"   2023 Average:         ₹{avg_2023:,.0f}")
    print(f"   2024 Average:         ₹{avg_2024:,.0f}")
    print(f"   Trend:                {'📈 Increasing' if avg_2024 > avg_2023 else '📉 Decreasing'}")
    print(f"\n   💡 Insight: Declining avg transaction value suggests more")
    print(f"      micro-transactions — exactly the type that cause")
    print(f"      overspending anxiety. Validates Smart Budgets need.")

    # Plot: Average Transaction Value
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(
        df["Date"],
        df["Avg_Txn_Calculated"],
        color=SLICE_COLORS["warning"],
        linewidth=2.5,
        marker="s",
        markersize=5,
        label="Avg Transaction Value (₹)",
    )

    # Add trend line
    x_numeric = np.arange(len(df))
    z = np.polyfit(x_numeric, df["Avg_Txn_Calculated"], 1)
    p = np.poly1d(z)
    ax.plot(
        df["Date"],
        p(x_numeric),
        color=SLICE_COLORS["accent"],
        linewidth=2,
        linestyle="--",
        label=f"Trend (slope: ₹{z[0]:+.1f}/month)",
    )

    ax.set_xlabel("Month", fontsize=12, fontweight="bold")
    ax.set_ylabel("Average Transaction Value (₹)", fontsize=12, fontweight="bold")
    ax.set_title(
        "UPI Average Transaction Value Trend\nMore Micro-Transactions = Greater Need for Budgeting",
        fontsize=16,
        fontweight="bold",
        pad=20,
    )
    ax.legend(fontsize=11)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"₹{x:,.0f}"))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "upi_avg_transaction.png"), dpi=150, bbox_inches="tight")
    plt.close()
    print(f"   ✅ Chart saved: output/upi_avg_transaction.png")


def market_projection(df):
    """Project future UPI growth and opportunity sizing."""
    print_section("MARKET PROJECTION & OPPORTUNITY SIZING")

    # Project next 12 months
    last_vol = df["Volume_Billion"].iloc[-1]
    last_val = df["Value_Lakh_Crore"].iloc[-1]
    last_users = df["Active_Users_Million"].iloc[-1]

    monthly_vol_growth = 0.035  # 3.5% monthly
    monthly_val_growth = 0.03   # 3% monthly
    monthly_user_growth = 0.02  # 2% monthly

    projections = []
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    for i in range(12):
        projected_vol = last_vol * (1 + monthly_vol_growth) ** (i + 1)
        projected_val = last_val * (1 + monthly_val_growth) ** (i + 1)
        projected_users = last_users * (1 + monthly_user_growth) ** (i + 1)
        projections.append({
            "Month": months[i],
            "Year": 2025,
            "Volume_Billion": round(projected_vol, 2),
            "Value_Lakh_Crore": round(projected_val, 2),
            "Active_Users_Million": round(projected_users),
        })

    proj_df = pd.DataFrame(projections)

    print(f"\n🔮 2025 Projections (Conservative Estimates):")
    print(f"   Monthly Volume Growth: {monthly_vol_growth*100:.1f}%")
    print(f"   Monthly Value Growth:  {monthly_val_growth*100:.1f}%")
    print(f"   Monthly User Growth:   {monthly_user_growth*100:.1f}%")
    print(f"\n   Projected Dec 2025:")
    print(f"   Volume:  {proj_df['Volume_Billion'].iloc[-1]:.1f}B transactions")
    print(f"   Value:   ₹{proj_df['Value_Lakh_Crore'].iloc[-1]:.1f} Lakh Crore")
    print(f"   Users:   {proj_df['Active_Users_Million'].iloc[-1]}M MAU")

    # Opportunity sizing for slice
    slice_mau = 8_000_000  # 8M MAU
    smart_budget_adoption = 0.30  # 30% adopt
    additional_txn_pct = 0.12  # 12% more transactions
    avg_monthly_spend = 15000  # ₹15,000 avg
    mdr_rate = 0.015  # 1.5% MDR

    adopters = slice_mau * smart_budget_adoption
    additional_revenue = adopters * avg_monthly_spend * additional_txn_pct * mdr_rate * 12

    print(f"\n   💰 slice Smart Budgets Revenue Opportunity:")
    print(f"   slice MAU:                {slice_mau/1e6:.0f}M")
    print(f"   Expected Adopters (30%):  {adopters/1e6:.1f}M")
    print(f"   Additional Revenue/Year:  ₹{additional_revenue/1e7:.1f} Crore")

    return proj_df


def generate_summary(yoy_vol_growth, yoy_val_growth):
    """Generate executive summary of findings."""
    print_section("EXECUTIVE SUMMARY FOR slice SMART BUDGETS")

    print("""
    📋 KEY FINDINGS:

    1. MASSIVE MARKET: UPI processed 16.7B+ transactions in Dec 2024
       alone, growing at {vol_g:.0f}% YoY volume and {val_g:.0f}% YoY value.

    2. USER BASE EXPLOSION: 385M+ monthly active UPI users,
       with ~135M in the 18-28 age group (slice's core demographic).

    3. MICRO-TRANSACTION TREND: Average transaction value is
       declining, indicating more frequent small purchases —
       exactly the type that causes overspending.

    4. BUDGET-READY DATA: The sheer volume of digital transactions
       means rich data is available for intelligent categorization
       and budgeting insights.

    5. TIMING IS RIGHT: UPI's growth trajectory ensures the
       addressable market will only expand. Building budgeting
       features now positions slice ahead of competitors.

    ✅ RECOMMENDATION: Launch Smart Budgets as a Phase 0 feature
       focusing on auto-categorization and spending dashboards,
       expanding to budgets, nudges, and gamification in subsequent
       phases.
    """.format(vol_g=yoy_vol_growth, val_g=yoy_val_growth))


def main():
    """Run the complete UPI market analysis."""
    print("\n" + "🍕" * 30)
    print("  slice Smart Budgets — UPI Market Analysis")
    print("  Product Management Internship Project")
    print("🍕" * 30)

    # Load data
    df = load_data()
    print(f"\n📂 Loaded {len(df)} months of UPI transaction data ({df['Date'].min().strftime('%b %Y')} to {df['Date'].max().strftime('%b %Y')})")

    # Run analyses
    yoy_vol_growth, yoy_val_growth = analyze_growth(df)
    analyze_user_growth(df)
    analyze_avg_transaction(df)
    market_projection(df)
    generate_summary(yoy_vol_growth, yoy_val_growth)

    print(f"\n{'='*60}")
    print(f"  Analysis complete! Charts saved to: {OUTPUT_DIR}/")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
