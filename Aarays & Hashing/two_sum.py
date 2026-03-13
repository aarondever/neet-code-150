class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, v in enumerate(nums):
            k = target - v
            if k in num_map:
                return [num_map[k], i]
            num_map[v] = i

        return []
