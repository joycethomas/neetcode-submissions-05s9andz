class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        alpha, d1, d2 = "abcdefghijklmnopqrstuvwxyz", {}, {}
        for x in alpha: 
            d1[x] = 0
            d2[x] = 0

        for x in s1:
            d1[x] += 1
        for i in range(0, len(s1)):
            d2[s2[i]] += 1

        matches = 0
        for x in alpha:
            if d1.get(x) == d2.get(x):
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            d2[s2[r]] += 1
            if d1.get(s2[r]) == d2.get(s2[r]):
                matches += 1
            elif d1.get(s2[r]) + 1 == d2.get(s2[r]):
                matches -= 1
            
            d2[s2[l]] -= 1
            if d1.get(s2[l]) == d2.get(s2[l]):
                matches += 1
            elif d1.get(s2[l]) - 1 == d2.get(s2[l]):
                matches -= 1
            l += 1
        return matches == 26
            
    