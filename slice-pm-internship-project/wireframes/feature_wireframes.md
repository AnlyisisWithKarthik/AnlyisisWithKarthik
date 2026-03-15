# 📱 Feature Wireframes: slice Smart Budgets

> Low-fidelity wireframe descriptions and user flow diagrams for the Smart Budgets feature set.
> These wireframes serve as a blueprint for design and engineering teams.

---

## 1. Entry Point: Smart Budgets Tab

### Screen: Home Tab with Smart Budgets Entry

```
┌─────────────────────────────────┐
│  🍕 slice                    ⚙️ │
├─────────────────────────────────┤
│                                 │
│  ┌───────────────────────────┐  │
│  │    Available Balance      │  │
│  │    ₹ 42,500              │  │
│  │    ─────────────          │  │
│  │    Credit Limit: ₹75,000 │  │
│  └───────────────────────────┘  │
│                                 │
│  ┌───────────────────────────┐  │
│  │ 📊 Smart Budgets    NEW! │  │
│  │                           │  │
│  │ This week: ₹4,200 spent  │  │
│  │ You're on track! 🟢      │  │
│  │                           │  │
│  │ [See full breakdown →]    │  │
│  └───────────────────────────┘  │
│                                 │
│  Recent Transactions            │
│  ├─ Swiggy        -₹349   🍔  │
│  ├─ Uber          -₹180   🚗  │
│  ├─ Amazon        -₹1,299 🛍️  │
│  └─ Netflix       -₹199   🎬  │
│                                 │
├─────────────────────────────────┤
│  🏠    💳    📊    👤    ⋯   │
│  Home  Card  Budget Profile More│
└─────────────────────────────────┘
```

**Interaction Notes:**
- The Smart Budgets card is a prominent entry point on the home screen
- Shows a quick summary: weekly spend + status indicator (green/yellow/red)
- Tapping the card or the Budget tab icon opens the full dashboard
- "NEW!" badge for first 30 days after feature launch

---

## 2. Smart Budgets Dashboard

### Screen: Spending Overview

```
┌─────────────────────────────────┐
│  ← Smart Budgets         ⚙️ 🔔 │
├─────────────────────────────────┤
│                                 │
│  March 2025                 ▼   │
│  ₹18,420 spent                  │
│  of ₹25,000 budget             │
│                                 │
│      ┌─────────────┐           │
│      │   🍩 DONUT  │           │
│      │   CHART     │           │
│      │             │           │
│      │  Food  32%  │           │
│      │  Shop  22%  │           │
│      │  Trans 14%  │           │
│      │  Enter  8%  │           │
│      │  Bills 22%  │           │
│      │  Other  2%  │           │
│      └─────────────┘           │
│                                 │
│  Category Budgets               │
│  ┌───────────────────────────┐  │
│  │ 🍔 Food & Dining         │  │
│  │ ₹5,890 of ₹7,000    84% │  │
│  │ ████████████████░░░  🟡  │  │
│  │ ₹1,110 left • 8 days     │  │
│  └───────────────────────────┘  │
│  ┌───────────────────────────┐  │
│  │ 🛍️ Shopping              │  │
│  │ ₹3,200 of ₹5,000    64% │  │
│  │ ████████████░░░░░░░  🟢  │  │
│  │ ₹1,800 left • 8 days     │  │
│  └───────────────────────────┘  │
│  ┌───────────────────────────┐  │
│  │ 🚗 Transport              │  │
│  │ ₹2,580 of ₹2,500   103% │  │
│  │ ████████████████████ 🔴  │  │
│  │ Over by ₹80               │  │
│  └───────────────────────────┘  │
│                                 │
│  [+ Add Budget]                 │
│                                 │
│  ─── This Week ───              │
│  🔥 5-day streak!              │
│  📊 Money Mood: 😊 Good        │
│                                 │
├─────────────────────────────────┤
│  🏠    💳    📊    👤    ⋯   │
└─────────────────────────────────┘
```

**Interaction Notes:**
- Month selector at top (swipe or dropdown)
- Interactive donut chart: tap a segment to drill down
- Each budget category card shows: amount spent, budget limit, %, visual bar, remaining amount, days left
- Color coding: 🟢 0-50%, 🟡 50-80%, 🟠 80-100%, 🔴 >100%
- "Add Budget" CTA prominent for categories without budgets
- Streak and Money Mood summary at bottom for engagement

---

## 3. Category Drill-Down

### Screen: Food & Dining Detail

