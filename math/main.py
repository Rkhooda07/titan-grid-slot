from simulator import simulate
from config import DEFAULT_SPINS

if __name__ == "__main__":
  results = simulate(DEFAULT_SPINS)

  print("------SIMULATION RESULTS------")
  print(f"Spins: {results['spins']}")
  print(f"Total Bet: {results['total_bet']}")
  print(f"Total Win: {results['total_win']:.2f}")
  print(f"RTP: {results['rtp'] * 100:.2f}%")
  print(f"Hit Frequency: {results['hit_frequency'] * 100:.2f}%")
  print(f"Max Win Observed: {results['max_win']}")
  print("--------------------------------")