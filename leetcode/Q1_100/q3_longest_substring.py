# LeetCodeUrl: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Question Name: 3. Longest Substring Without Repeating Characters
# Time Complexity: O(n)
# Space Complexity: O(n)
# Tag: Sliding Window


class Solution:
    """
    Given a string s, find the length of the longest 
    substring without repeating characters.


    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    def lengthOfLongestSubstring(self, st: str) -> int:

        left = 0
        longest_len = 0
        current_chars = set()

        for right in range(len(st)):
            # This while loop remove characters from the left end of the substring until duplicates are no longer present
            while st[right] in current_chars:
                current_chars.remove(st[left])
                left += 1
            current_chars.add(st[right])
            longest_len = max(longest_len, right-left+1)
        return longest_len
