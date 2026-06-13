class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        final = ""
        for word in words:
            total = 0
            for letter in word:
                total += weights[ord(letter) - 97]
            let = chr(122 - (total % 26))
            final = final + let
        return final