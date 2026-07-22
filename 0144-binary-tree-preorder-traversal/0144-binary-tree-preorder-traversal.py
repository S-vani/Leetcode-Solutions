# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        else:
            lst = []
            if root.left and root.right:
                lst.append(root.val)
                lst.extend(self.preorderTraversal(root.left))
                lst.extend(self.preorderTraversal(root.right))
            elif root.left:
                lst.append(root.val)
                lst.extend(self.preorderTraversal(root.left))
            elif root.right:
                lst.append(root.val)
                lst.extend(self.preorderTraversal(root.right))
            return lst
        