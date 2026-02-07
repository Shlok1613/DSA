#Problem Name: Letter Combinations of a Phone Number
#Pattern Used: Backtracking
#Time Complexity: O(3^m * 4^n) where m is the number of digits that maps to 3 letters and n is the number of digits that maps 
#                 to 4 letters
#Space Complexity: O(3^m * 4^n) for the output list
#Short Explanation: We use backtracking to generate all possible combinations of letters for the given digits by mapping 
#                   each digit to its corresponding letters and recursively building the combinations.
#LeetCode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from ast import List


class Solution:
    def letterCombinations(self, digits: str) ->    List[str]:
        if not digits:
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        } 

        def backtracking(combination, next_digit):
            if len(next_digit) == 0:
                output.append(combination)
            else:
                for letter in letters[next_digit[0]]:
                    backtracking(combination + letter, next_digit[1:])
            
        output = []
        backtracking("", digits)
        return output