```
┌─────────────────────────────────┐
│  ← 🍔 Food & Dining            │
├─────────────────────────────────┤
│                                 │
│  March 2025                     │
│  ₹5,890 of ₹7,000 budget       │
│  ████████████████░░░  84% 🟡   │
│                                 │
│  📈 Trend: +12% vs last month  │
│  💡 Tip: 3 less food orders     │
│     could save you ₹900!       │
│                                 │
│  ─── Transactions ───           │
│                                 │
│  Today                          │
│  ├─ Swiggy         -₹349  🍔  │
│  │  12:30 PM • Food Delivery    │
│  │                    [Edit ✏️] │
│  ├─ Chaayos         -₹180  ☕  │
│  │  10:15 AM • Cafe             │
│  │                    [Edit ✏️] │
│                                 │
│  Yesterday                      │
│  ├─ Zomato          -₹520  🍔  │
│  │  8:45 PM • Food Delivery     │
│  ├─ BigBasket       -₹1,245 🛒 │
│  │  6:00 PM • Groceries         │
│                                 │
│  Mar 12                         │
│  ├─ Domino's        -₹450  🍕  │
│  │  9:15 PM • Restaurant        │
│  ├─ Starbucks       -₹380  ☕  │
│  │  3:00 PM • Cafe              │
│                                 │
│  [Load More ↓]                  │
│                                 │
│  ─── Monthly Comparison ───     │
│                                 │
│  Feb: ₹5,250  ████████████░░░  │
│  Mar: ₹5,890  ██████████████░  │
│  (so far)      +₹640 (+12%)    │
│                                 │
│  [Adjust Budget]                │
│                                 │
├─────────────────────────────────┤
│  🏠    💳    📊    👤    ⋯   │
└─────────────────────────────────┘
```

**Interaction Notes:**
- Shows trend vs. previous month
- Personalized tip based on spending pattern
- Each transaction has an "Edit" button for re-categorization
- Monthly comparison bar at bottom
- "Adjust Budget" CTA to modify budget if unrealistic

---

## 4. Budget Setting Flow

### Screen: Set Budget (Bottom Sheet)

```
┌─────────────────────────────────┐
│                                 │
│  (Background: Dashboard - dim)  │
│                                 │
├─────────────────────────────────┤
│  ━━━━━━━━━ (drag handle)        │
│                                 │
│  Set Budget for 🍔 Food         │
│                                 │
│  Your average spend (3 months): │
│  ₹6,200/month                  │
│                                 │
│  💡 Suggested: ₹6,800          │
│  (Your avg + 10% buffer)        │
│                                 │
│         ₹ [  7,000  ]          │
│                                 │
│  ◄━━━━━━━━━━━━●━━━━━►          │
│  ₹1,000            ₹15,000     │
│                                 │
│  Alerts:                        │
│  ☑ At 50%  (₹3,500)           │
│  ☑ At 80%  (₹5,600)  🔔       │
│  ☑ At 100% (₹7,000)  🔔       │
│                                 │
│  ┌─────────────────────────┐    │
│  │    Set Budget  ✓        │    │
│  └─────────────────────────┘    │
│                                 │
│  [Skip for now]                 │
│                                 │
└─────────────────────────────────┘
```

**Interaction Notes:**
- Bottom sheet slides up over dashboard
- Shows historical average as context
- AI-suggested budget prominently displayed
- Slider + text input for amount
- Alert thresholds configurable with toggle switches
- "Set Budget" primary CTA; "Skip" secondary option
- Success animation on save (confetti + streak starts)

---

## 5. Nudge Notifications

### Notification: 80% Budget Alert

```
┌─────────────────────────────────┐
│ 🍕 slice                   now │
│                                 │
│ 🔔 Budget Alert: Food & Dining │
│                                 │
│ You've used 80% of your food    │
│ budget! ₹1,400 left for 8 days │
│                                 │
│ [View Budget]  [Got it 👍]     │
└─────────────────────────────────┘
```

### In-App Alert: Budget Exceeded

