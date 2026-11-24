class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        previous_value = 0
        for char in reversed(s):
            current_value = roman_to_num[char]
            if current_value < previous_value:
                total -= current_value
            else:
                total += current_value
            previous_value = current_value

        return total
