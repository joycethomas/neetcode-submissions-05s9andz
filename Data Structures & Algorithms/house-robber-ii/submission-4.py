class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        n = len(nums)
        cache = [-1] * n #cache[i] will have max_profit that DOESN'T include last house
        cache_with_last = [-1] * n #cache_with_last[i] may include last value, won't be able to include first
        
        cache[-1], cache[-2] = 0, nums[-2]
        cache_with_last[0], cache_with_last[-1], cache_with_last[-2] = -1, nums[-1], nums[-2]

        max_prof = 0 #not including the last value
        max_prof_last = nums[-1] #this will include the last value
        i = n - 3

        while i >= 0: 
            #if i > 0:
            cache_with_last[i] = max_prof_last + nums[i]
            max_prof_last = max(max_prof_last, cache_with_last[i + 1])
                
            #if i < n - 2:
            cache[i] = max_prof + nums[i]
            max_prof = max(max_prof, cache[i + 1])
            if i == 0:
                max_prof = max(max_prof, cache[i])

            i -= 1

        print(cache, max_prof, cache_with_last, max_prof_last)
        return max(max_prof_last, max_prof)

        