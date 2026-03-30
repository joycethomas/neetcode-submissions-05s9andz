class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x == "*":
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif x == "+":
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif x == "-":
                a, b = stack.pop(), stack.pop()
                result = b - a
                stack.append(result)
            elif x == "/":
                a, b = stack.pop(), stack.pop()
                result = int(b/a)
                stack.append(result)
            else:
                stack.append(int(x))
        
        return stack[0]
                    