class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []

        for n in nums1:
            if n in nums2:
                intersection.append(n)
        
        return list(set(intersection))