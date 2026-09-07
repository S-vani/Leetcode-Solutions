class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        else:
            num = n / 4
            if num != round(num):
                return False
            return self.isPowerOfFour(num)