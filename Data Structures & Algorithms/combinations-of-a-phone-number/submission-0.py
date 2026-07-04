class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        #keypad = {2 : {'a', 'b', 'c'}, 3 : {'d', 'e', 'f'}, 4 : {'g', 'h', 'i'}, 5 : {'j', 'k', 'l'}, 6 : {'m', 'n', 'o'}, 7 : {'p', 'q', 'r', 's'}, 8 : {'t', 'u', 'v'}, 9 : {'w', 'x', 'y', 'z'},}
        keypad = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'], 5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'], 7 : ['p', 'q', 'r', 's'], 8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z'],}
        combo, curr, digs = [], [], []
        for x in digits:
            digs.append(int(x))
        #print(digs)

        def helper(i):
            if i == len(digs):
                combo.append(''.join(curr.copy()))
                return
            if i > len(digs):
                return

            for x in keypad[digs[i]]:
                curr.append(x)
                helper(i + 1)
                curr.pop()

        helper(0)
        return combo