# Problem Name: Zigzag Conversion
# Pattern Used: Simulation
# Time Complexity: O(n)
# Space Complexity: O(n)
# Short Explanation: The problem is solved by simulating the zigzag pattern. We maintain a list of strings for each row and
#                    iterate through the input string, appending characters to the appropriate row based on the current
#                    direction of traversal (down or up). Finally, we concatenate all the rows to get the final result.
# LeetCode: https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s

        rows = [""] * numRows
        direction = 1
        curr_row = 0

        for i in s:
            rows[curr_row] += i

            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        return("".join(rows))