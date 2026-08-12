# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [f"{root.val}"]
        else:
            final_paths = []
            paths = []
            if root.left:
                paths.extend(self.binaryTreePaths(root.left))
            if root.right:
                paths.extend(self.binaryTreePaths(root.right))
            for path in paths:
                final_paths.append(f"{root.val}->{path}")
            return final_paths


        