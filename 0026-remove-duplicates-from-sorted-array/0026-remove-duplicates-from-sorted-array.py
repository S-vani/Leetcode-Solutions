class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for num in range(len(nums) - 1):
            if nums[num] == 101:
                continue
            for i in range(num + 1, len(nums)):
                if nums[num] == nums[i]:
                    nums[num] = 101
        nums.sort()
        
        for n in nums:
            if n != 101:
                k+=1
        

        return k


