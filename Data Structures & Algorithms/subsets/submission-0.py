class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results, self.subsets = [],[]

        def helper(i, nums):
            if i >= len(nums):
                self.results.append(self.subsets.copy())
                return self.results
            
            #include the subset
            self.subsets.append(nums[i])
            helper(i + 1, nums)
            self.subsets.pop()

            #don't include the subset
            helper(i + 1, nums)

        helper(0, nums)
        return self.results
        