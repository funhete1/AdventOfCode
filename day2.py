x = 0
aim = 0
depth = 0
with open( "input2.txt","r") as f:
    instructions = f.readlines()
    for lines in instructions:
        joker = lines.split(" ")
        if joker[0] == "up":
            aim-=int(joker[1])
        elif joker[0] == "down":
            aim+=int(joker[1])
        else:
            x+=int(joker[1])
            depth += aim * int(joker[1]) 
    print(x*depth)
