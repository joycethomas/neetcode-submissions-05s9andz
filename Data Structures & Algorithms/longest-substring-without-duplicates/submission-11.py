class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        dups = {s[0]}
        result = 0
        r = 1
        for l in range(len(s)):
            while r < len(s) and s[r] not in dups:
                dups.add(s[r])
                result = max(result, len(dups))
                r += 1
            if r < len(s) and s[r] in dups:
                dups.remove(s[l])

            '''while r < len(s) and s[r] not in dups:
                #print(s[r])
                dups.add(s[r])
                result = max(result, len(dups))
               #print(s[r], result, dups)
                r += 1
            if r < len(s):
                print(s[r], r, "out of while")
            if r < len(s) and s[r] in dups:
                dups.remove(s[r])
            if s[l] in dups:
                dups.remove(s[l])'''
            
        return result





        