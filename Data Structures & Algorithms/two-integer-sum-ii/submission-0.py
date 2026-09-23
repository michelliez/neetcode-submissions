class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            search = target - numbers[left]
            if search < numbers[right]:
                right -= 1
            elif search > numbers[right]:
                left += 1
            else:
                return [left+1, right+1]



        