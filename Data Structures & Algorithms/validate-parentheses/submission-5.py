class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "]": "[","}":"{"}
        for x in s:
            if x in dic.keys(): 
                if stack and stack[-1] == dic.get(x):
                    stack.pop()
                else:
                    return False
            if x not in dic.keys():
                stack.append(x)

        return not stack