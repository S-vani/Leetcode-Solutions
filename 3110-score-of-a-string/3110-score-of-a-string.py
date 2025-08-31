class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        string_list = list(s)
        for letter in range(len(s)-1):
            difference = ord(string_list[letter]) - ord(string_list[letter + 1])
            total += abs(difference)
        
        return total

        