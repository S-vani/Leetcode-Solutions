class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for letter in range(len(s)-1):
            difference = ord(s[letter]) - ord(s[letter + 1])
            total += abs(difference)
        
        return total

        