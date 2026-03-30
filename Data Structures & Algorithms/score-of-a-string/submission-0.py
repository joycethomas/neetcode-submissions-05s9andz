class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        slist = list(s)
        for i in range(len(slist)-1):
            letter1 = ord(slist[i])
            letter2 = ord(slist[i+1])
            total += abs(letter1-letter2)
        return total

Solution().scoreOfString("code")