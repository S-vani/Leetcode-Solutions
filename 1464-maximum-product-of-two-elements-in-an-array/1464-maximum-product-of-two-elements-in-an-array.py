class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def _calculate_product(n1: int, n2: int) -> int:
            return (n1-1)*(n2-1)
        if len(nums) == 2:
            return _calculate_product(nums[0], nums[1])
        largest = 0
        for i in range(len(nums)):
            for n in range(i+1, len(nums)):
                if i != len(nums) - 1:
                    largest = max(largest, _calculate_product(nums[i], nums[n]))
        
        return largest
        