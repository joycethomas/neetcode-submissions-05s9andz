class Solution: 
    def isPalindrome(self, s: str) -> bool:
        '''if s == " " or s == ".":
            return True'''
        temp = ""
        for x in s: 
            if x.isalnum() == True:
                temp += x.lower()

        i = 0
        j = len(temp) - 1
        if temp == "": 
            return True
        while i < j:
            #print(s[i], s[j])
            if temp[i] == temp[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

        #FIRST ATTEMPT------------------------------------------------
        '''s = s.lower()
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
        
        return True'''