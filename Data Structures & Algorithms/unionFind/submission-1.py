class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.numcomps = n

        for x in range(n):
            self.par[x] = x
            self.rank[x] = 0

        

    def find(self, x: int) -> int:
        p = self.par[x]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]] #getting the root of whatever p is
            p = self.par[p] #setting p to the root
        return p
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y): return False
        p1, p2 = self.find(x), self.find(y)

        if self.rank[p1] > self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] < self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        self.numcomps -= 1

        return True


        

    def getNumComponents(self) -> int:
        return self.numcomps

