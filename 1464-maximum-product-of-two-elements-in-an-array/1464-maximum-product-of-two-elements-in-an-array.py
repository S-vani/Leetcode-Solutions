class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def _calculate_product(n1: int, n2: int) -> int:
            return (n1-1)*(n2-1)
        if len(nums) == 2:
            return _calculate_product(nums[0], nums[1])
        largest_num_index = 0
        second_largest_num_index = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[largest_num_index]:
                second_largest_num_index = largest_num_index
                largest_num_index = i
            elif nums[i] > nums[second_largest_num_index]:
                second_largest_num_index = i
            print(f"{largest_num_index} and {second_largest_num_index}")

        return _calculate_product(nums[largest_num_index], nums[second_largest_num_index])
            
        