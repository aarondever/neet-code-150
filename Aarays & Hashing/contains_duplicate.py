class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        duplicate = set()

        for num in nums:
            if num in duplicate:
                # Duplicate found
                return True
            duplicate.add(num)

        return False
