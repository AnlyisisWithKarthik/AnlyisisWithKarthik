# 📈 Metrics Framework: Measuring Smart Budgets Success

## 1. North Star Metric

### **Weekly Active Budgeters (WAB)**
> Number of unique users who interact with any Smart Budgets feature at least once per week.

**Why this metric?**
- Captures **adoption** (users activated the feature)
- Captures **engagement** (they return weekly)
- Captures **value delivery** (they find it useful enough to return)
- Directly correlates with business outcomes (DAU, retention, transaction frequency)

**Target:** 2M WAB within 6 months of full launch (25% of MAU)

---

## 2. Metric Hierarchy (Input → Output)

```
                        ┌─────────────────────────┐
                        │   BUSINESS OUTCOMES      │
                        │   (Revenue, Retention,   │
                        │    Growth)               │
                        └───────────┬─────────────┘
                                    │
                        ┌───────────▼─────────────┐
                        │   NORTH STAR             │
                        │   Weekly Active          │
                        │   Budgeters (WAB)        │
                        └───────────┬─────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
    ┌─────────▼─────────┐ ┌───────▼─────────┐ ┌────────▼────────┐
    │   ADOPTION         │ │   ENGAGEMENT     │ │   OUTCOMES       │
    │   Metrics          │ │   Metrics        │ │   Metrics        │
    └─────────┬─────────┘ └───────┬─────────┘ └────────┬────────┘
              │                   │                     │
    • Activation Rate      • DAU/MAU Ratio       • Overspending ↓
    • Budget Set Rate      • Session Frequency    • Default Rate ↓
    • Feature Discovery    • Time in Feature      • Support Tickets ↓
    • Onboarding Complete  • Nudge Engagement     • Transaction Freq ↑
                           • Streak Length         • NPS Score
                           • Digest Open Rate      • Referral Rate
```

---

## 3. Detailed Metrics by Phase

### Phase 0: Foundation Metrics

| Metric | Definition | Target | Measurement Method |
|--------|-----------|--------|-------------------|
| **Feature Discovery Rate** | % of MAU who discover Smart Budgets tab | 60% in 30 days | In-app analytics (tab opens) |
| **Dashboard View Rate** | % of discoverers who view full dashboard | 70% | Funnel analysis |
| **Avg. Time on Dashboard** | Time spent on spending dashboard | > 30 sec | Session tracking |
| **Categorization Accuracy** | % of transactions correctly categorized | > 85% | Manual correction rate (proxy) |
| **Category Correction Rate** | % of transactions users re-categorize | < 15% | User correction events |

### Phase 1: Control Metrics

| Metric | Definition | Target | Measurement Method |
|--------|-----------|--------|-------------------|
| **Budget Activation Rate** | % of dashboard users who set ≥1 budget | 30% in 60 days | Feature activation tracking |
| **Avg. Budgets per User** | Number of category budgets set per user | 2.5 | Aggregate tracking |
| **Nudge Delivery Rate** | % of nudges successfully delivered | > 95% | Push notification analytics |
| **Nudge Open Rate** | % of nudges opened/acted upon | > 35% | Notification tap-through |
| **Budget Adherence Rate** | % of budgets stayed within for the month | > 45% | End-of-month calculation |
| **Overspending Reduction** | % less overspending vs. pre-feature baseline | -15% | Cohort comparison |
| **Subscription Discovery** | Avg. subscriptions surfaced per user | 2.1 | Detection algorithm output |

### Phase 2: Delight Metrics

| Metric | Definition | Target | Measurement Method |
|--------|-----------|--------|-------------------|
| **Streak Participation Rate** | % of budget users with active streak | 50% | Streak tracking |
| **Avg. Streak Length** | Average consecutive days in budget | > 5 days | Streak calculation |
| **Badge Unlock Rate** | Avg. badges earned per user per month | 1.5 | Badge system tracking |
| **Digest Open Rate** | % of Money Mood digests opened | 45% | Story view analytics |
| **Digest Completion Rate** | % who swipe through all cards | 60% | Story completion tracking |
| **Social Share Rate** | % who share milestones externally | 8% | Share button analytics |
| **Challenge Participation** | % of users who join/create challenges | 15% | Challenge feature tracking |
| **Viral Coefficient** | New users acquired per existing user | 0.3 | Referral tracking |

### Phase 3: Intelligence Metrics

| Metric | Definition | Target | Measurement Method |
|--------|-----------|--------|-------------------|
| **AI Tip Action Rate** | % of AI tips that lead to behavior change | 25% | Before/after spending comparison |
| **Predictive Alert Accuracy** | % of predictions within 10% of actual | > 80% | Prediction vs. actual |
| **Credit Health Engagement** | % MAU who check credit health score | 30% | Feature view tracking |
| **Cross-Sell Conversion** | % who take personalized offers | 5% | Offer funnel analytics |

---

## 4. Business Impact Metrics

