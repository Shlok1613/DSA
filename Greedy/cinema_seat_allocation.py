# Problem Name: Cinema Seat Allocation
# Pattern Used: Greedy
# Time Complexity: O(n)
# Space Complexity: O(n)
# Short Explanation: The problem is solved by first calculating the maximum number of families 
#                    that can be seated in the cinema without any reserved seats. Then, for each row with reserved seats,  
#                    we check how many families can be seated based on the reserved seats and adjust the total accordingly.
# LeetCode: https://leetcode.com/problems/cinema-seat-allocation/description/

from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        answer = 2 * n

        rows = {}

        for row, seat in reservedSeats:
            rows.setdefault(row, set()).add(seat)

        for seats in rows.values():
            families = 0

            left = all(seat not in seats for seat in [2, 3, 4, 5])

            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left:
                families += 1

            if right:
                families += 1

            if families == 0:
                middle = all(seat not in seats for seat in [4, 5, 6, 7])

                if middle:
                    families = 1

            answer -= 2
            answer += families

        return answer
        