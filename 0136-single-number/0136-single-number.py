class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while True:
            if i == len(nums) - 1:
                return nums[i]

            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2

                
