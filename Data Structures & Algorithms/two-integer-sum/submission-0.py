class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            desired = target - num
            if desired in seen:
                return [seen[desired], i]
            seen[num] = i 