# 📋 Feature Specifications: slice Smart Budgets

## Feature 1: Smart Spending Dashboard

### Overview
An always-visible spending intelligence hub that auto-categorizes every transaction and presents spending in beautiful, glanceable visualizations.

### User Stories

| # | As a... | I want to... | So that... |
|---|---------|-------------|-----------|
| 1.1 | slice user | See my spending broken down by category | I know where my money is going |
| 1.2 | slice user | View a visual pie chart of monthly spending | I can quickly spot my biggest expense areas |
| 1.3 | slice user | Compare this month's spending with last month | I can identify if I'm spending more or less |
| 1.4 | slice user | Tap into a category to see individual transactions | I can identify specific expenses |
| 1.5 | slice user | Correct a transaction's category | I can fix auto-categorization mistakes |

### Acceptance Criteria

**AC 1.1: Spending Categorization**
```
GIVEN a user has made transactions via slice (UPI or card)
WHEN they open the Smart Budgets tab
THEN all transactions are automatically grouped into categories:
  - 🍔 Food & Dining (restaurants, food delivery, groceries)
  - 🛍️ Shopping (e-commerce, retail, fashion)
  - 🚗 Transport (cab, fuel, public transport)
  - 🎬 Entertainment (streaming, gaming, movies)
  - 💡 Bills & Utilities (electricity, internet, phone)
  - 💊 Health (pharmacy, hospitals, insurance)
  - 🎓 Education (courses, books, fees)
  - 💸 Transfers (P2P, UPI transfers)
  - 📦 Others (uncategorized)
AND each category shows total amount and % of overall spend
AND categorization accuracy is ≥ 85%
```

**AC 1.2: Visual Dashboard**
```
GIVEN the user is on the Smart Budgets tab
THEN they see:
  - A donut/pie chart with spending by category (color-coded)
  - Total spend amount prominently displayed
  - Date range selector (this month / last month / custom)
  - Top 3 spending categories highlighted
  - A horizontal bar chart showing month-over-month comparison
```

**AC 1.3: Category Drill-Down**
```
GIVEN the user taps on a spending category
THEN they see:
  - List of all transactions in that category
  - Each transaction shows: merchant name, amount, date, time
  - Option to re-categorize any transaction
  - Sub-total for the category
```

### Technical Notes
- Use UPI MCC (Merchant Category Codes) as primary categorization signal
- Supplement with merchant name matching (regex + lookup table)
- Store user corrections to improve categorization over time
- Cache dashboard data; refresh on new transaction or pull-to-refresh
- Consider on-device categorization for privacy-sensitive users

### Design Requirements
- Dashboard must load in < 2 seconds
- Charts must be interactive (tap for details)
- Use slice's existing color palette and design system
- Support dark mode
- Accessible: minimum contrast ratio 4.5:1; screen reader compatible

---

## Feature 2: Budget Setting & Alerts

### Overview
Users can set monthly spending limits per category and receive proactive nudges when approaching or exceeding their budget.

### User Stories

| # | As a... | I want to... | So that... |
|---|---------|-------------|-----------|
| 2.1 | slice user | Set a monthly budget for any spending category | I have a target to control my spending |
| 2.2 | new user | Get AI-suggested budgets based on my history | I don't have to guess what's realistic |
| 2.3 | slice user | See a progress bar showing % of budget used | I know how much room I have left |
| 2.4 | slice user | Get an alert when I've used 80% of a budget | I can slow down before overspending |
| 2.5 | slice user | Get a friendly notification when I bust a budget | I'm aware and can adjust next month |

### Acceptance Criteria

**AC 2.1: Budget Creation**
```
GIVEN a user is on the spending dashboard
WHEN they tap "Set Budget" on any category
THEN they see:
  - A slider/input to set monthly limit (₹100 - ₹1,00,000)
  - Their average spend in that category (last 3 months)
  - AI-suggested budget (avg spend + 10% buffer)
  - Option to set budgets for multiple categories at once
AND the budget is saved and tracked from that moment
```

**AC 2.2: Budget Progress**
```
GIVEN a user has set a budget for a category
WHEN they view the dashboard
THEN the category shows:
  - A progress bar (green 0-50%, yellow 50-80%, orange 80-100%, red >100%)
  - "₹X of ₹Y spent" text below the bar
  - Days remaining in the month
  - Projected month-end spend based on current pace
```

