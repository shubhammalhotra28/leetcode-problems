# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,current_val,total_sum):
        
        if root is None:
            return #None
        current_val = (10*current_val)+(root.val)
        if root.left==None and root.right==None:
            
            total_sum[0] += current_val

            return #None
        
        self.helper(root.left,current_val,total_sum)
        self.helper(root.right,current_val,total_sum)
        
        
    def sumNumbers(self, root: TreeNode) -> int:
        total_sum = [0]
        self.helper(root,0,total_sum)
        return total_sum[0]
        

