class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []
      
        def isPali(x):
            l = 0
            r = len(x) - 1
            while l <= r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def helper(i):
            if i == len(s):
                res.append(curr.copy())
                return
            if i > len(s):
                return 
            
            for j in range(i, len(s)):
                if isPali(s[i:j + 1]):
                    curr.append(s[i:j + 1])
                    helper(j + 1)
                    curr.pop()
        
        helper(0)
        return res