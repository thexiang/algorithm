from leetcode.Q201_300.q209_minimum_size_subarray_sum import Solution

# Create an instance of the Solution class
solution = Solution()

# Test cases
def test_minSubArrayLen_basic():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    assert solution.minSubArrayLen(target, nums) == 2

def test_minSubArrayLen_no_subarray():
    target = 20
    nums = [1, 2, 3, 4, 5]
    assert solution.minSubArrayLen(target, nums) == 0

def test_minSubArrayLen_single_element():
    target = 4
    nums = [4]
    assert solution.minSubArrayLen(target, nums) == 1

def test_minSubArrayLen_empty_array():
    target = 1
    nums = []
    assert solution.minSubArrayLen(target, nums) == 0