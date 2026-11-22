class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final_lst = []
        sorted_nums = sorted(nums)
        nums_length = len(nums)
        s = set()

        for i in range(nums_length):
            left = i+1
            right = nums_length - 1
            while left < right:
                sum_of_tree = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if sum_of_tree == 0:
                    if (sorted_nums[i], sorted_nums[left], sorted_nums[right]) not in s:
                        final_lst.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                        s.add((sorted_nums[i], sorted_nums[left], sorted_nums[right]))
                    left += 1
                elif sum_of_tree > 0:
                    right -= 1
                else:
                    left += 1
        
        return final_lst
