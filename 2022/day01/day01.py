def main():
    with open("input.txt") as f:
        nums = ""
        for lines in f:
            nums += lines
        nums = nums.split("\n\n")
        
        for i in range(len(nums)):
            j =  nums[i].split('\n')
            nums[i] = sum(map(int,j))  # type: ignore 
        nums.sort(reverse=True)
    print(sum(nums[0:3]))  # type: ignore
if __name__=="__main__":
    main()

    