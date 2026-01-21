# Problem Name: Min Stack
# Pattern Used: Stack
# Time Complexity: O(N) for getMin, O(1) for push, pop, top
# Space Complexity: O(N)
# Short Explanation: We use a stack to store the elements. 
#                    The getMin function iterates through the stack to find the minimum element.
# LeetCode: https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return []

    def getMin(self) -> int:
        minimum = self.stack[0]
        for i in range(1,len(self.stack)):
            if self.stack[i] < minimum:
                minimum = self.stack[i]
        return minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()