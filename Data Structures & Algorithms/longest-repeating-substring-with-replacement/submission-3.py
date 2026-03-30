class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0
        result = 0
        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            #making sure that window is valid, this while is fixing it until it's value
            while (r - l + 1) - max(dic.values()) > k: #window - max freq <= k
                dic[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        
        return result

        
        #window size = (r - l + 1)
        #max(count.values())
        #count.get(s[r], 0)
