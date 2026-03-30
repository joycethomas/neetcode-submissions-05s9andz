class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{", ")":"(", "]":"["}
        result = []
        for x in s: 
            if x in pairs: 
                if result and result[-1] == pairs[x]:
                    result.pop()
                else:
                    return False
            else:
                result.append(x)
            

        return True if not result else False
        