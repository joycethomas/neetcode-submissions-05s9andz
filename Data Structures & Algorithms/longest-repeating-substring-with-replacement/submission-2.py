class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #TRY THIS SHIT AGAIN BRO 
        l = 0
        result = 0
        dic = {}
        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            if (r - l + 1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
                
        
        # X Y Y X
        # L R
























        '''if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l = 0
        r = 1
        count = 0
        result = 0
        temp1 = k
        for r in range(len(s)):
            #print(l, r, s[l:r + 1], "\n")
            if s[l] == s[r]:
                print("loop 1", l, r, s[l:r + 1], "\n")
                count += 1
                r += 1
                result = max(result, count)
            elif k > 0 and s[l] != s[r]:
                #s[l] and s[r] aren't the same
                print("loop 2", l, r, s[l:r + 1], "\n")
                k -= 1
                r += 1
                count += 1
                result = max(result, count)
            else: 
                #k is 0 and s[l] and s[r] aren't the same
                print("loop 3", l, r, s[l:r + 1], "\n")
                l = r
                r = l + 1
                k = temp1
                count = 1
            

        return result'''