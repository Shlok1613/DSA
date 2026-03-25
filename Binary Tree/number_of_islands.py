# Problem Name: Number of Islands
# Pattern Used: Breadth First Search (BFS)
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use BFS to traverse the grid and find the number of islands. 
#                    We maintain a queue of nodes to visit. In each iteration, 
#                    we process all nodes at the current level and add their children to the queue. 
#                    The number of levels we process is the maximum depth of the tree.
# LeetCode Link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    queue = deque([(i,j)])
                    while queue:
                         x, y = queue.popleft()
                         if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                            grid[x][y] = "0"
                            for dx, dy in directions:
                                queue.append((x+dx, y+dy))
        
        return num_islands