**AC 2.3: Smart Nudges**
```
GIVEN a user has set a budget
WHEN they reach 50% of their budget:
  THEN send an in-app message: "Halfway through your [Category] budget — ₹X left for Y days 👍"
WHEN they reach 80% of their budget:
  THEN send a push notification: "Heads up! You've used 80% of your [Category] budget. ₹X left for Y days 🔔"
WHEN they exceed 100% of their budget:
  THEN send a push notification: "You've gone over your [Category] budget by ₹X. No stress — let's plan better next month 💪"
AND all nudge messages use a supportive, non-judgmental tone
AND users can configure nudge frequency (every threshold / critical only / off)
```

### Behavioral Design Principles
1. **Non-judgmental tone** — Never use words like "failed" or "bad"; always forward-looking
2. **Actionable** — Every alert suggests a next step
3. **Timely** — Alert at the moment of decision, not after the fact
4. **Respectful** — User controls notification frequency; smart batching
5. **Celebratory** — Acknowledge when users stay within budget

---

## Feature 3: Savings Streaks & Gamification

### Overview
A gamification layer that makes budget adherence feel rewarding through streaks, badges, and social challenges.

### User Stories

| # | As a... | I want to... | So that... |
|---|---------|-------------|-----------|
| 3.1 | slice user | See a streak counter for days I've stayed in budget | I feel motivated to maintain it |
| 3.2 | slice user | Earn badges for financial milestones | I get a sense of accomplishment |
| 3.3 | slice user | Challenge friends to savings competitions | We hold each other accountable |
| 3.4 | slice user | Share my milestones on social media | I can celebrate wins publicly |

### Acceptance Criteria

**AC 3.1: Savings Streaks**
```
GIVEN a user has active budgets
WHEN they stay within ALL budgets for a full day
THEN their streak counter increments by 1
AND a subtle animation plays on the dashboard

WHEN they exceed any budget
THEN their streak resets to 0
AND they see an encouraging message: "Streaks restart tomorrow. You've got this! 🚀"

Streak Milestones:
  - 3 days: "Getting started!" (fire emoji)
  - 7 days: "One week strong!" (star emoji)
  - 14 days: "Two week champion!" (trophy emoji)
  - 30 days: "Monthly master!" (crown emoji)
  - 90 days: "Legendary saver!" (diamond emoji)
```

**AC 3.2: Achievement Badges**
```
Badge Collection:
  - 🎯 "First Budget" — Set your first budget
  - 🔥 "Hot Streak" — 7-day budget streak
  - 💪 "Category King" — Stay in budget for one category for a full month
  - 🏆 "Budget Boss" — Stay in all budgets for a full month
  - 🎉 "Saver Alert" — Save ₹5,000+ vs. previous month's spending
  - 👥 "Challenge Accepted" — Complete your first social challenge
  - 📊 "Data Nerd" — Check your spending dashboard 30 times
  - 🌟 "Money Mood Master" — Read 10 consecutive weekly digests
  - 💎 "Quarter Legend" — 90-day streak (ultra rare)

Display: Badge collection viewable on profile; earned badges highlighted; unearned badges shown as silhouettes with unlock hints
```

**AC 3.3: Social Money Challenges**
```
GIVEN a user wants to start a challenge
WHEN they tap "Start Challenge"
THEN they can:
  - Choose a challenge type:
    • "No [Category] Week" — ₹0 in a category for 7 days
    • "Savings Race" — Who saves more this month?
    • "Budget Buddies" — Both stay in budget for 14 days
    • Custom challenge (set own rules)
  - Invite 1-5 friends via slice contacts
  - Set duration (3/7/14/30 days)

Challenge Flow:
  1. Creator sets challenge → Friends get notification
  2. Friends accept/decline within 24 hours
  3. Progress tracked automatically via spending data
  4. Daily leaderboard updates
  5. Winner gets special badge + bragging rights card

Privacy: Only challenge-related spending categories are visible; individual transactions are NEVER shared
```

---

## Feature 4: Weekly "Money Mood" Digest

### Overview
A weekly personalized financial summary delivered as an engaging in-app story format — think Instagram Stories meets financial wellness.

