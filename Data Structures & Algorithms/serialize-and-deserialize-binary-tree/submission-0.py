# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return 'N'
        
        left = self. serialize(root.left)
        right = self.serialize(root.right)

        result = str(root.val) + "," + str(left) + "," +  str(right)
        return result

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.i = 0

        def dfs():
            if nodes[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(nodes[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()



        '''if data is None:
            return TreeNode(None, None, None)
        nodes = data.split(',')
        print("run", nodes)
        for x in nodes:
            if x != 'N':
                x = int(x)
        if len(nodes) == 3 and nodes[-2] == "N" and nodes[-1] == "N":
            return TreeNode(nodes[0], None, None)
        elif len(nodes) == 3 and (nodes[-2] == "N" or nodes[-1] == "N"):
            temp = TreeNode(nodes[0], None, None)
            if nodes[-2] == "N":
                temp.right = nodes[-1]
            else:
                temp.left = nodes[-2]
            return temp

        left = self.deserialize(data[1:])
        right = self.deserialize(data[1:])

        return TreeNode(data[0], left, right)'''
        
        
