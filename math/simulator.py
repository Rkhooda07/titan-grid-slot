from spin_engine import spin
from evaluator import evaluate_spin
from config import TOTAL_BET

#SIMULATION ENGINE

def simulate(num_spins):
  total_bet = 0
  total_win = 0
  hit_count = 0
  max_win = 0

  for i in range(num_spins):
    total_bet += TOTAL_BET

    grid = spin()

    win = evaluate_spin(grid)

    total_win += win

    if win > 0:
      hit_count += 1

    if win > max_win:
      max_win = win


  rtp = total_win / total_bet if total_bet > 0 else 0
  hit_frequency = hit_count / num_spins if num_spins > 0 else 0

  return {
    "spins": num_spins,
    "total_bet": total_bet,
    "total_win": total_win,
    "rtp": rtp,
    "hit_frequency": hit_frequency,
    "max_win": max_win
  }
