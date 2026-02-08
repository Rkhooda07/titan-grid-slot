# 🎰 Slot Machine Game – WAYS Slot

A custom-built **WAYS slot machine game**, designed from scratch with a clear **Game Design Document (GDD)** approach.  
This project focuses on clean reel logic, symbol weighting, configurable reel strips, and a scalable architecture suitable for real-money or social casino games.

---

## 🚀 Project Overview

This slot game is built as a **WAYS slot** (no fixed paylines). Wins are calculated based on matching symbols from **left to right** across adjacent reels, using dynamic reel configurations.

Key goals of this project:
- Modular & scalable slot engine
- Configurable reels, rows, and symbol weights
- Clear separation between game logic and UI
- Easy future expansion (features, bonus rounds, free spins, etc.)

---

## 🎯 Slot Configuration (Phase 1)

### 🔹 Reels & Rows
- **Reels:** 5
- **Rows:** 3
- Symbols are evaluated reel-by-reel from left to right.

### 🔹 WAYS System
- All possible symbol combinations across adjacent reels are counted as **WAYS**.
- No fixed paylines.
- More matching symbols on consecutive reels = more WAYS.

### 🔹 Symbols
- Regular symbols
- Premium symbols
- Wild symbol (substitutes for others)
- Scatter (reserved for future bonus features)

### 🔹 Symbol Weights
- Each symbol has a defined probability via **reel strips**
- Higher-value symbols appear less frequently
- Lower-value symbols appear more often

---

## 🧠 Core Game Logic

- Reel strips control randomness (not RNG-per-spin symbol picks)
- Spin result is derived from stopping positions on each reel
- Win evaluation:
  - Starts from Reel 1
  - Stops when a reel breaks the matching chain
- Payout =  
  `symbol payout × number of matching reels × number of WAYS`

---

## 📂 Project Structure (Suggested)

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

## 📈 Roadmap

### Phase 1 – Core Slot
- ✅ Reels & rows
- ✅ WAYS evaluation
- ✅ Symbol weights & reel strips
- ✅ Base game payouts

### Phase 2 – Features
- ⏳ Wild multipliers
- ⏳ Free spins
- ⏳ Scatter bonus
- ⏳ RTP tuning

### Phase 3 – Polish
- ⏳ Animations & sound
- ⏳ UI/UX integration
- ⏳ Performance optimization
