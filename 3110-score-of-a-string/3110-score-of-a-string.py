class Solution:
    def scoreOfString(self, s: str) -> int:
        total_amount = 0
        for letter in range(len(s)-1):
            difference = ord(s[letter]) - ord(s[letter + 1])
            total_amount += abs(difference)
        
        return total_amount

        