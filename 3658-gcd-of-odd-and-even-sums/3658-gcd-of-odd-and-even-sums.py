class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:  
        sumodd = 0
        sumeven = 0
        for i in range(1, n*2 +1):
            if i % 2 == 0:
                sumeven += i
            else:
                sumodd += i

        r = 1
        bigger = max(sumodd, sumeven)
        smaller = min(sumodd, sumeven) 
        while True:
            last_r = r
            q = int(bigger/smaller)
            r = bigger - (smaller *q)
            if r == 0:
                return last_r
            else:
                bigger = smaller
                smaller = r




