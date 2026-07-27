class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_str = ""
        for letter in s:
            if letter.isalnum():
                converted_str += letter.lower()
        i = 0
        j = len(converted_str) - 1
        while i < j:
            if converted_str[i] != converted_str[j]:
                return False
            i += 1
            j -= 1
        return True