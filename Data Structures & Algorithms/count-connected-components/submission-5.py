class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.par = {}
        self.rank = {}
        self.num = n

        for x in range(n):
            self.par[x] = x
            self.rank[x] = 0

        def find(x):
            p = self.par[x]

            while self.par[p] != p:
                self.par[p] = self.par[self.par[p]]
                p = self.par[p] #might be wrong but idr
            
            return p
        
        def sameparent(x, y):
            return find(x) == find(y)
        
        def union(x, y):
            if sameparent(x, y): return True

            p1, p2 = find(x), find(y)
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
                self.rank[p2] -= 1
            elif self.rank[p2] > self.rank[p1]:
                self.par[p1] = p2
                self.rank[p1] -= 1
            else:
                self.par[p1] = p2
                self.rank[p1] -= 1
            self.num -= 1
        
        for x, y in edges:
            union(x, y)
        
        return self.num

        