from leetcode.Q1_100.q3_longest_substring import Solution

# Create an instance of the Solution class
solution = Solution()

# Test cases
def test_lengthOfLongestSubstring_empty_string():
    s = ""
    assert solution.lengthOfLongestSubstring(s) == 0

def test_lengthOfLongestSubstring_no_repeating_characters():
    s = "abcde"
    assert solution.lengthOfLongestSubstring(s) == 5

def test_lengthOfLongestSubstring_repeating_characters():
    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s) == 3

def test_lengthOfLongestSubstring_mixed_characters():
    s = "pwwkew"
    assert solution.lengthOfLongestSubstring(s) == 3