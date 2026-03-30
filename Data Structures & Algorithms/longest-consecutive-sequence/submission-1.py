class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dic = {}
        teeheeset = set()
        for x in nums: 
            if x not in dic:
                dic[x] = False
                #print("x:", x, "x-1:", x-1)
            teeheeset.add(x)
        
        for x in nums:
            if x + 1 in dic:
                dic[x + 1] = True #does it have a left neighbor

        llen = [] 
        count = 0
        curr = 0
        for x in dic:
            if dic.get(x) == False:
                curr = x
                count += 1
                while curr + 1 in teeheeset:
                    curr += 1
                    count += 1
                llen.append(count)
                curr = 0
                count = 0
        
        return max(llen)