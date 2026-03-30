class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        renum = {}
        
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in renum:
                return [renum[compliment], index]
            renum[num] = index