### User Stories

| # | As a... | I want to... | So that... |
|---|---------|-------------|-----------|
| 4.1 | slice user | Get a fun weekly summary of my spending | I stay engaged with my finances without effort |
| 4.2 | slice user | See my "money mood" for the week | I get a quick vibe check on my financial health |
| 4.3 | slice user | Share my Money Mood card on social media | I can engage my friends in financial awareness |

### Acceptance Criteria

**AC 4.1: Weekly Digest Content**
```
Delivered: Every Monday at 9:00 AM (configurable)
Format: Instagram-story-style cards (swipeable)

Card 1: "Money Mood" Score
  - Emoji-based mood: 😎 Chill | 😊 Good | 😐 Meh | 😬 Tight | 🔥 Overspent
  - One-liner: "You spent ₹X this week — that's Y% [more/less] than last week"

Card 2: Top Categories
  - Top 3 spending categories with amounts
  - Visual bars showing each category
  - Fun insight: "Swiggy was your BFF this week! 🍕"

Card 3: Budget Health
  - Green/Yellow/Red status for each active budget
  - Days left in the month
  - Projected month-end status

Card 4: Streak & Badges
  - Current streak count
  - Any new badges earned this week
  - Encouragement or celebration message

Card 5: Weekly Tip
  - Personalized financial tip based on spending pattern
  - Example: "You spent ₹2,100 on food delivery. Cooking 2 meals this week could save ₹800! 🍳"

Card 6: Shareable Summary Card
  - Beautiful, branded card with key stats
  - "Share to Instagram" / "Share to WhatsApp" buttons
  - No sensitive amounts on shareable card — only mood + streak
```

---

## Feature 5: Subscription Detector

### Overview
Automatically detect recurring charges and alert users to subscriptions they may have forgotten about.

### User Stories

| # | As a... | I want to... | So that... |
|---|---------|-------------|-----------|
| 5.1 | slice user | See all my active subscriptions in one place | I know what I'm paying for monthly |
| 5.2 | slice user | Get alerted about subscriptions I haven't used | I can cancel things I don't need |
| 5.3 | slice user | See total monthly subscription spend | I understand my recurring costs |

### Acceptance Criteria

**AC 5.1: Subscription Detection**
```
GIVEN a user has recurring transactions
WHEN the system detects 2+ charges from the same merchant in 60 days
  with similar amounts (within 10% variance)
THEN it's flagged as a potential subscription

Detection covers:
  - OTT platforms (Netflix, Hotstar, Prime, Spotify, YouTube Premium)
  - Cloud storage (Google One, iCloud)
  - Food (Zomato Pro, Swiggy One)
  - Fitness (Cult, gym memberships)
  - Software (Adobe, Notion, others)
  - Any other recurring merchant

Dashboard shows:
  - Subscription name & logo
  - Monthly cost
  - Next expected charge date
  - "Last used" indicator (if available via app usage data)
  - Total annual cost
```

**AC 5.2: Smart Alerts**
```
GIVEN a subscription has been detected
AND the user hasn't transacted with that merchant in 30+ days (beyond subscription)
THEN send an in-app notification:
  "You're paying ₹X/month for [Service]. Haven't used it in 30 days — want to review? 🤔"
  Options: [Keep] [Remind me later] [Help me cancel]
```

---

## 6. Non-Functional Requirements

| Requirement | Specification |
|-------------|--------------|
| **Performance** | Dashboard loads in < 2 seconds; budget updates < 5 seconds |
| **Availability** | 99.9% uptime for budget tracking; nudges delivered within 5 minutes |
| **Scalability** | Handle 8M MAU with 50 transactions/user/month |
| **Security** | All spending data encrypted at rest and in transit; no PII in analytics |
| **Privacy** | DPDP Act compliant; explicit consent for categorization; easy opt-out |
| **Accessibility** | WCAG 2.1 AA compliant; screen reader support; minimum 4.5:1 contrast |
| **Localization** | English and Hindi at launch; add 3 more languages in Phase 2 |
| **Backward Compatibility** | Works on Android 8+ and iOS 14+; graceful degradation on older devices |

---

[← Product Roadmap](05-product-roadmap.md) | [Next: Metrics Framework →](07-metrics-framework.md)
