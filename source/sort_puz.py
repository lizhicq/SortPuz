import argparse
import time
from game import NewGame

def main():
    parser = argparse.ArgumentParser(description="Specify the mapping file you want to solve")
    parser.add_argument("--file", default="data/74.json", help="--file data/139.json")
    args = parser.parse_args()

    start_date = time.time()
    game = NewGame(args.file)

    result = game.solve()
    end_date = time.time()

    diff = end_date - start_date
    print(f"Solution: {result.bottles}\nduration: {diff} seconds")

    for move in result.moves:
        print(move)

if __name__ == "__main__":
    main()
