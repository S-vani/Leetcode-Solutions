class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        for n in nums1:
            for i in nums2:
                if n == i and not(n in intersection):
                    intersection.append(n)
        
        return intersection