numbers = []
guesses = []
i=0
with open("input4.txt", "r") as f:
    numbers = f.readlines()
    guesses = numbers[0].split(",")
    print(numbers[2])
    print(numbers[3])
    numbers.pop(0)
    numbers.pop(0)
    for i in range(0,len(numbers),5): #vai matriz a matriz
        for j in range(5): #linha da matriz