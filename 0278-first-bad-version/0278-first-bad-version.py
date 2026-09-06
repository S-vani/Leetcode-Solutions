# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n
        middle = right // 2

        while left < right:
            if isBadVersion(middle):
                right = middle
                middle = ((right - left) // 2) + left
            else:
                left = middle + 1
                middle = ((right - left) // 2) + left
        
        return middle


        