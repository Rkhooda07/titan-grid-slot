from paylines import PAYLINES
from paytable import PAYTABLE, SCATTER_PAYTABLE
from config import LINE_BET, TOTAL_BET

# LINE EVALUATION

def evaluate_spin(grid):
  # Evaluate one full spin result

  total_win = 0

  for line in PAYLINES:
    line_symbols = []

    # Extract symbols for this payline
    for reel_index in range(len(line)):
      row_index = line[reel_index]
      line_symbols.append(grid[reel_index][row_index])

    line_win = evaluate_line(line_symbols)
    total_win += line_win

  scatter_win = evaluate_scatter(grid)
  total_win += scatter_win

  return total_win

# SINGLE LINE LOGIC

def evaluate_line(symbols):
  # Evaluates one payline 

  first_symbol = symbols[0]

  # If first symbol is Scatter, no line win
  if first_symbol == "S":
    return 0
  
  # Case 1: First symbol is not Wild
  if first_symbol != "W":
    match_symbol = first_symbol
    count = 1

    for s in symbols[1:]:
      if s == match_symbol or s == "W":
        count += 1
      else:
        break

    if count >= 3 and match_symbol in PAYTABLE:
      return PAYTABLE[match_symbol].get(count, 0) * LINE_BET
    
    return 0
  
  # Case 2: First symbol is wild
  else:
    # Testing all possible regular symbols
    best_win = 0

    for symbol in PAYTABLE.keys():
      if symbol == "w":
        continue

      count = 1

      for s in symbols[1:]:
        if s == symbol or s == "W":
          count += 1
        else:
          break

      if count >= 3:
        payout = PAYTABLE[symbol].get(count, 0) * LINE_BET
        if payout > best_win:
          best_win = payout

    # Check pure wild line
    wild_count = 1
    for s in symbols[1:]:
      if s == "W":
        wild_count += 1
      else: 
        break

    if wild_count >= 3:
      wild_payout = PAYTABLE["W"].get(wild_count, 0) * LINE_BET
      best_win = max(best_win, wild_payout)

    return best_win

# SCATTER LOGIC

def evaluate_scatter(grid):
  # Count total scatter anywhere and pay accordingly

  scatter_count = 0

  for reel in grid:
    for symbol in reel:
      if symbol == "S":
        scatter_count += 1

  if scatter_count in SCATTER_PAYTABLE:
    return SCATTER_PAYTABLE[scatter_count] * TOTAL_BET
  
  return 0