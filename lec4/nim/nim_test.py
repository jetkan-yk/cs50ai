"""
Acceptance tests for nim.py

Make sure that this file is in the same directory as nim.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from nim import train, Nim

# Let the AI play against itself for 10 times. If the q function
# is implemented correctly, the AI which moved second should always win.

ai = train(10000)


def test():
    print("Playing AI vs AI...")
    winrate = 0
    for _ in range(10000):
        winrate += play_ai_vs_ai()
    print(f"Win rate: {winrate // 100}.{winrate % 100}%")


# helper function


def play_ai_vs_ai():
    game = Nim()
    while True:
        game.move(ai.choose_action(game.piles))

        if game.winner is not None:
            return game.winner
