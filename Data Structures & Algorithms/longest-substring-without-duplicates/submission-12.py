class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        vis = set()
        #vis.add(s[l])
        #vis.add(s[r])

        result = 0

        while r < len(s):
            #print(vis)
            #if s[r] not in vis:
            while s[r] in vis and l < r:
                vis.remove(s[l])
                l += 1
            vis.add(s[r])
            result = max(result, r - l + 1)
            r += 1

        return result

