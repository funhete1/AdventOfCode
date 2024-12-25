import sys

class Day2():
    def part1(self, data):
        safe = 0
        with open(data, 'r') as file:
            for report in file:
                levels = [*map(int, report.split())]  
                if self.is_safe(levels):
                    safe += 1
            return safe

    def part2(self, data):
        safe = 0
        with open(data, 'r') as file:
            for report in file:
                levels = [*map(int, report.split())]
                if self.is_safe(levels):
                    safe += 1
                else:
                    for i in range(len(levels)):
                        tolerated_levels = levels[:i] + levels[i + 1 :]  #check every combination without each element without the first, second, third ...
                        if self.is_safe(tolerated_levels):
                            safe += 1
                            break
            return safe

    def is_safe(self, levels):
        differs = [a - b for a, b in zip(levels, levels[1:])]
        is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)     #instead of verifying if is ascendent or descendent check if the diference is > or < then 0  
        is_in_range = all(0 < abs(i) <= 3 for i in differs)
        if is_monotonic and is_in_range:
            return True
        return False
    
if __name__=='__main__':
    solution = Day2()
    print(f"Safe Reports: {solution.part1(sys.argv[1])}")
    print(f"Tolared Reports: {solution.part2(sys.argv[1])}")