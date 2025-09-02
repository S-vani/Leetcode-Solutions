class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in range(len(nums)):
            if nums[num] == val:
                nums[num] = -1
        
        for index in range(len(nums)):
            for i in range(index + 1, len(nums)):
                if nums[index] < nums[i]:
                    swap = nums[i]
                    nums[i] = nums[index]
                    nums[index] = swap
                
        k = 0
        for n in nums:
            if n != -1:
                k += 1

        return k