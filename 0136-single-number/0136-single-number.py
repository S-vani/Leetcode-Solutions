class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            j = len(nums) - 1
            i = 0
            while True:
                if nums[i] == nums[j]:
                    nums.pop(j)
                    nums.pop(i)
                    break
                i += 1
                if i == j:
                    return nums[i]
            return self.singleNumber(nums)
                
