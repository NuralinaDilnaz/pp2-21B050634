def spy_game(nums):
    answer = False
    for i in range(len(nums)-2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            answer = True
    return answer
nums = list(map(int, input().split()))
print(spy_game(nums))