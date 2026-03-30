class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        dic, dic2 = {}, {}
        for x in t:
            dic[x] = 1 + dic.get(x, 0)

        have, need = 0, len(dic) # for need, we're gonna keep track if the requirements for each letter has been met
        result, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r] 
            dic2[c] = 1 + dic2.get(c, 0)

            if c in dic and dic2[c] == dic[c]: #we just satisfied a condition
                have += 1
            
            while have == need: #while this condition is met, we want to reduce the window with the l index
                if (r - l + 1) < resLen: 
                    result = [l, r]
                    resLen = r - l + 1
                #getting rid of the left
                dic2[s[l]] -= 1
                if s[l] in dic and dic2[s[l]] < dic[s[l]]: #if we messed up the requirements
                    have -= 1
                l += 1

        l, r = result
        return s[l:r + 1] if resLen != float("infinity") else ""



        '''dic2, result, matches, r, target = {}, s + " ", 0, 0, len(t)
        for l in range(len(s)):
            # in the beginning, maybe not necessary but can decide later
            if result == "" and matches == 0:
                r = l
                continue
            while l < len(s) and s[l] not in dic:
                l+= 1
            if s[l] in dic:
                dic2[s[l]] = 1 + dic2.get(s[l], 0)
                #only update matches if there's NOT a surplus
                if dic2.get(s[l]) <= dic.get(s[l]):
                    matches += 1
            while matches < target: 
                if s[r] in dic: 
                    dic2[s[r]] = 1 + dic2.get(s[r], 0)
                if dic2.get(s[r]) <= dic.get(s[r]):
                    matches += 1
                r += 1
                if matches == target:
                    if (r - l) < len(result):
                        result = s[l:r]
                    break
            if dic2[s[l]] <= dic[s[l]]:
                match -= 1
            if s[l] in dic2:
                dic2[s[l]] -= 1
        if result == " ":
            return "" '''
            
        