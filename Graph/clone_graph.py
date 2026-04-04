# Problem Name: Clone Graph
# Pattern Used: Depth-First Search (DFS)
# Time Complexity: O(V + E) where V is the number of vertices (nodes) and E is the number of edges in the graph
# Space Complexity: O(V) for the visited dictionary and the recursion stack in the worst case
# Short Explanation: The function clones a graph using depth-first search (DFS). 
#                    It uses a dictionary to keep track of visited nodes and their corresponding clones.
#                    The DFS function checks if the current node has already been cloned (visited).
#                    If it has, it returns the cloned node from the visited dictionary.
#                    If it hasn't, it creates a new clone of the current node, adds it to the visited dictionary,
#                    and then recursively clones all of its neighbors, adding the cloned neighbors to the clone's neighbors list.
# LeetCode: https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from xml.dom.minidom import Node
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(original_node):
            if original_node in visited:
                return visited[original_node]

            clone = Node(original_node.val)
            visited[original_node] = clone

            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))   

            return clone

        return dfs(node) 
        