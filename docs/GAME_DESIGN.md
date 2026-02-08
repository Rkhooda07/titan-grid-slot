# Game Design Document (GDD)
## Payline Slot – 5x3, 20 Fixed Paylines

---

## 1. Design Goals

- Create a **classic-feel slot** with modern UX
- Keep rules easy to understand
- Encourage frequent engagement through small wins
- Build a solid foundation for feature expansion

---

## 2. Core Game Specs

### Grid
| Property | Value |
|-------|------|
| Reels | 5 |
| Rows | 3 |
| Layout | Static |
| Direction | Left → Right |

---

## 3. Paylines

- Total Paylines: **20**
- Type: Fixed, always active
- Player cannot enable/disable paylines
- Patterns include:
  - Horizontal lines
  - Zig-zag / V / inverted V shapes
- One winning combination per payline

---

## 4. Symbol System

### Symbol Breakdown

| Type | Count |
|----|-----|
| Regular Symbols | 6–7 |
| Wild | 1 |
| Scatter | 1 |
| Bonus (Future) | 1 (optional) |

---

### Wild Symbol Rules

- Substitutes for all regular symbols
- Cannot substitute for Scatter or Bonus
- Appears only on Reels 2–5
- No multipliers applied

---

### Scatter Symbol Rules

- Pays anywhere on the grid
- Ignores paylines
- Counted globally per spin
- Triggers Free Spins feature (future implementation)

---

## 5. Win Rules

### Line Wins

- Matching symbols must:
  - Start from Reel 1
  - Be consecutive
  - Follow an active payline
- Win lengths:
  - 3 of a kind
  - 4 of a kind
  - 5 of a kind
- Only the **highest-paying combination per payline** is awarded

---

### Scatter Wins

- Paid independently of paylines
- Evaluated after line wins
- Does not block line wins

---

## 6. Betting Model

- Player places **one total bet**
- Bet is divided equally across 20 paylines
- No line bet customization
- Simple bet ladder recommended (e.g. 0.20 → 100.00)

---

## 7. RTP & Volatility

### Target Metrics

- RTP Target: ~96% (adjustable)
- Volatility: Medium

### Feel Profile

- Frequent small line wins (3-symbol hits)
- Regular 4-symbol wins
- Occasional strong 5-symbol payouts
- Scatters provide anticipation without overuse

---

## 8. RNG & Weighting (High-Level)

- Each reel uses weighted symbol distribution
- Higher-value symbols have lower weights
- Wild appearance limited via reel restriction
- Scatter appearance tuned to control feature frequency

---

## 9. Future Features (Not in Scope)

- Free Spins with modifiers
- Bonus Game
- Wild Multipliers
- Expanding or Sticky Reels
- Cascading or Hold & Spin modes

---

## 10. Non-Goals

- No payline selection
- No cluster pays
- No Megaways / dynamic reels
- No multi-directional wins

---

## 11. Success Criteria

- Clear win visibility
- Predictable behavior
- Easy math validation
- Extendable codebase

---

End of Document
