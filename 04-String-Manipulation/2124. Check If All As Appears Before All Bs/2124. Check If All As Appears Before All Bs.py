class Solution:
    def checkString(self, s: str) -> bool:
        for index in range(len(s) - 1):
            if s[index] > s[index + 1]:
                return False
        return True
