numbers = []
guesses = []
counter = 0
with open("input4.txt", "r") as f:
    numbers = f.readlines()
    guesses = numbers[0].split(",")
    numbers.pop(0)
    numbers.pop(0)
    for i in range(len(numbers)): #quebra as linhas da matriz 
        numbers[i] = numbers[i].split(" ")
        numbers[i] = list(filter(lambda a : a != "",numbers[i]))
    
    for e in guesses:
        for j in range(len(numbers)):
            if numbers[j] == ['*','*','*','*','*']:break
            if numbers[j] == "\n":continue 
            for k in range(len(numbers[j])):
                for e in guesses:
                    if numbers[j][k] == e:
                        numbers[j][k] = '*'  
    print(numbers)

