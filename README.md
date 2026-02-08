# 🎰 Slot Machine Game – PAYLINE Slot

A modern, classic-style **payline-based slot game** built with a fixed grid and always-active paylines.  
Designed for **medium volatility**, frequent small wins, and clear, readable gameplay.

This project focuses on simplicity, clarity, and extensibility for future features like free spins and bonus rounds.

---

## 🎰 Game Overview

- **Grid:** 5 Reels × 3 Rows
- **Paylines:** 20 fixed paylines (always active)
- **Pay Direction:** Left → Right only
- **Win Condition:** 3 / 4 / 5 matching symbols
- **Match Requirement:** Must start from Reel 1
- **Volatility:** Medium
- **Target Feel:** Frequent small hits, occasional strong wins

---

## 🧩 Core Features

### Grid
- Static 5×3 layout
- No expanding reels or modifiers (for now)

### Paylines
- 20 predefined paylines
- Always enabled (no player selection)
- Includes:
  - Straight horizontal lines
  - Zig-zag patterns
- One win per payline (highest-paying symbol wins)

### Symbols
- **10–12 total symbols**
  - 6–7 Regular symbols
  - 1 Wild
  - 1 Scatter
  - (Optional) 1 Bonus symbol for future features

### Wild Symbol
- Substitutes for all regular symbols
- Appears on **Reels 2–5 only**
- No multipliers or special effects (yet)

### Scatter Symbol
- Pays anywhere on the grid
- Does **not** use paylines
- Triggers free spins (feature to be added later)

---

## 💰 Betting System

- Single **total bet**
- Internally divided across 20 paylines
- No per-line betting or line selection
- Clean and beginner-friendly UX

---

## 🎯 Win Evaluation Rules

- Only leftmost-aligned wins count
- Winning symbols must start from Reel 1
- Evaluated per payline independently
- Highest possible win per payline is awarded

---

## 🚀 Planned Extensions

- Free Spins Feature (Scatter-based)
- Bonus Symbol & Bonus Game
- Wild Multipliers
- Expanding or Sticky Wilds
- Volatility tuning via symbol weights

---

## 📂 Project Structure (initial)

slot-machine/
│
├── src/
│ ├── engine/
│ │ ├── reels/
│ │ ├── symbols/
│ │ ├── paytable/
│ │ └── win-calculator/
│ │
│ ├── config/
│ │ ├── reelStrips.json
│ │ ├── symbols.json
│ │ └── gameConfig.json
│ │
│ ├── utils/
│ └── index.ts
│
├── tests/
│
├── docs/
│ └── GDD.md
│
├── README.md
└── .gitignore

---

## 🛠️ Tech Stack

> Adjust this section if needed

- Language: **TypeScript / JavaScript**
- Architecture: Modular slot engine
- RNG: Deterministic reel-strip based RNG
- Target Platforms:
  - Web
  - Mobile
  - Casino backend integration ready

---
