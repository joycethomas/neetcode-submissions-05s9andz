class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = set(nums)
        for i in range(len(nums)):
            look = target - nums[i]
            if look in numset:
                result = nums.index(look)
                if result != i: 
                    if i < result: 
                        return [i, result]
                    else:
                        return [result, i]
            


        