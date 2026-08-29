class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        i = 0
        nums_majority = int(len(nums)/2)
        while True:
            if nums_sorted[i] == nums_sorted[i+nums_majority]:
                return nums_sorted[i]
            else:
                i += 1