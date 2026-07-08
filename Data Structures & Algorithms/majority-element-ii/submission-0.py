class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        vote1, vote2 = 0, 0
        cand1, cand2 = None, None
        k = len(nums)//3
        res = []
        

        for n in nums:
            #print(n, "Cand1", cand1, vote1, "Cand2", cand2, vote2)
            if n == cand1:
                vote1 += 1
            elif n == cand2:
                vote2 += 1
            elif vote1 == 0:
                cand1 = n
                vote1 = 1
            elif vote2 == 0:
                cand2 = n
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        
        count1, count2 = 0, 0
        for n in nums:
            if cand1 == n:
                count1 += 1
            if cand2 == n:
                count2 += 1

        print(count1, count2)    
        if count1 and count1 > k:
            res.append(cand1)
        if count2 > k and cand1 != cand2:
            res.append(cand2)
        return res
            