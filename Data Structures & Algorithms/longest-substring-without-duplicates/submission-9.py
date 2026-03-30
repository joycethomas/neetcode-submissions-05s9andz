class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        result = 0
        dupes = set()
        for r in range(len(s)):
            while s[r] in dupes: 
                dupes.remove(s[l])
                l += 1
            result = max(result, r - l + 1)
            dupes.add(s[r])
            r += 1
        
        return result

























        '''if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        if len(s) == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1
        l = 0
        r = 1
        result = 0
        dups = set()
        dups.add(s[l])
        while r < len(s):
            print(l, r, s[l:r])
            print(dups)
            if s[r] not in dups:
                dups.add(s[r])
                r += 1
                print("loop 1")
            else:
                #result = max(result, r - l - 1)
                #print(s[l:r])
                result = max(result, r - l)
                dups.clear()
                l = r
                r += 1
                dups.add(s[l])
                print("loop 2")
            print()

        print("out of loop")
        print(dups)
        print("length", len(dups))
        if s[-1] not in dups: 
            dups.add(s[-1])
            result = max(result, len(dups))
            print(s[l:])'''
            
        '''if r == len(s) - 1 and s[r] not in dups:
            result = max(result, r - l)'''


        #len = 8
        # a b c a b c b b"
        # l r               set = a, b; result = 1
        # l   r             set = a, b, c; result = 2
        
        #return result
        