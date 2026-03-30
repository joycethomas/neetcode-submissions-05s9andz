class Solution:
    #DO THIS AGAIN BUT WITH TWO POINTERS, NOT IN O(N^2) TIME
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j: 
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]











        #FIRST ATTEMPT ---------------------------------------------------
        '''for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [numbers.index(numbers[i]) + 1, numbers.index(numbers[j]) + 1]
                if numbers[i] + numbers[j] > target:
                    break'''

        