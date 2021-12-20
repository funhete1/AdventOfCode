numbers = []
guesses = []
counter = 0
with open("input4.txt", "r") as f:
    numbers = f.readlines()
    guesses = numbers[0].split(",")
    numbers.pop(0)
    numbers.pop(0)
    for i in range(len(numbers)): #vai matriz a matriz
        if i%5==0:counter+=1
        for j in range(5): #linha da matriz
            for e in guesses:
                if numbers[i][j] ==  e:
                    numbers[i][j] = '0'
        if numbers[i] == ['0','0','0','0','0']:break
    print(numbers)
        