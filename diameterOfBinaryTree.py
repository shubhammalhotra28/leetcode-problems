# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#
         self.right = right
class Solution:
    
    def height(self,root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        
        return 1+max(lh,rh)
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        option1 = self.height(root.left)+self.height(root.right)
        option2 = self.diameterOfBinaryTree(root.left)
        option3 = self.diameterOfBinaryTree(root.right)
        
        return max(option1,option2,option3)
    
        
######################################################################        


##OPTIMIZED##

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def calDiameterAndHeight(self,root):
        if root is None:
            return 0,0 # diameter and height
        ld,lh = self.calDiameterAndHeight(root.left)
        rd,rh = self.calDiameterAndHeight(root.right)
        
        ht = 1+max(lh,rh) # calculating the height
        
        diaWithRoot = lh+rh # diameter with Root
        
        return max(ld,rd,diaWithRoot),ht
        
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diameter,height = self.calDiameterAndHeight(root)
        
        return diameter
            
        
          
