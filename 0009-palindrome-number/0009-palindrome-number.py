class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringVersion = str(x)
        reverse = ""
        for i in range(len(stringVersion)):
            index = (i - len(stringVersion) + 1) * (-1)
            reverse += stringVersion[index]
        
        if reverse == stringVersion:
            return True
        else:
            return False
        