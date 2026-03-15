# 🗺️ Product Roadmap: slice Smart Budgets

## 1. Vision & North Star

### Product Vision
> Make every young Indian feel confident and in control of their money — one smart nudge at a time.

### North Star Metric
**Weekly Active Budgeters (WAB):** Number of users who check or interact with their budget at least once per week.

*Why this metric?* It captures the intersection of adoption (users activated the feature), engagement (they come back weekly), and value delivery (they find it useful enough to return).

---

## 2. Phased Roadmap

### Phase 0: Foundation (Weeks 1-4) — "See Your Money"
> Build the data backbone and basic spending visibility

| Feature | Description | Effort | Impact |
|---------|------------|:------:|:------:|
| Transaction Categorization Engine | Auto-categorize transactions using UPI merchant codes + rules | L | 🔴 Critical |
| Spending Summary Dashboard | Visual breakdown of spending by category (pie + bar charts) | M | 🔴 Critical |
| Monthly Spending History | Month-over-month comparison of spending | S | 🟡 High |
| Category Labels & Icons | Intuitive categories: Food, Shopping, Transport, Entertainment, Bills, Others | S | 🟡 High |
| Manual Category Correction | Allow users to re-categorize transactions (feeds back to ML) | S | 🟢 Medium |

**Success Metrics:**
- 50% of MAU view spending dashboard at least once
- Category accuracy > 85% (measured by manual correction rate)
- Avg. time on spending screen > 30 seconds

---

### Phase 1: Control (Weeks 5-10) — "Own Your Money"
> Give users the tools to set budgets and get alerts

| Feature | Description | Effort | Impact |
|---------|------------|:------:|:------:|
| Budget Setting by Category | Set monthly limits for each spending category | M | 🔴 Critical |
| Smart Budget Suggestions | AI-suggested budgets based on 3-month spending history | M | 🟡 High |
| Budget Progress Bar | Visual tracker showing % spent vs. budget per category | S | 🔴 Critical |
| Proactive Nudge Alerts | Push notification at 50%, 80%, 100% of budget | M | 🔴 Critical |
| Bill Due Date Tracker | Consolidated view of upcoming bills with countdown | S | 🟡 High |
| Subscription Detector | Auto-identify recurring charges; flag forgotten subscriptions | M | 🟡 High |

**Success Metrics:**
- 30% of dashboard users set at least one budget
- Budget alert open rate > 35%
- 15% reduction in overspending for budget-active users (vs. control)
- Subscription detector surfaces avg. 2.1 forgotten subscriptions per user

---

### Phase 2: Delight (Weeks 11-18) — "Love Your Money"
> Add gamification and social features that make budgeting sticky

| Feature | Description | Effort | Impact |
|---------|------------|:------:|:------:|
| Savings Streaks | Track consecutive days/weeks of staying under budget | S | 🟡 High |
| Achievement Badges | Unlock badges: "First Budget", "7-Day Streak", "₹5K Saved", etc. | S | 🟡 High |
| Weekly "Money Mood" Digest | Fun, visual weekly summary delivered as in-app story | M | 🔴 Critical |
| Savings Goal Tracker | Set goals ("New Phone", "Trip to Goa") with progress visualization | M | 🟡 High |
| Social Money Challenges | Challenge friends: "No food delivery week", "₹1000 savings race" | L | 🟡 High |
| Shareable Milestones | "I saved ₹10K this month on slice!" — shareable card for social media | S | 🟢 Medium |

**Success Metrics:**
- 40% of budget users engage with gamification features
- Avg. savings streak > 5 days
- Social challenge feature drives 0.3 viral coefficient
- Money Mood digest achieves 45% open rate
- 10% of milestone cards shared to external platforms

---

### Phase 3: Intelligence (Weeks 19-26) — "Grow Your Money"
> Evolve to AI-driven financial coaching and cross-sell

| Feature | Description | Effort | Impact |
|---------|------------|:------:|:------:|
| AI Spending Coach | Personalized tips based on spending patterns ("You spend 30% more on weekends") | L | 🟡 High |
| Predictive Budget Alerts | "At this rate, you'll exceed your food budget by ₹2,000" | L | 🟡 High |
| Credit Health Score | Simple score: How well are you managing your slice credit? | M | 🟡 High |
| Personalized Offers | Offer relevant deals based on spending categories | M | 🟢 Medium |
| Account Aggregator Integration | Pull in bank account data for holistic view (AA framework) | L | 🟢 Medium |
| Financial Wellness Score | Composite score combining budgets, credit, savings, spending patterns | L | 🟡 High |

