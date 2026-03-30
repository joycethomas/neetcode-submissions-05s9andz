class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L, R = 0, len(numbers)-1

        while L < R:
            compliment = target - numbers[R]
            if compliment < numbers[L]:
                R -= 1
            if compliment > numbers[L]:
                L += 1
            if compliment == numbers[L]:
                return [L+1, R+1]