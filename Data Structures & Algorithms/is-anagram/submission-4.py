class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        '''dic1 = {}
        for x in s: 
            if x not in dic1:
                dic1[x] = 1
            if x in dic1: 
                dic1[x] += 1
        dic2 = {}
        for x in t:
            if x not in dic1:
                return False
            if x not in dic2:
                dic2[x] = 1
            if x in dic2: 
                dic2[x] += 1
        dic1 = {key: dic1[key] for key in sorted(dic1.keys())}
        dic2 = {key: dic2[key] for key in sorted(dic2.keys())}
        print(dic1)
        print(dic2)
        if dic1 == dic2: 
            return True
        return False'''
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        return False