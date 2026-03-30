class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs: 
            result += str(len(s)) + "#" + s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        '''j = i
            while s[j] != "#":
                end = int(s[i:i + j])
                j += 1
            end = int(s[i]) #fucking up because it's only taking the first digit of 10 (like it's only taking 1)
            i += it
            add = s[i:i + end]
            #print("thing", s[i:i + end])
            #print("add", add)
            i += end
            print("i", s[i])
            print(s, i, i + end)
            print(add)
            result.append(add)
        print("fuck this", i)'''
        #return result
        result = []
        i = 0
        #end = int(s[0])
        #print(s[i:end + 2])
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result
            