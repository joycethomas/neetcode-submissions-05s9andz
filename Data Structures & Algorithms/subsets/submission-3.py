class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        curr = []

        def helper(i, subset, currset, num):
            if i >= len(num):
                subset.append(currset.copy())
                return 

            currset.append(num[i])
            helper(i + 1, subset, currset, num)
            currset.pop()

            helper(i + 1, subset, currset, num)
        
        helper(0, subs, curr, nums)
        return subs
            
        