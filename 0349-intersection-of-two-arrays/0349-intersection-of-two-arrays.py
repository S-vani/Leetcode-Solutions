class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []

        for n in nums1:
            for i in nums2:
                if n == i and not(n in intersection):
                    intersection.append(n)
        
        return intersection