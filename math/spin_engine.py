import random
from reels import REELS
from config import NUM_ROWS

# SPIN ENGINE

def spin():
  # Generate 5x3 grid spin result

  grid = []

  for reel in REELS:
    reel_length = len(reel)

    stop_index = random.randint(0, reel_length - 1)

    visible_symbole = [
      reel[(stop_index + i) % reel_length]
      for i in range(NUM_ROWS)
    ]

    grid.append(visible_symbole)

  return grid


def print_grid(grid):
  print("Spin results : ")

  for row in range(NUM_ROWS):
    row_symbols = [grid[reel][row] for reel in range(len(grid))]

    print(row_symbols)
