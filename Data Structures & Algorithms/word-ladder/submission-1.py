class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {}
        wordList.append(beginWord)
        for x in wordList:
            adj[x] = set()
        
        
        def oneapart(x, y):
            count = len(x)

            for i in range(len(x)):
                if x[i] == y[i]:
                    count -= 1
            if count == 1: return True
            return False
        
        endflag = False
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                endflag = True
            for j in range(len(wordList)):
                if i == j:
                    continue
                x, y = wordList[i], wordList[j]
                if y in adj[x]: #switched the letters here
                    continue
                if oneapart(x, y):
                    adj[x].add(y)
                    adj[y].add(x)
        
        if not endflag: return 0
        
        def bfs(node, target, adjL):
            length = 1
            visit = set()
            q = collections.deque()
            visit.add(node)
            q.append(node)
        
            while q: 
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr == target:
                        return length
                    for nei in adjL[curr]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
                length += 1
            return 0
        
        return bfs(beginWord, endWord, adj)


