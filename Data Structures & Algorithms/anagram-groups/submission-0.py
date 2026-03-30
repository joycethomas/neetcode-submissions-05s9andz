class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        results = []
        #adding a k:v pair with the actual word and then the sorted 
        for x in strs:
            alpha = ''.join(sorted(x))
            if alpha in dic:
                dic[alpha].append(x)
            else:
                dic[alpha] = [x]

        for x in dic.values():
            results.append(x)
            
        return results



