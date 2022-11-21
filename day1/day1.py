def Increses(measurments):
    frist = measurments[0]
    count = 0
    for i in measurments[1:]:
        if i > frist:
            count+=1
        frist = i
    return count

def main():
    with open("measurments.txt","r") as f:
        medidas = f.readlines()
        measurments = []
        for lines in medidas:
            measurments.append(int(lines.strip()))
        print(Increses(measurments))

main()