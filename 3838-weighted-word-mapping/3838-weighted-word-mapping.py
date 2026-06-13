class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        final = ""
        for word in words:
            total = 0
            for letter in word:
                int_value = ord(letter) - 97
                total += weights[int_value]
            let = chr(122 - (total % 26))
            final = final + let
        return final