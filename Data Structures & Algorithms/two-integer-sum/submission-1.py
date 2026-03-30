class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = []
        dic = {}
        for x in range(len(nums)): 
            if nums[x] in dic.values():
                results.append(nums.index(target - nums[x]))
                results.append(x)
                break
            else:
                dic[nums[x]] = target - nums[x]
        return results