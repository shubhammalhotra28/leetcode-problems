# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedCheck(self,root:TreeNode): 
        
        if root==None:
            return 0,True
        
        lh,isLeftBalanced = self.isBalancedCheck(root.left)
        rh, isRightBalanced = self.isBalancedCheck(root.right)
        
        h = 1+max(lh,rh);
        
        if lh-rh>1 or rh-lh>1:
            return h,False
        
        if isLeftBalanced and isRightBalanced:
            return h,True
        else:
            return h,False
        
        
    def isBalanced(self, root: TreeNode) -> bool:
        
        h,ans = self.isBalancedCheck(root)
        
        return ans
        
