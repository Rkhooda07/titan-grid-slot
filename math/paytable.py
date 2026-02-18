# PAYTABLE (Line Bet Multipliers)

# Regular symbols
PAYTABLE = {

    # ----- LOW SYMBOLS -----
    "L1": {3: 0.2,  4: 1,   5: 4},
    "L2": {3: 0.25, 4: 1.2, 5: 5},
    "L3": {3: 0.3,  4: 1.5, 5: 6},
    "L4": {3: 0.4,  4: 2,   5: 8},

    # ----- MEDIUM SYMBOLS -----
    "M1": {3: 0.6, 4: 4,   5: 12},
    "M2": {3: 0.8, 4: 6,   5: 18},
    "M3": {3: 1.0, 4: 8,   5: 25},

    # ----- HIGH SYMBOLS -----
    "H1": {3: 1.5, 4: 10,  5: 40},
    "H2": {3: 2.0, 4: 15,  5: 60},

    # ----- WILD -----
    "W":  {3: 2.0, 4: 20,  5: 100}
}

# SCATTER PAYTABLE (Bonus - Total Bet)

SCATTER_PAYTABLE = {
    3: 2,    # 2x total bet
    4: 10,   # 10x total bet
    5: 50    # 50x total bet
}