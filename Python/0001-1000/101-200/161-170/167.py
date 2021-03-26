class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        for index in range(n+1):
            new_target = target - numbers[index]
            left, right = index + 1, n
            while left <= right:
                middle = (left + right) // 2
                if numbers[middle] < new_target:
                    left = middle + 1
                elif numbers[middle] > new_target:
                    right = middle - 1
                else:
                    return [index + 1, middle + 1]
