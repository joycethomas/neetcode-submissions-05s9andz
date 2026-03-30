class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        fin = []
        for n in range(len(arr)):
            if n != len(arr)-1:
                fin.append(max(arr[n+1:]))
            if n == len(arr)-1:
                fin.append(-1)
        return fin