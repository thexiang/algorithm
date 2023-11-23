# LeetCodeUrl: https://leetcode.com/problems/gas-station/
# Question Name: 134. Gas Station
# Time Complexity: O(n)
# Space Complexity: O(n)
# Tag: Greedy


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if not gas or not cost:
            return -1

        # Feasibility Check: If the total amount of gas is less than the total cost required to travel, 
        # it’s impossible to complete the circuit.
        if sum(cost) > sum(gas):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            # If at any point, total becomes negative, it means you cannot reach the next station from the current starting point.
            if total < 0:
                total = 0
                start = i + 1

        return start