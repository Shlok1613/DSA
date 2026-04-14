# Problem Name: Rotting Oranges
# Pattern Used: Breadth First Search (BFS)
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use BFS to traverse the grid and find the minimum time required to rot all the oranges. 
#                    We maintain a queue of rotten oranges and in each iteration, 
#                    we process all the rotten oranges at the current level and add their adjacent fresh oranges to the queue. 
#                    The number of levels we process is the minimum time required to rot all the oranges.
# LeetCode Link: https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min = 0
        good = 0
        rotten = deque()

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    good += 1

        while rotten and good > 0:

            min += 1

            for _ in range(len(rotten)):
                x,y = rotten.popleft()

                for dx, dy in dir:
                    new_x, new_y = x+dx, y+dy

                    if new_x < 0 or new_x == rows or new_y < 0 or new_y == cols or grid[new_x][new_y] == 0 or grid[new_x][new_y] == 2:
                        continue

                    good -= 1

                    grid[new_x][new_y] = 2

                    rotten.append((new_x, new_y))

        if good == 0:
            return min
        else:
            return -1