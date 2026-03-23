# Hi — I'm Karthik Sharma 👋  
**Data Analyst | SQL • Python (Pandas) • Advanced Excel • Power BI • Tableau**  

[![GitHub followers](https://img.shields.io/github/followers/your-github-username?label=Follow&style=social)]
[![Top Language](https://img.shields.io/github/languages/top/your-github-username/your-repo?label=Top%20Language)]
[![Repo size](https://img.shields.io/github/repo-size/your-github-username/your-repo)]

---

## 🔍 About Me
I'm a data-focused problem solver with strong hands-on experience in **SQL, Python (Pandas), Advanced Excel, Power BI, and Tableau**. I transform messy data into clear insights and actionable dashboards that drive decisions. I enjoy end-to-end analytics — from data modeling and ETL to visualization and storytelling.

---

## ⚙️ Core Skills
- **Databases & SQL:** complex joins, window functions, query optimization, schema design, data cleaning  
- **Python (Pandas):** ETL, data wrangling, feature engineering, reproducible analysis  
- **Advanced Excel:** pivot tables, Power Query, array formulas, VBA-ready automation patterns  
- **BI & Visualization:** interactive dashboards in **Power BI** and **Tableau**; KPI design, storytelling  
- **Tools:** Git, Jupyter, VS Code, CSV/Excel, REST APIs, basic Linux commands

---

## 🚀 What I Build
- Production-ready **SQL pipelines & optimized queries** for analytics  
- End-to-end **data analysis projects** using Pandas + SQL  
- Interactive **dashboards** (Power BI / Tableau) for business stakeholders  
- Automation templates and Excel models for recurring reports

---

## 📁 Projects (examples to pin)
- **Sales Performance Dashboard (Power BI)** — drilldowns, dynamic measures, performance forecasting  
- **Customer Cohort Analysis (SQL + Pandas)** — retention cohorts, LTV approximation, churn signals  
- **Inventory Optimization (SQL)** — reorder triggers, ABC analysis, reporting automation  
- **ETL Scripts (Python)** — ingestion, cleaning, validation, ready for BI consumption

*(Pin the above repos to your profile for maximum recruiter visibility.)*

---

## 🎯 Highlights
- Strong practical focus — projects built for business impact, not just notebooks  
- Clean, well-documented code and reproducible notebooks  
- Prioritize explainable visuals and stakeholder-friendly dashboards

---

## 📫 Reach Me
- GitHub: `https://github.com/your-github-username`  
- Email: `your.email@example.com`  
- LinkedIn: `https://www.linkedin.com/in/your-profile`

---

## ✨ Want to collaborate?
Check my pinned projects — open to collaborations, internships, and data challenges.  
**If you like what you see, star a repo or drop me a message.**

---
*Keywords: SQL, Python, Pandas, Power BI, Tableau, Advanced Excel, Data Analysis, Data Visualization, ETL, BI, Dashboard*

## 🤖 NASDAQ India Investor Cost Bot

This repository now includes a CLI bot at `./nasdaq_tax_bot.py` that helps estimate:
- convenience fees
- compliance fees
- tax impact (including LRS TCS and investment tax estimates)

It also supports live internet-backed data:
- USD/INR conversion rate
- live US ticker quote
- listing US market companies (SEC dataset)

### Run examples

```bash
# From repository root

# Live USD/INR
python nasdaq_tax_bot.py fx

# Live quote
python nasdaq_tax_bot.py quote --ticker AAPL

# List companies
python nasdaq_tax_bot.py companies --limit 20

# Calculate cost impact
python nasdaq_tax_bot.py calculate --amount-inr 100000 --platform vested --ticker AAPL

# If live FX API is unavailable in your environment
python nasdaq_tax_bot.py calculate --amount-inr 100000 --platform vested --usd-inr-rate 83.0
```
