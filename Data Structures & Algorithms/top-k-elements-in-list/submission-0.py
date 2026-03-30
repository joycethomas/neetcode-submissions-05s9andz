class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        results = []
        for x in nums: 
            if x not in dic: 
                dic[x] = 1
            else: 
                dic[x] += 1
        print(dic)
        slist = list(sorted(dic.items(), key=lambda item: item[1], reverse = True))
        #print(slist)
        for i in range(k):
            results.append(slist[i][0])
        return results
        