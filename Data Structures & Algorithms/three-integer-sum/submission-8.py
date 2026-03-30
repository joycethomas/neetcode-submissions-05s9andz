class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            mid = first + 1
            last = len(nums) - 1
            while mid < last:
                adds = nums[first] + nums[mid] + nums[last]
                if adds < 0:
                    if nums[mid] == nums[mid + 1]:
                        mid += 1
                    mid += 1
                if adds > 0:
                    if nums[last] == nums[last - 1]:
                        last -= 1
                    last -= 1
                if adds == 0:
                    toadd = [nums[first], nums[mid], nums[last]]
                    toadd.sort()
                    print(toadd)
                    if toadd not in results:
                        results.append(toadd)
                    mid += 1
        
        return results
