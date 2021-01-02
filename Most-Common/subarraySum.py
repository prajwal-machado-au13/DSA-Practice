def subarraySum(nums):
    max_val=float("-inf")
    for i in range(len(nums)):
        sum_val = 0
        for j in range(i, len(nums)):
            sum_val += nums[j]

            if sum_val > max_val:
                max_val = sum_val
    return max_val

if __name__ == "__main__":
    print(subarraySum(nums=[-2,1,-3,4,-1,2,1,-5,4]))
