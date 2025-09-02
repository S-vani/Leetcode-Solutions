class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for n in range(len(nums)):
            if nums[n] == val:
                nums[n] = -1
        
        for index in range(len(nums)):
            for i in range(index + 1, len(nums)):
                if nums[index] < nums[i]:
                    swap = nums[i]
                    nums[i] = nums[index]
                    nums[index] = swap
        
        print(nums)
        
        k = 0
        for n in nums:
            if n != -1:
                k += 1

        return k