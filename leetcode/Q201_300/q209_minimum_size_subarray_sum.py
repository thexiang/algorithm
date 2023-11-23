# LeetCodeUrl: https://leetcode.com/problems/minimum-size-subarray-sum/
# Question Name: 209. Minimum Size Subarray Sum
# Time Complexity: O(N)
# Space Complexity: O(N)
# Tag: Sliding Window


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0

        left = 0
        total = 0
        min_len = 2**32 - 1

        for right in range(len(nums)):
            total += nums[right]

            while total >= target and left <= right:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
            
        return min_len

