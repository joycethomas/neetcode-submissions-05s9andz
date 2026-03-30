class Solution: #DO IT AGAIN BUT WITH TWO POINTERS
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        new = ""
        for x in s: 
            if x in alpha:
                new += x
        counter = 0
        for x in reversed(new):
            print(x)
            if x != new[counter]:
                return False
            counter += 1
        
        return True