def jump_game(nums):
    n = len(nums)
    curr_end , curr_far = 0 , 0
    answer = 0

    for i in range(n-1):
        curr_far = max (curr_far , i+ nums[i])

        if i == curr_end:
            answer +=1
            curr_end = curr_far

    return answer

def main():
    nums = [2,3,1,1,9]
    print(f"{nums} , jumps : { jump_game(nums) }")

if __name__ == "__main__":
    main()