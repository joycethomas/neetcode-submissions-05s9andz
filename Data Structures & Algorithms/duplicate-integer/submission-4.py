class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for x in nums:
            if x in result:
                return True
            result.add(x)
        return False
        