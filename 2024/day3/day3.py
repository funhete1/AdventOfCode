import sys
import re

class day3:
    def part1(input):
        multiplications = []
        result = 0
        with open(input, 'r') as corrupted:
                pattern = r'mul\(\d{1,3},\d{1,3}\)'
                multiplications = re.findall(pattern,corrupted.read()) 
        for operaiton in multiplications:
            numbers = re.findall(r'\d{1,3},\d{1,3}', operaiton)[0].split(',')
            result += int(numbers[0]) * int(numbers[1])
        return result
    def part2(input):
        with open(input, 'r') as corrupted:
            pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
            instructions = re.findall(pattern, "".join(corrupted))

        do_flag = True
        result = 0

        for inst in instructions:
            match inst:
                case "do()":
                    do_flag = True
                case "don't()":
                    do_flag = False
                case _ if do_flag:
                    numbers = re.findall(r'\d{1,3},\d{1,3}',inst)[0].split(',')
                    result += int(numbers[0]) * int(numbers[1])
        return result
if __name__=="__main__":
    print(f"Multiplications Results: {day3.part1(sys.argv[1])}")
    print(f"Multiplications Enabled: {day3.part2(sys.argv[1])}")