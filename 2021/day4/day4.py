import numpy as  np
from pyparsing import CaselessKeyword


numbers = {}
guesses = []
counter = 0

with open("input4.txt", "r") as f:
    guesses  = list(f.readline())
    f.readline()
    lines = []
    for i in f:
        if i =="\n": continue
        lines.append(i.split(","))
        if len(lines) % 5 == 0:
            numbers[len(lines)//5 - 1] = (np.array(lines[len(lines)-5:len(lines)])   )

for i in numbers.keys():
    for j in range(len(numbers[i])):
        x = np.fromstring(numbers[i][j][0], dtype=int, sep=' ')
        arr = []       
        for k in range(len(x)):
            arr.append(x[k])
        print(numbers[i][j])
        numbers[i][j] = arr

