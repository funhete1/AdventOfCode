import re
import sys
class Day5:
    def __init__(self,puzzle_input):
        self.rules = []
        self.updates = []
        with open(puzzle_input, 'r') as file:
                for lines in file:
                    line = lines.strip()
                    pattern = "^[0-9][0-9]\\|[0-9][0-9]$"
                    self.rules.append(line) if re.match(pattern=pattern,string=line) else self.updates.append(line.split(','))
        self.updates = self.updates[1:]

    def rule_exist(self,n1,n2,change=False):
            pattern = [f"{n1}|{n3}" for n3 in n2] 
            if not change:
                return all(p in self.rules for p in pattern)
            else:
                for p in pattern:
                    if not p in self.rules:
                        return False,p
                    else:
                        return True,None
    
    def part1(self):     
        sum_middle = 0
        for update in self.updates:
            flag = True
            for idx in range(len(update)-1):
                if not self.rule_exist(update[idx],update[idx+1:]):
                    flag = False
                    break
            if flag:
                sum_middle += int(update[len(update)//2])
        return sum_middle

    def part2(self):
        def make_correct(update):
            for idx in range(len(update)-1):
                exist, swap = self.rule_exist(update[idx],update[idx+1:],change=True) 
                if not exist:
                    hold = update[idx]
                    update[update.index(swap.split('|')[1])] = hold
                    update[idx] = swap.split('|')[1]
                    return make_correct(update)
            return update
                        
                        
        sum_middle = 0
        for update in self.updates:
            for idx in range(len(update)-1):
                if not self.rule_exist(update[idx],update[idx+1:]):
                    corrected = make_correct(update)
                    sum_middle += int(corrected[len(corrected)//2])
        return sum_middle


if __name__=="__main__":
    solution = Day5(sys.argv[1])
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")