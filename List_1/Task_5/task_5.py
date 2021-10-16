import prefix as pr
import os
import sys


if __name__ == '__main__':
    test = [["Cyprian", "cyberotoman", "cynik", "ceniąc", "czule"]]
    test.append(["University", "of", "Wroclaw",
                "Instintue", "of", "Computer", "Science"])
    test.append(["Doom", "Duck", "Zeta", "Do", "Done"])
    test.append(["a", "b", "c", "d", "e"])
    test.append(["Toy", "Stories"])
    test.append(["red", "rose", "horse", "morse",
                "roar", "chew", "rear", "rock"])

    with open(os.path.join(sys.path[0], "words.txt"), "r") as words:
        test.append(list(map(str.strip, words.readlines())))

    for case in test:
        print(case)
        print(f"Common prefix '{pr.Prefix.common_prefix(case)}'")

    length = 5
    print(f"\nCommon prefix with {length} words")
    for case in test:
        print(case)
        print(f"Common prefix '{pr.Prefix.common_prefix(case, length)}'")

    length = 10
    print(f"\nCommon prefix with {length} words")
    for case in test:
        print(case)
        print(f"Common prefix '{pr.Prefix.common_prefix(case, length)}'")
