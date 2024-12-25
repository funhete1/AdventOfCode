import sys
import re
class Day1():
    def part1(file):
        distance = 0
        left = []
        right = []
        with open(f"{file}", 'r') as f:
            for line in f:
                l,r = map(lambda x : int(x),line.strip().split())
                left.append(l)
                right.append(r)
                
            f.close()
        while(left != []):
            min_left = left.pop(left.index(min(left)))
            min_right = right.pop(right.index(min(right)))
            distance += abs(min_left - min_right)
        return distance

    def part2(file):
        left = []
        right = []
        simliraty = 0
        with open(f"{file}", 'r') as f:
            for line in f:
                l,r = map(lambda x : int(x),line.strip().split())
                left.append(l)
                right.append(r)
            f.close()
        for number in left:
            equals = len(list(filter(lambda x: x == number, right)))
            simliraty += equals * number
        return simliraty    

if __name__ == '__main__':
    print(f"distance: {Day1.part1(sys.argv[1])}")
    print(f"similiraty: {Day1.part2(sys.argv[1])}")