```
┌─────────────────────────────────┐
│                                 │
│  (Overlay on transaction)       │
│                                 │
│  ┌───────────────────────────┐  │
│  │  🚗 Transport Budget      │  │
│  │  You went ₹80 over budget │  │
│  │                           │  │
│  │  No stress! Here's how to │  │
│  │  stay on track next week: │  │
│  │                           │  │
│  │  💡 Try taking the metro  │  │
│  │  2x this week to save     │  │
│  │  ₹300+                    │  │
│  │                           │  │
│  │  [Adjust Budget] [OK 💪]  │  │
│  └───────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

**Design Principles:**
- Never use negative language ("failed", "bad", "overspent" ❌)
- Always provide actionable suggestion
- Forward-looking tone ("here's how to stay on track" ✅)
- Quick dismiss option (don't force interaction)

---

## 6. Weekly Money Mood Digest

### Screen: Instagram-Style Story Cards

```
Card 1/6: Money Mood
┌─────────────────────────────────┐
│                                 │
│        Your Money Mood          │
│          This Week              │
│                                 │
│            😊                   │
│           GOOD                  │
│                                 │
│     You spent ₹4,200           │
│     That's 8% less than        │
│     last week! Nice! 🎉        │
│                                 │
│         [Tap to continue →]     │
│                                 │
│  ● ○ ○ ○ ○ ○                   │
└─────────────────────────────────┘

Card 2/6: Top Categories
┌─────────────────────────────────┐
│                                 │
│     Where Your ₹ Went          │
│                                 │
│  🍔 Food        ₹1,580  (38%) │
│  ████████████████░░░░░░         │
│                                 │
│  🛍️ Shopping    ₹1,020  (24%)  │
│  ██████████░░░░░░░░░░░░         │
│                                 │
│  🚗 Transport   ₹680    (16%) │
│  ███████░░░░░░░░░░░░░░░         │
│                                 │
│  Fun fact: Swiggy was your      │
│  #1 merchant this week! 🍕      │
│                                 │
│  ○ ● ○ ○ ○ ○                   │
└─────────────────────────────────┘

Card 3/6: Budget Status
┌─────────────────────────────────┐
│                                 │
│     Budget Health Check 🏥      │
│                                 │
│  🟢 Food       On track (65%) │
│  🟢 Shopping   Under (48%)     │
│  🟡 Transport  Watch it (82%)  │
│  🟢 Bills      On track (55%) │
│                                 │
│     Overall: Looking good! 💪   │
│     Keep it up for 3 more days  │
│     to earn your weekly badge!  │
│                                 │
│  ○ ○ ● ○ ○ ○                   │
└─────────────────────────────────┘

Card 4/6: Streak & Badges
┌─────────────────────────────────┐
│                                 │
│     Your Progress 🏆            │
│                                 │
│     🔥 5-Day Streak!           │
│                                 │
│     ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐      │
│     │✓│ │✓│ │✓│ │✓│ │✓│ □ □   │
│     └─┘ └─┘ └─┘ └─┘ └─┘      │
│     M   T   W   T   F   S  S   │
│                                 │
│     🏅 NEW BADGE UNLOCKED!     │
│     "Hot Streak" — 5 days       │
│     staying in budget!          │
│                                 │
│  ○ ○ ○ ● ○ ○                   │
└─────────────────────────────────┘

