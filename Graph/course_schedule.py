#Problem Name: Course Schedule
#Pattern Used: Depth-First Search (DFS)
#Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
#Space Complexity: O(V) for the visited list and the recursion stack in the worst case
#Short Explanation: The function determines if it's possible to finish all courses given the prerequisites.
#                   It uses an adjacency list to represent the graph of courses and their prerequisites.
#                   The DFS function checks for cycles in the graph. If it encounters a node that is currently being visited 
#                   (visited[node] == 1), it means there is a cycle, and it returns False.
#                   If it encounters a node that has already been fully processed (visited[node] == 2), 
#                   it means the node and all its descendants are safe to process.
#                   If it successfully processes all neighbors without finding a cycle, 
#                   it marks the node as fully processed (visited[node] = 2).
#LeetCode: https://leetcode.com/problems/course-schedule/

from ast import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = [0] * numCourses
        
        def dfs(node):
            if visited[node] == 1:
                return False  
            if visited[node] == 2:
                return True
            
            visited[node] = 1
            
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visited[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True