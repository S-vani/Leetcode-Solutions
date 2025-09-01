class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_of_lengths = []
        if len(strs) > 1:
            for i in range(len(strs)):
                list_of_lengths.append(len(strs[i]))
        elif len(strs) == 1:
            return strs[0]
        else:
            return ""

        len_of_shortest = min(list_of_lengths)
        longest = ""
        first_word = strs[0]
        letter = 0
        while letter < len_of_shortest:
            valid = True
            for i in range(1, len(strs)):
                if first_word[letter] == strs[i][letter]:
                    continue
                else:
                    valid = False
                    break
            
            if not valid:
                break
            longest += f"{first_word[letter]}"

            letter += 1
        
        return longest
                    
            