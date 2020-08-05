from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
aSays = And(AKnight, AKnave)
knowledge0 = And(
    Biconditional(Not(aSays), AKnave),
    Biconditional(aSays, AKnight)
    )
knowledge0.add(Not(aSays))


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
aSays = And(AKnave, BKnave)
knowledge1 = And(
    Biconditional(Not(aSays), AKnave),
    Biconditional(aSays, AKnight)
)
knowledge1.add(Not(aSays))
knowledge1.add(Or(And(AKnight, BKnave), And(BKnight, AKnave)))


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
aSays = Or(And(AKnave,BKnave), And(AKnight, BKnight))
bSays = Or(And(AKnave, BKnight), And(AKnight, BKnave))
knowledge2 = And(
    Biconditional(Not(aSays), AKnave),
    Biconditional(aSays, AKnight),
    Biconditional(Not(bSays), BKnave),
    Biconditional(bSays, BKnight),
)
knowledge2.add(Not(And(AKnave, BKnave, aSays)))
knowledge2.add(Not(And(BKnave, AKnight, bSays)))

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
aSays = Or(AKnight, AKnave)
bSays = And(CKnave, aSays, AKnight)
cSays = AKnight
knowledge3 = And(
    Biconditional(Not(aSays), AKnave),
    Biconditional(aSays, AKnight),
    Biconditional(Not(bSays), BKnave),
    Biconditional(bSays, BKnight),
    Biconditional(Not(cSays), CKnave),
    Biconditional(cSays, CKnight)
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
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
