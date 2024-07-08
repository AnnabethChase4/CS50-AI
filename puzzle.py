from logic import *

# Define symbols for each character's role
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A cannot be both a knight and a knave
    Biconditional(AKnight, Not(AKnave)),
    # If A is telling the truth, then A is a knave, which is a contradiction
    Biconditional(AKnight, And(AKnight, AKnave)),
    # If A is lying, then A is not a knave
    Biconditional(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A and B cannot be both knights and knaves
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    # If A is a knight, then both A and B are knaves (A is lying)
    Biconditional(AKnight, And(AKnave, BKnave)),
    # If A is a knave, then it is not true that both A and B are knaves
    Biconditional(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B cannot be both knights and knaves
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    # If A is a knight, then A and B are of the same kind
    Biconditional(AKnight, Biconditional(AKnight, BKnight)),
    # If A is a knave, then A and B are of different kinds
    Biconditional(AKnave, Not(Biconditional(AKnight, BKnight))),
    # If B is a knight, then A and B are of different kinds
    Biconditional(BKnight, Not(Biconditional(AKnight, BKnight))),
    # If B is a knave, then A and B are of the same kind
    Biconditional(BKnave, Biconditional(AKnight, BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave.'"
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A and B cannot be both knights and knaves
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
    # B's statement about A: If B is a knight, A said "I am a knave."
    Implication(BKnight, Biconditional(AKnight, AKnave)),
    # If B is a knight, C is a knave
    Biconditional(BKnight, CKnave),
    # If B is a knave, C is not a knave
    Biconditional(BKnave, Not(CKnave)),
    # C's statement about A: If C is a knight, A is a knight
    Biconditional(CKnight, AKnight),
    # If C is a knave, A is not a knight
    Biconditional(CKnave, Not(AKnight))
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()