| Metric | Baseline (Pre-Feature) | Target (6 Months Post) | Measurement |
|--------|:---------------------:|:---------------------:|-------------|
| **DAU/MAU Ratio** | 22% | 30% (+36%) | App analytics |
| **Monthly Transaction Frequency** | 18 transactions | 22 transactions (+22%) | Transaction data |
| **30-Day Retention** | 45% | 55% (+22%) | Cohort retention curves |
| **90-Day Retention** | 28% | 38% (+36%) | Cohort retention curves |
| **Credit Default Rate** | 3.2% | 2.9% (-9%) | NPA tracking |
| **Support Ticket Volume** | 100% (baseline) | 75% (-25%) billing-related | Support analytics |
| **NPS (Feature)** | N/A | ≥ 50 | In-app survey |
| **NPS (Overall App)** | 35 | 42 (+20%) | Periodic survey |
| **Organic Install Rate** | 15% | 20% (+33%) | Attribution analytics |

---

## 5. A/B Testing Plan

### Test 1: Dashboard Design (Phase 0)

| Element | Variant A (Control) | Variant B (Test) |
|---------|-------------------|-----------------|
| **Layout** | Pie chart + list | Donut chart + card grid |
| **Color** | Muted colors | Vibrant, category-specific |
| **CTA** | "View Details" | "See where your ₹ went" |
| **Hypothesis** | — | Vibrant, conversational design drives +15% engagement |
| **Sample Size** | 50K users | 50K users |
| **Duration** | 2 weeks | — |
| **Primary Metric** | Avg. time on dashboard | — |
| **Secondary Metrics** | Tap-through rate, return rate | — |

### Test 2: Nudge Messaging (Phase 1)

| Element | Variant A (Formal) | Variant B (Friendly) | Variant C (Gamified) |
|---------|-------------------|---------------------|---------------------|
| **80% Alert** | "You have used 80% of your Food budget" | "Heads up! Food budget at 80% 🔔" | "⚡ Level up! 80% of food budget used. Stay in the green to keep your streak!" |
| **Hypothesis** | Baseline | +10% open rate | +20% open rate, +5% adherence |
| **Sample Size** | 30K each | — | — |
| **Duration** | 1 month | — | — |
| **Primary Metric** | Nudge open rate + budget adherence | — | — |

### Test 3: Gamification Impact (Phase 2)

| Element | Control | With Streaks | With Streaks + Badges |
|---------|---------|-------------|---------------------|
| **Features** | Budgets + alerts only | + streak counter | + streak + badges + milestones |
| **Hypothesis** | Baseline | +15% retention | +25% retention |
| **Sample Size** | 40K each | — | — |
| **Duration** | 6 weeks | — | — |
| **Primary Metric** | 30-day retention | — | — |
| **Secondary Metrics** | DAU, budget adherence, NPS | — | — |

### Test 4: Digest Format (Phase 2)

| Element | Variant A | Variant B |
|---------|----------|----------|
| **Format** | Push notification summary | In-app Instagram-style story |
| **Hypothesis** | — | Stories get +30% engagement vs. push |
| **Sample Size** | 50K each | — |
| **Duration** | 4 weeks | — |
| **Primary Metric** | Open rate + completion rate | — |

---

## 6. Monitoring & Alerting

### Real-Time Dashboards

| Dashboard | Metrics | Refresh Rate | Audience |
|-----------|---------|:------------:|---------|
| **Smart Budgets Health** | WAB, activation rate, nudge delivery, errors | Real-time | Engineering + Product |
| **Engagement Overview** | DAU, session duration, feature usage | Hourly | Product + Leadership |
| **Business Impact** | Transaction frequency, default rate, support tickets | Daily | Leadership + Finance |
| **A/B Test Monitor** | Variant metrics, statistical significance | Hourly | Product + Data Science |

### Alert Thresholds

| Metric | Warning Threshold | Critical Threshold | Action |
|--------|:-:|:-:|--------|
| Categorization accuracy | < 82% | < 75% | Review categorization rules; add merchant mappings |
| Nudge delivery rate | < 92% | < 85% | Check push notification service; investigate failures |
| Dashboard load time | > 3 sec (P95) | > 5 sec (P95) | Scale infrastructure; optimize queries |
| WAB week-over-week change | -10% | -20% | Investigate UX issues; check for bugs |
| Budget abandon rate | > 40% | > 60% | Survey users; simplify budget UX |

---

## 7. Reporting Cadence

| Report | Frequency | Audience | Content |
|--------|:---------:|---------|---------|
| **Daily Pulse** | Daily | Product Team | WAB, activation, key metrics, anomalies |
| **Weekly Review** | Weekly | Product + Engineering | Metric trends, A/B updates, bug impact |
| **Monthly Business Review** | Monthly | Leadership | Business impact, retention, growth, roadmap progress |
| **Quarterly OKR Review** | Quarterly | All stakeholders | OKR progress, strategic pivots, next quarter plan |

---

[← Feature Specifications](06-feature-specifications.md) | [Next: Go-to-Market Strategy →](08-go-to-market-strategy.md)
