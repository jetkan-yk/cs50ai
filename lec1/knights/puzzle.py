from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


def Xor(P, Q):
    return And(Or(P, Q), Not(And(P, Q)))


# Add character
# Can only be either a knight or knave, but not both
def char(knight, knave):
    return Xor(knight, knave)


# Add statement
# Either it is a knight and the statement is true,
# or it is a knave and the statement is false
def says(knight, knave, s):
    return Or(And(knight, s), And(knave, Not(s)))


# Puzzle 0
# A says "I am both a knight and a knave."
ASays = And(AKnight, AKnave)

knowledge0 = And(
    # Add characters
    char(AKnight, AKnave),
    # Add statements
    says(AKnight, AKnave, ASays),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
ASays = And(AKnave, BKnave)

knowledge1 = And(
    # Add characters
    char(AKnight, AKnave),
    char(BKnight, BKnave),
    # Add statements
    says(AKnight, AKnave, ASays),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
ASays = Or(And(AKnight, BKnight), And(AKnave, BKnave))

BSays = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    # Add characters
    char(AKnight, AKnave),
    char(BKnight, BKnave),
    # Add statements
    says(AKnight, AKnave, ASays),
    says(BKnight, BKnave, BSays),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
