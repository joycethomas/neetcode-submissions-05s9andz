class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        result = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                result = min(nums[l], result)
                break
            mid = (l + r) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        return result


        # 3 4 5 6 1 2 
        # L   M     R
        #     L M   R
        #       L M R

        # 1 2 3 4 5 6
        # L     M   R
        # L   M R
        # L M R

        # 3 4 5 6 7 1 2
        # L     M     R
        #       L   M R
        #           L R        






















        '''
        result = nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid = (l + r)//2
            result = min(result, nums[mid])
            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return result'''


        '''if len(nums) == 1:
            return mid[0]
        mid = (int)(len(nums)/2)
        first = nums[:mid]
        second = nums[mid:]
        while len(first) > 2: 
            fmid = (int)(len(first)/2)
            if first[fmid - 1] < first[fmid]:
                first = first[:fmid]
            elif first[fmid + 1] < first[fmid]: 
                first = first[fmid:]
        print(first)
        while len(second) > 2: 
            smid = (int)(len(second)/2)
            if second[smid - 1] < second[smid]:
                second = second[:smid]
            elif second[smid + 1] < second[smid]: 
                second = second[smid:]
        print(second)

        if len(first) > 2:
            flow = min(first[0], first[1])
        else:
            flow = first[0]

        if len(second) > 2:
            slow = min(second[0], second[1])
        else:
            slow = second[0]
        return min(flow, slow) '''          

