from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
A = (AKnight, AKnave)

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
B = (BKnight, BKnave)

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")
C = (CKnight, CKnave)


def Xor(P, Q):
    return And(Or(P, Q), Not(And(P, Q)))


# Add character P
# P can only be either a knight or knave, but not both
def add_char(P):
    (knight, knave) = P
    return Xor(knight, knave)


# Character P makes statement S
# Either P is a knight and the statement S is true,
# or P is a knave and the statement S is false
def make_stmt(P, S):
    (knight, knave) = P
    return Or(And(knight, S), And(knave, Not(S)))


# Puzzle 0
# A says "I am both a knight and a knave."
ASays = And(AKnight, AKnave)

knowledge0 = And(
    # Add characters
    add_char(A),
    # Make statements
    make_stmt(A, ASays),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
ASays = And(AKnave, BKnave)

knowledge1 = And(
    # Add characters
    add_char(A),
    add_char(B),
    # Add statements
    make_stmt(A, ASays),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
ASays = Or(And(AKnight, BKnight), And(AKnave, BKnave))
BSays = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    # Add characters
    add_char(A),
    add_char(B),
    # Add statements
    make_stmt(A, ASays),
    make_stmt(B, BSays),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
ASays = Xor(AKnight, AKnave)
BSays1 = make_stmt(A, AKnave)
BSays2 = CKnave
CSays = AKnight

knowledge3 = And(
    # Add characters
    add_char(A),
    add_char(B),
    add_char(C),
    # Add statements
    make_stmt(A, ASays),
    make_stmt(B, BSays1),
    make_stmt(B, BSays2),
    make_stmt(C, CSays),
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
