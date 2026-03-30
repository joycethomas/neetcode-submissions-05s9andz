class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        while first < last:
            add = numbers[first] + numbers[last]
            if add == target:
                return [first + 1, last + 1]
            if add > target:
                last -= 1
            else:
                first += 1
        