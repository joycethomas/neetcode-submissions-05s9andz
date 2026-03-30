class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        for letter in list(s):
            if letter not in s1:
                s1[letter] = 1
            else:
                s1[letter] += 1
        
        for letter in list(t):
            if letter not in s2:
                s2[letter] = 1
            else:
                s2[letter] += 1

        if s1 == s2:
            return True
        else:
            return False
        