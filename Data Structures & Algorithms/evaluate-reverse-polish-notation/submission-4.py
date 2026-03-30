class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        currsum = 0
        ops = ["+", "-", "*", "/"]
        store = []

        for elem in tokens:
            if elem in ops:
                num2 = int(store.pop())
                num1 = int(store.pop())
                if elem == "+":
                    currsum = num1 + num2
                if elem == "-":
                    currsum = num1 - num2
                if elem == "*":
                    currsum = num1 * num2
                if elem == "/":
                    currsum = int(num1 / num2)
                store.append(currsum)
            else:
                store.append(elem)
        return int(store[0])