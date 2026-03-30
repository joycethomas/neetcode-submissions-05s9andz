class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for x in nums: 
            if x not in dic: 
                dic[x] = 1
            else: 
                return True
        return False
         