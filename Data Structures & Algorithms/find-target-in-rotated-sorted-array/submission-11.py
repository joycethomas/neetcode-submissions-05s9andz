class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # 4 5 6 7 0 1 2, target = 0
        while l <= r: 
            m = (l + r)//2
            if nums[m] == target:
                return m
            #left sorted portion
            if nums[l] <= nums[m]:
                if nums[m] < target:
                    l = m + 1
                elif target < nums[l]: #less than the middle but also less than the left value
                    l = m + 1
                else: 
                    r = m - 1
            #right sorted portion
            else: 
                if target < nums[m]: 
                    r = m - 1
                elif target > nums[r]: #target is greater than middle and greater than right most value
                    r = m - 1
                else:
                    l = m + 1  
        return -1
        