Card 5/6: Weekly Tip
┌─────────────────────────────────┐
│                                 │
│     💡 Smart Tip                │
│                                 │
│     You spent ₹1,580 on food   │
│     delivery this week.         │
│                                 │
│     🍳 Cooking just 2 meals    │
│     at home this week could     │
│     save you ₹600+!            │
│                                 │
│     That's ₹2,400/month or     │
│     ₹28,800/year! 🤯           │
│                                 │
│     [I'll try this! ✅]         │
│                                 │
│  ○ ○ ○ ○ ● ○                   │
└─────────────────────────────────┘

Card 6/6: Share Card
┌─────────────────────────────────┐
│                                 │
│     ┌───────────────────────┐   │
│     │  My Money Mood  🍕    │   │
│     │                       │   │
│     │       😊 GOOD         │   │
│     │  🔥 5-day streak      │   │
│     │  🏅 2 badges earned   │   │
│     │                       │   │
│     │  #sliceSavers         │   │
│     │  @slice               │   │
│     └───────────────────────┘   │
│                                 │
│  [Share to Instagram 📸]        │
│  [Share to WhatsApp 💬]         │
│  [Save Image 💾]               │
│                                 │
│  ○ ○ ○ ○ ○ ●                   │
└─────────────────────────────────┘
```

**Design Notes:**
- Story format: swipe left/right between cards
- Auto-advance timer (5 sec per card) with tap to pause
- Vibrant colors, large text, emoji-rich
- Share card excludes actual amounts — only mood + streak + badges
- Delivered as push notification Monday 9 AM: "Your Money Mood is ready! 📊"

---

## 7. Social Challenges

### Screen: Challenge Creation

```
┌─────────────────────────────────┐
│  ← Start a Challenge  🏆       │
├─────────────────────────────────┤
│                                 │
│  Choose Challenge Type:         │
│                                 │
│  ┌───────────────────────────┐  │
│  │ 🚫 No Food Delivery Week │  │
│  │ ₹0 on food delivery ×7d  │  │
│  └───────────────────────────┘  │
│  ┌───────────────────────────┐  │
│  │ 💰 Savings Race           │  │
│  │ Who saves more this month │  │
│  └───────────────────────────┘  │
│  ┌───────────────────────────┐  │
│  │ 👯 Budget Buddies         │  │
│  │ Both stay in budget × 14d│  │
│  └───────────────────────────┘  │
│  ┌───────────────────────────┐  │
│  │ ✏️ Custom Challenge       │  │
│  │ Set your own rules        │  │
│  └───────────────────────────┘  │
│                                 │
│  Duration:                      │
│  [3 days] [7 days] [14 days]    │
│                  [30 days]      │
│                                 │
│  Invite Friends:                │
│  ┌───────────────────────────┐  │
│  │ 🔍 Search slice contacts  │  │
│  ├───────────────────────────┤  │
│  │ ☐ Priya S.    On slice   │  │
│  │ ☐ Rohan M.    On slice   │  │
│  │ ☐ Ananya D.   On slice   │  │
│  │ ☐ Arjun K.    Invite →   │  │
│  └───────────────────────────┘  │
│                                 │
│  ┌─────────────────────────┐    │
│  │  Start Challenge! 🚀    │    │
│  └─────────────────────────┘    │
│                                 │
└─────────────────────────────────┘
```

### Screen: Challenge Leaderboard

```
┌─────────────────────────────────┐
│  ← 🏆 Savings Race             │
│  Day 5 of 7                     │
├─────────────────────────────────┤
│                                 │
│  ┌───────────────────────────┐  │
│  │  🥇 You          ₹2,100  │  │
│  │  ████████████████████     │  │
│  │                           │  │
│  │  🥈 Priya S.     ₹1,800  │  │
│  │  █████████████████░░░     │  │
│  │                           │  │
│  │  🥉 Rohan M.     ₹1,200  │  │
│  │  ████████████░░░░░░░░     │  │
│  └───────────────────────────┘  │
│                                 │
│  Status: You're in the lead!    │
│  2 days left — keep going! 🔥   │
│                                 │
│  ─── Activity Feed ───          │
│                                 │
│  📣 Priya just saved ₹300      │
│     on transport! Getting close │
│                                 │
│  📣 Rohan set a new food        │
│     budget — game on! 🎮       │
│                                 │
│  [Send Encouragement 💬]        │
│                                 │
│  Privacy: Only savings amounts  │
│  are shared. No transaction     │
│  details visible to others. 🔒 │
│                                 │
├─────────────────────────────────┤
│  🏠    💳    📊    👤    ⋯   │
└─────────────────────────────────┘
```

**Privacy Notes:**
- ⚠️ Only aggregate category totals are shared in challenges
- ⚠️ Individual transaction details are NEVER visible to other participants
- ⚠️ Users must explicitly opt-in to each challenge
- ⚠️ "Leave Challenge" option always available

---

## 8. User Flow Summary

```
                    ┌──────────┐
                    │  Home    │
                    │  Screen  │
                    └────┬─────┘
                         │
              ┌──────────▼──────────┐
              │  Smart Budgets Tab  │
              │  (Entry Point)     │
              └──────────┬──────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
    │Spending │    │ Budget  │    │ Social  │
    │Dashboard│    │ Setting │    │Features │
    └────┬────┘    └────┬────┘    └────┬────┘
         │              │              │
    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
    │Category │    │  Nudge  │    │Challenge│
    │Drilldown│    │ Alerts  │    │ Create  │
    └────┬────┘    └─────────┘    └────┬────┘
         │                             │
    ┌────▼────┐                   ┌────▼────┐
    │Re-categ │                   │  Leader │
    │  orize  │                   │  board  │
    └─────────┘                   └─────────┘

         ┌───────────────┐
         │ Weekly Digest  │
         │ (Push Monday)  │
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │ Story Cards    │
         │ (6 swipeable)  │
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │ Share to Social │
         └────────────────┘
```

---

*These wireframes are low-fidelity intentionally — they define information architecture and user flows, not visual design. The design team would create high-fidelity mockups based on slice's design system.*

[Back to Project README](../README.md)
