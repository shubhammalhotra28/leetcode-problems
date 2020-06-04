# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diaHeight(self,root):
        if root is None:
            return 0,0
        
        ld,lh = self.diaHeight(root.left)
        rd,rh = self.diaHeight(root.right)
        
        ht = 1+max(lh,rh)
        dia_with_root = lh+rh
        
        # dia and ht
        return max(ld,rd,dia_with_root),ht
        
        
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diameter,height = self.diaHeight(root)
        
        return diameter
        
        
