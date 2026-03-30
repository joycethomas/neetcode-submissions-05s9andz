class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combo = []
        stack = []
        for i in range(len(position)): 
            combo.append((position[i], speed[i]))
        
        pairs = sorted(combo, key=lambda x:x[0], reverse=True)
        print(pairs)
        for x in pairs: 
            dest = (target - x[0])/x[1]
            if stack and dest > stack[-1]:
                stack.append(dest)
            if not stack:
                stack.append(dest)

        
        return len(stack)



        