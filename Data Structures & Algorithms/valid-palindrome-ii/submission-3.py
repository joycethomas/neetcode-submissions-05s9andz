class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        l = 0
        r = len(s) - 1
        while l <= r:
            print(count, s[l],s[r])
            if s[l] != s[r]:
                #if og string is baaa
                #sleft = aaa
                #sright = baa
                sleft = s[l + 1: r + 1]
                sright = s[l:r]
                return (sleft == sleft[::-1] or sright == sright[::-1])
            l += 1
            r -= 1
        return True
        
        