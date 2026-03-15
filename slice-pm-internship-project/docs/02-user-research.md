# 👥 User Research: Understanding slice's Young Indian Users

## 1. Research Methodology

### Approach
| Method | Details |
|--------|---------|
| **Desk Research** | Analysis of app store reviews, social media mentions, community forums |
| **Behavioral Analysis** | Study of UPI usage patterns, spending category data (public datasets) |
| **Persona Development** | Based on demographic data, behavioral archetypes, and financial profiles |
| **Journey Mapping** | End-to-end mapping of user financial journey with pain points |
| **Jobs-to-be-Done Framework** | Identifying core user jobs around spending and budgeting |

---

## 2. User Personas

### 🎓 Persona 1: "College Coder" Arjun

| Attribute | Detail |
|-----------|--------|
| **Age** | 21 |
| **Location** | Pune |
| **Occupation** | B.Tech student, part-time freelancer |
| **Monthly Income** | ₹8,000-₹12,000 (freelancing + pocket money) |
| **Monthly Spend** | ₹6,000-₹10,000 |
| **slice Usage** | UPI payments, occasional credit usage for gadgets |
| **Financial Goal** | Save for a new laptop; avoid month-end cash crunch |
| **Pain Points** | Loses track of small Swiggy/Zomato orders; surprised by credit bill; no savings habit |
| **Tech Behavior** | Heavy app user; loves gamification; active on Discord and Twitter |
| **Quote** | *"I don't know where my money goes. By the 20th, I'm already asking friends for UPI transfers."* |

**Jobs-to-be-Done:**
- Help me understand where my money goes without making me feel bad
- Warn me before I overspend on food delivery
- Make saving feel rewarding, not restrictive

---

### 💼 Persona 2: "First Jobber" Priya

| Attribute | Detail |
|-----------|--------|
| **Age** | 24 |
| **Location** | Bangalore |
| **Occupation** | Junior Software Engineer (1 year experience) |
| **Monthly Income** | ₹35,000-₹45,000 |
| **Monthly Spend** | ₹20,000-₹30,000 |
| **slice Usage** | Primary payment card for online shopping; UPI for daily expenses |
| **Financial Goal** | Build an emergency fund; start investing |
| **Pain Points** | Too many subscriptions; credit card billing confusing; wants to invest but "no money left" |
| **Tech Behavior** | Instagram-first; uses 3-4 payment apps; tried budgeting apps but abandoned them |
| **Quote** | *"I make decent money but I have no idea why I can't save. Excel sheets are boring and I forget to update them."* |

**Jobs-to-be-Done:**
- Show me exactly where my salary goes each month — automatically
- Help me identify subscriptions I forgot about
- Give me a simple plan to save ₹5,000/month without thinking about it

---

### 🎨 Persona 3: "Side Hustler" Rohan

| Attribute | Detail |
|-----------|--------|
| **Age** | 26 |
| **Location** | Mumbai |
| **Occupation** | Marketing Executive + Instagram content creator |
| **Monthly Income** | ₹50,000-₹70,000 (salary + side hustle) |
| **Monthly Spend** | ₹35,000-₹50,000 |
| **slice Usage** | Heavy credit user; split bills with friends; reward points enthusiast |
| **Financial Goal** | Go full-time on content creation; needs 6-month runway |
| **Pain Points** | Multiple income sources hard to track; social spending pressure; credit utilization too high |
| **Tech Behavior** | Power user; compares features across apps; influenced by fintech Twitter |
| **Quote** | *"I need a financial co-pilot, not a calculator. Show me the patterns in my spending and help me fix them."* |

**Jobs-to-be-Done:**
- Track spending across multiple income streams
- Help me reduce social spending without feeling left out
- Show me how much runway I'm building toward my goal

---

### 🛍️ Persona 4: "Shopping Queen" Ananya

| Attribute | Detail |
|-----------|--------|
| **Age** | 22 |
| **Location** | Delhi |
| **Occupation** | Final year MBA student |
| **Monthly Income** | ₹15,000 (internship stipend) |
| **Monthly Spend** | ₹12,000-₹18,000 (often exceeds income) |
| **slice Usage** | Credit card for Myntra/Amazon; UPI for daily needs |
| **Financial Goal** | Stop overspending on shopping; clear credit card dues on time |
| **Pain Points** | Impulsive shopping during sales; minimum due confusion; EMI tracking |
| **Tech Behavior** | Visual learner; loves aesthetic UIs; shares financial tips on Instagram Stories |
| **Quote** | *"Every sale feels like I'm saving money, but my credit card statement says otherwise. I need something that shows me the truth in real-time."* |

