# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBST(self,root,min_range,max_range):
        
        if root is None:
            return True
        if root.val < min_range or root.val > max_range:
            return False
        
        leftCheck = self.isBST(root.left,min_range,root.val-1)
        
        rightCheck = self.isBST(root.right,root.val+1,max_range)
        
        return leftCheck and rightCheck
        
        
        
    
    
    def isValidBST(self, root: TreeNode) -> bool:
        ans = self.isBST(root,-2147483648,2147483647)
        return ans






#############################################################


###########  2nd Approach ###################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBST(self,root):
        #min,max,bool(isBST)
        if root is None:
            return 2147483647,-2147483648,True
        
        leftMin,leftMax,isLeftBST = self.isBST(root.left)
        rightMin,rightMax,isRightBST = self.isBST(root.right)
        
        minimum = min(leftMin,rightMin,root.val)
        maximum = max(leftMax,rightMax,root.val)
        isTreeBST = True # initially true
        if root.val<=leftMax or root.val>=rightMin:
            isTreeBST = False
        
        if not(isLeftBST) or not(isRightBST):
            isTreeBST = False
        
        return minimum,maximum,isTreeBST
        
        
        
        
    def isValidBST(self, root: TreeNode) -> bool:
        
        minimum, maximum, isBSTOK = self.isBST(root)
        
        return isBSTOK
            
        
        
        

