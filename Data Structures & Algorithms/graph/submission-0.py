class Graph:
    
    def __init__(self):
        self.adj_list = {}


    def addEdge(self, src: int, dst: int) -> None:
        if dst not in self.adj_list:
            self.adj_list[dst] = set() #[] made it as list first
        if src not in self.adj_list:
            self.adj_list[src] = set() #[] made it as list first
        self.adj_list[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list:
            return False
        if dst not in self.adj_list[src]: #didn't have this one either
            return False
        #self.adj_list.get(src).remove(dst) changed it to set now which changes the syntax
        self.adj_list[src].remove(dst) 
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        def dfs(s, d, visited):
            #if s in visited:
                #return False
            #^^ puts this in the recursive call for returning True purposes
            if s == d:
                return True
            visited.add(s)
            for n in self.adj_list.get(s):
                if dfs(n, d, visited):
                    return True
            return False

        
        return dfs(src, dst, visited)