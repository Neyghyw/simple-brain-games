#!/usr/bin/env python
from brain_games import engine, games


def main():
    engine.start_game_template(games.gcd_game)


if __name__ == "__main__":
    main()
