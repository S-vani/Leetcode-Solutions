class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        while i + 1 <= len(s):
            if i == len(s) - 1:
                total += romans[s[i]]
                break
            elif romans[s[i]] >= romans[s[i + 1]]:
                total += romans[s[i]]
                i += 1
            elif romans[s[i]] < romans[s[i + 1 ]]:
                total += (romans[s[i + 1]] - romans[s[i]])
                i += 2
        
        return total
            
        