# Problem Name: Integer to Roman
# Pattern Used: Hash Map
# Time Complexity: O(1)
# Space Complexity: O(1)
# Short Explanation: The function converts an integer to its corresponding Roman numeral representation using a hash map for value-symbol mapping.
# LeetCode Link: https://leetcode.com/problems/integer-to-roman/

# Without 9s and 4s in the dictionary, we can use the following approach to convert an integer to a Roman numeral.
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            "1": "I",
            "5": "V",
            "10": "X",
            "50": "L",
            "100": "C",
            "500": "D",
            "1000": "M"
        }

        num = str(num)
        result = ""

        num_zero = len(num) - 1

        for i in num:
            # For 9 or 4
            if i == "9" or i == "4":
                i = i + ("0" * num_zero)
                adder = str(int(i) + int("1" + ("0" * num_zero)))
                result += roman["1" + ("0" * num_zero)] + roman[adder]
                num_zero -= 1

            # For numbers greater than 5 (6,7,8)
            elif int(i) > 5:
                remaining = int(i) - 5
                roman_ones = roman["1" + ("0" * num_zero)] * remaining
                roman_fives =  roman["5"  + ("0" * num_zero)]
                result += roman_fives + roman_ones
                num_zero -= 1
                
            # For 5
            elif int(i) == 5:
                roman_fives =  roman["5"  + ("0" * num_zero)]
                result += roman_fives
                num_zero -= 1

            # For less than 4 (1,2,3)
            elif int(i) < 4:
                roman_ones = roman["1" + ("0" * num_zero)] * int(i)
                result +=  roman_ones
                num_zero -= 1

        return result


# Solution with 9s and 4s in the dictionary, we can use the following approach to convert an integer to a Roman numeral.
class Solution:

  def intToRoman(self, num: int) -> str:
    # Value to symbol mapping in descending order
    val_to_roman = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    res = []
    for value, symbol in val_to_roman:
      if num == 0:
        break
      count = num // value
      res.append(symbol * count)
      num %= value

    return ''.join(res)
        