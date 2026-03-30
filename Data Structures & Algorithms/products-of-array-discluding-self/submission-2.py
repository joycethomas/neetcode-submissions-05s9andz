class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        prod = 1
        zeroes = nums.count(0)
        if zeroes >= 2:
            return [0] * len(nums)
        
        for x in nums: 
            if x != 0: 
                prod *= x
            else: 
                prod *= 1
        
        flag = nums.count(0) == 1
        if flag:
            for x in nums: 
                if x != 0:
                    results.append(0)
                else: 
                    results.append(prod)
            return results

        for x in nums:
            results.append(int(prod/x))
            
        return results