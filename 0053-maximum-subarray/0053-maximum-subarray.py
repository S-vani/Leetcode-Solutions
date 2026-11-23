class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        largest_subarray = float("-inf")
        current_subarray = float("-inf")
        for i in range(len(nums)):
            if nums[i] + current_subarray < nums[i]:
                current_subarray = nums[i]
            else:
                current_subarray += nums[i]

            largest_subarray = max(largest_subarray, current_subarray)

        return largest_subarray
