class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for x in nums: 
            if x not in dups:
                dups.add(x)
            else:
                return True
        return False
         