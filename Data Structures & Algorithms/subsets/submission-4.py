class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currset, subs = [], []

        def helper(curr, result, i, num):
            if len(num) <= i:
                result.append(curr.copy())
                return
            
            curr.append(nums[i])
            helper(curr, result, i + 1, nums)
            curr.pop()

            helper(curr, result, i + 1, nums)
            

        
        helper(currset, subs, 0, nums)
        return subs

        
        