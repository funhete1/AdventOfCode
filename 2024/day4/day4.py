import sys


class Day4: 
    def __init__(self,input_data):
        with open(input_data,'r') as file:
            self.lines = file.read().strip().split('\n')
        
        self.height = len(self.lines)
        self.width = len(self.lines[0])
    def part1(self):
        directions = []
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j ==0:
                    continue
                directions.append((i,j))


        def has_xmas(i,j,dd): 
            dx, dy = dd
            for k, x in enumerate('XMAS'):
                ii = i + k * dx
                jj = j + k * dy
                if not (0 <= ii < self.width and 0 <= jj < self.height):
                    return False
                if self.lines[ii][jj] != x:
                    return False
            return True
        
        count = 0
        for i in range(self.width):
            for j in range(self.height):
                for dd in directions:
                    count += has_xmas(i,j,dd)

        return count   
    
    def part2(self):
        def has_mas(i,j):
            if not (1 <= i < self.width - 1 and 1 <= j < self.height - 1):
                return False
            if self.lines[i][j] != 'A':
                return False
        
            diagonal_princ = f"{self.lines[i-1][j-1]}{self.lines[i+1][j+1]}"
            diagonal_sec = f"{self.lines[i+1][j-1]}{self.lines[i-1][j+1]}"

            return diagonal_princ in ["MS","SM"] and diagonal_sec in ["MS","SM"] 
        
        count = 0
        for i in range(self.width):
            for j in range(self.height):
                count += has_mas(i,j)
        return count 

if __name__=="__main__":
    solution = Day4(sys.argv[1])
    print(f"Part 1:{solution.part1()}")
    print(f"Part 2:{solution.part2()}")