def twoSum(nums,target):
    d = {}
    for i in range(0, len(nums)):
        if target - nums[i] in d:
            return [d[target - nums[i]], i]
            
        d[nums[i]] = i
        
nums=[1,4,6,7,8]
print(twoSum(nums,12))
