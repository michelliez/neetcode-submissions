class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val_i in enumerate(nums):
            for j in range(i+1, len(nums)):
                want = target - val_i
                if nums[j] == want:
                    return [i, j]