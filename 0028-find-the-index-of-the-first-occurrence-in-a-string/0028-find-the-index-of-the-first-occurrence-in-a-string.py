class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        index = 0
        needle_index = 0
        hay = 0

        if haystack == needle:
            return 0

        while hay < len(haystack):
            if needle[needle_index] == haystack[hay]:
                if len(needle) == 1:
                    return hay
                needle_index += 1
                hay += 1
                if needle_index == len(needle):
                    index = hay - len(needle)
                    return index
            else:
                hay = hay - needle_index + 1
                needle_index = 0
        return -1           
   
