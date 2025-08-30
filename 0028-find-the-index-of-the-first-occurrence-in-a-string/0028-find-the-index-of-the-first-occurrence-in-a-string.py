class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        index = 0
        needle_index = 0
        hay = 0

        if haystack == needle:
            return 0

        while hay < len(haystack):
            if needle_index == len(needle):
                index = hay - len(needle)
                return index
            elif needle[needle_index] == haystack[hay]:
                if len(needle) == 1:
                    return hay
                needle_index += 1
            else:
                if needle_index >= 1:
                    hay = hay - needle_index
                needle_index = 0
            hay += 1   
        return -1           
   