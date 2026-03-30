class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs: 
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        
        
        
        
        
        '''def count(s):
            alpha = {}
            for x in "abcdefghijklmnopqrstuvwxyz":
                alpha[x] = 0
            for c in s:
                if c in alpha:
                    alpha[c] += 1
            results = {}
            for x in alpha: 
                if alpha[x] != 0:
                    results[x] = alpha[x]
            return results

        final = {}
        for x in strs:
            res = count(x).items()
            if res not in final:
                final[res] = [x]
            else:
                final[res].append
        return final.values()'''
        




        '''al = {}
        alpha = {}
        for x in "abcdefghijklmnopqrstuvwxyz":
            al[x] = 0
        for x in strs:
            for c in x:
                if c in alpha:
                    al[c] += 1
            alpha[x] = al
            
        print(alpha)
        after = {}
        for x in alpha:
            if alpha[x] not in after:
                after[alpha[x]] = [x]
            else:
                after[alpha[x]].append(x)
        return after.values()'''
        
        