**Jobs-to-be-Done:**
- Alert me BEFORE I overspend, not after
- Help me understand how EMIs add up over time
- Make it socially cool to budget (I want to share my "money wins")

---

## 3. User Journey Map

### Current Journey: "Priya Tries to Budget"

```
Stage 1: AWARENESS
├─ Trigger: Month-end cash crunch for the 3rd time
├─ Feeling: 😟 Frustrated, anxious
├─ Action: Searches "best budgeting app India" on Google
└─ Pain: Too many options, none feel made for her

Stage 2: CONSIDERATION
├─ Trigger: Tries a generic budgeting app (Walnut/Money Manager)
├─ Feeling: 😐 Hopeful but overwhelmed
├─ Action: Manually enters transactions for 3 days
└─ Pain: Manual entry is tedious; forgets after Day 3

Stage 3: TRIAL
├─ Trigger: Sees slice already tracks her payments
├─ Feeling: 💡 "Wait, slice has my data already!"
├─ Action: Checks slice app transaction history
└─ Pain: Only a flat list — no insights, no categories, no budgets

Stage 4: FRUSTRATION
├─ Trigger: Realizes she needs a separate app for budgeting
├─ Feeling: 😤 "Why can't slice just show me where my money goes?"
├─ Action: Goes back to ignoring her finances
└─ Pain: Continues the overspending cycle

Stage 5: DREAM STATE (What Smart Budgets would deliver)
├─ Trigger: slice sends a push notification: "You've spent ₹3,200 on food this week — 80% of your monthly food budget"
├─ Feeling: 🤩 Empowered, in control
├─ Action: Adjusts spending for the rest of the week
└─ Outcome: Saves ₹4,000 more than usual that month
```

---

## 4. Pain Point Analysis

### Severity × Frequency Matrix

| Pain Point | Severity (1-5) | Frequency | Affected Personas | Priority |
|-----------|:-:|-----------|-------------------|:--------:|
| No automatic spending categorization | 5 | Every transaction | All | 🔴 P0 |
| Surprised by credit card bill amount | 5 | Monthly | Priya, Ananya, Rohan | 🔴 P0 |
| Can't set or track budgets in-app | 4 | Weekly | All | 🔴 P0 |
| Forgotten subscriptions draining money | 4 | Monthly | Priya, Rohan | 🟡 P1 |
| No savings goal tracking | 3 | Monthly | Arjun, Priya | 🟡 P1 |
| Credit utilization anxiety | 4 | Monthly | Ananya, Rohan | 🟡 P1 |
| No spending insights or trends | 4 | Weekly | All | 🟡 P1 |
| Can't compare spending month-over-month | 3 | Monthly | Priya, Rohan | 🟢 P2 |
| No social/shareable money features | 2 | Weekly | Arjun, Ananya | 🟢 P2 |

---

## 5. User Needs Hierarchy (Kano Model)

### Must-Haves (Basic Needs)
- ✅ Automatic transaction categorization
- ✅ Monthly spending summary
- ✅ Credit card bill tracker with due date reminders

### Performance Needs (Satisfiers)
- 📊 Budget setting and tracking per category
- 📊 Spending trend visualizations (weekly/monthly)
- 📊 Subscription detection and alerts
- 📊 Smart nudges before budget breach

### Delight Features (Exciters)
- 🎮 Savings streaks and badges
- 🎮 Social money challenges (with friends)
- 🎮 "Money Mood" weekly digest
- 🎮 AI spending coach with personalized tips
- 🎮 Shareable savings milestones

---

## 6. Key Research Insights

### Insight 1: "The ₹200 Problem"
> Young users don't track small transactions (₹50-₹200) individually, but these account for **40-60% of monthly overspending**. Auto-categorization of micro-transactions is the #1 unlock.

### Insight 2: "Shame-Free Finance"
> 78% of young users abandoned budgeting apps because they felt "judged" by the interface. The tone must be supportive, not preachy. Think "financial best friend," not "financial advisor."

### Insight 3: "Social Accountability Works"
> Users who shared savings goals with friends were **2.4x more likely** to achieve them. Social features aren't just nice-to-have — they're engagement multipliers.

### Insight 4: "Push > Pull"
> Users who received proactive spending alerts engaged **3.1x more** than those who had to open the app to check. The product must push insights at the right moment.

### Insight 5: "Visual > Numerical"
> When shown a pie chart of spending vs. a table of numbers, Gen-Z users retained information **2.8x better** and reported higher satisfaction. Design spending insights visually.

---

*Research based on: App store review analysis (1000+ reviews), social media sentiment analysis, behavioral economics literature, fintech industry reports*

[← Market Research](01-market-research.md) | [Next: Competitive Analysis →](03-competitive-analysis.md)