**Success Metrics:**
- AI coach tips achieve 25% action rate
- Predictive alerts prevent 20% of budget overruns
- Credit health score engagement > 30% MAU
- Personalized offers drive 5% higher conversion vs. generic offers

---

## 3. RICE Prioritization Framework

### Scoring Legend
- **Reach:** % of MAU impacted (1-10 scale)
- **Impact:** Effect on North Star Metric (1-5 scale: Minimal → Massive)
- **Confidence:** Data supporting this bet (1-5 scale: Low → Certain)
- **Effort:** Engineering weeks (person-weeks)

| Feature | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---------|:-----:|:------:|:----------:|:------:|:----------:|:--------:|
| Transaction Categorization | 10 | 5 | 4 | 6 | 33.3 | 🥇 1 |
| Spending Dashboard | 10 | 4 | 5 | 4 | 50.0 | 🥇 2 |
| Budget Setting | 8 | 5 | 4 | 5 | 32.0 | 🥇 3 |
| Proactive Nudge Alerts | 8 | 5 | 4 | 4 | 40.0 | 🥇 4 |
| Weekly Money Mood Digest | 7 | 4 | 3 | 3 | 28.0 | 🥈 5 |
| Savings Streaks | 6 | 3 | 3 | 2 | 27.0 | 🥈 6 |
| Subscription Detector | 5 | 4 | 4 | 4 | 20.0 | 🥈 7 |
| Social Money Challenges | 4 | 3 | 2 | 8 | 3.0 | 🥉 8 |
| AI Spending Coach | 5 | 4 | 2 | 10 | 4.0 | 🥉 9 |
| Account Aggregator | 3 | 3 | 2 | 12 | 1.5 | 🥉 10 |

---

## 4. Dependency Map

```
Phase 0: FOUNDATION
  │
  ├── Transaction Categorization Engine ──────────┐
  │       │                                       │
  │       ▼                                       │
  ├── Spending Summary Dashboard                  │
  │       │                                       │
  │       ▼                                       │
  └── Monthly History + Category Fixes            │
                                                  │
Phase 1: CONTROL                                  │
  │                                               │
  ├── Budget Setting ◄────────────────────────────┘
  │       │
  │       ├── Smart Budget Suggestions (needs 3 months of data)
  │       │
  │       ▼
  ├── Budget Progress Bar
  │       │
  │       ▼
  ├── Proactive Nudge Alerts
  │
  ├── Subscription Detector (independent)
  └── Bill Tracker (independent)

Phase 2: DELIGHT
  │
  ├── Savings Streaks (needs budget tracking)
  ├── Achievement Badges (needs streaks)
  ├── Money Mood Digest (needs categorization + budget data)
  ├── Social Challenges (needs streaks + friends list)
  └── Shareable Milestones (needs badges/streaks)

Phase 3: INTELLIGENCE
  │
  ├── AI Coach (needs 3+ months of user behavior data)
  ├── Predictive Alerts (needs spending patterns)
  ├── Credit Health (needs budget + payment history)
  └── Account Aggregator (independent, regulatory dependent)
```

---

## 5. Risk & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|:----------:|:------:|-----------|
| Categorization accuracy < 85% | Medium | High | Start with UPI codes + rules; add ML gradually; allow user corrections |
| Low adoption of budgets | Medium | High | Make budgets optional; lead with insights dashboard; auto-suggest budgets |
| Notification fatigue | Medium | Medium | Smart batching; frequency caps; user preference settings |
| Privacy backlash | Low | High | Transparent consent; on-device processing option; easy opt-out |
| Engineering capacity | Medium | Medium | Phase 0 uses mostly existing data; minimal new infrastructure |
| Competitor launches first | Low | High | Speed to market; leverage existing user base; iterate faster |

---

## 6. Resource Estimation

| Phase | Duration | Engineering | Design | Data Science | Product |
|-------|:--------:|:-----------:|:------:|:------------:|:-------:|
| Phase 0 | 4 weeks | 3 engineers | 1 designer | 1 data scientist | 1 PM |
| Phase 1 | 6 weeks | 4 engineers | 1 designer | 1 data scientist | 1 PM |
| Phase 2 | 8 weeks | 3 engineers | 2 designers | 0.5 data scientist | 1 PM |
| Phase 3 | 8 weeks | 5 engineers | 1 designer | 2 data scientists | 1 PM |
| **Total** | **26 weeks** | **~15 engineer-months** | **~5 designer-months** | **~4.5 DS-months** | **6 PM-months** |

---

[← Problem Statement](04-problem-statement.md) | [Next: Feature Specifications →](06-feature-specifications.md)
