# Problem Name: Minimum Number of Pushes to Type Word I
# Pattern Used: Math
# Time Complexity: O(1)
# Space Complexity: O(1)
# Short Explanation: The problem can be solved by dividing the length of the word into segments of 8 characters.
#                    Each segment requires a different number of pushes based on its position.

class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) <= 8:
            return len(word)

        elif len(word) > 8 and len(word) <= 16:
            return (8 + ((len(word) - 8) * 2))

        elif len(word) > 16 and len(word) <= 24:
            return (8 + 8*2 + (len(word) - 16) * 3 )

        elif len(word) > 24:
            
            return (8 + 8*2 + 8*3 + (len(word) - 24) * 4)