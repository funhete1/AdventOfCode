"""
X - pedra//////Y - Papel/////Z - Tesoura

A- Pedra/////B - Papel/////C - Tesoura

A Y        W (6+2) = 8
A X        D (3+1) = 4
A Z        L (0+3) = 3


B X        L (0+1) = 1
B Y        D (3+2) = 5
B Z        W (6+3) = 9

C Y        L (0+2) = 2
C Z        D (3+3) = 6
C X        W (6+1) = 7

"""





def main():
    with open("input.txt", 'r') as f:
        rounds = [i for i in f.read().strip().split("\n")]
    #result for part one
    """results = {
        "A Y": 8, "B Z": 9, "C X":7,
        "A X": 4, "B Y": 5, "C Z":6,
        "A Z": 3, "B X": 1, "C Y":2,
    }"""
    results = {
        "A Y": 4, "B Z": 9, "C X":2,
        "A X": 3, "B Y": 5, "C Z":7,
        "A Z": 8, "B X": 1, "C Y":6,
    }
    total = 0
    for round in rounds:
        total += results[round]
    print(total)


if __name__=="__main__":
    main()


"//make a max function ?"