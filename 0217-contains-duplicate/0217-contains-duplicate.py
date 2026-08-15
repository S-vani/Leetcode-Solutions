class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        print(nums_sorted)
        for i in range(len(nums) - 1):
            print(i)
            if nums_sorted[i] == nums_sorted[i+1]:
                return True
        
        return False