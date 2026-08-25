class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        curr_multiple = k
        while True:
            if curr_multiple not in nums:
                return curr_multiple
            else:
                curr_multiple += k
        