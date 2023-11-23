from leetcode.leetcode_101_200.q134_gas_station import Solution

def test_example1():
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

def test_example2():
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1

def test_empty_lists():
    assert Solution().canCompleteCircuit([], []) == -1

def test_single_station():
    assert Solution().canCompleteCircuit([5], [4]) == 0

def test_infeasible_circuit():
    assert Solution().canCompleteCircuit([1, 2, 3], [4, 5, 1]) == -1

def test_feasible_circuit():
    assert Solution().canCompleteCircuit([3, 1, 2], [2, 2, 2]) == 0