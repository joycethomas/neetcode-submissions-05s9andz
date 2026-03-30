class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        while first < last:
            while not self.alphaNum(s[first]) and first < last:
                first += 1
            while not self.alphaNum(s[last]) and first < last:
                last -= 1
            print("first", s[first], "last", s[last])
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))