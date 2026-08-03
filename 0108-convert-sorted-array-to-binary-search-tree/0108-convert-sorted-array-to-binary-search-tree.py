# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            i = len(nums)//2
            tree = TreeNode(nums[i])
            tree.left = self.sortedArrayToBST(nums[:i])
            tree.right = self.sortedArrayToBST(nums[i+1:])
            return tree
        