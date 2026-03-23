class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        left = 0
        max_profict = 0

        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
                continue

            max_profict = max(prices[right] - prices[left], max_profict)

        return max_profict
