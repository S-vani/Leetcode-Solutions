class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        copy = strs[:]
        anagrams = []
        while len(copy) > 0:
            fixed_str = copy.pop(0)
            anagram = [fixed_str]
            to_be_removed = []
            for string in copy:
                str_list = list(fixed_str)

                if len(fixed_str) != len(string):
                    continue
                for i in string:
                    if i in str_list:
                        str_list.remove(i)
                if len(str_list) == 0:
                    anagram.append(string)
                    to_be_removed.append(string)
            for s in to_be_removed:
                copy.remove(s)
            anagrams.append(anagram) 
        
        return anagrams

                    
