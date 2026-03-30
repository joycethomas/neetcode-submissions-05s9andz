class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #mid = len(nums)/2
        f = 0
        s = len(nums) - 1
        while f <= s:
            #mid = int(len(nums)/2) apparently leads to overflow
            mid = f + ((s - f) // 2)
            if nums[mid] > target:
                s = mid - 1
            elif nums[mid] < target:
                f = mid + 1
            else:
                return mid
        return -1

