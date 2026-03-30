class Solution:
    def isPalindrome(self, s: str) -> bool:
        L,R = 0, len(s)-1

        while L < R:
            if s[L].isalnum() and s[R].isalnum():
                if s[L].lower() == s[R].lower():
                    L += 1
                    R -= 1
                else:
                    return False
            elif (s[L].isalnum()) == False:
                L += 1
            elif (s[R].isalnum()) == False:
                R -= 1
        return True
