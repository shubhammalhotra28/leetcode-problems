# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        inorderLen = len(inorder)
        postorderLen = len(postorder)
        
        if inorderLen!=postorderLen or inorderLen == 0 or postorderLen == 0 or inorderLen==None or postorderLen == None:
            return None
        
        # inorder (left root right)
        # postorder (left right root)
        
        root = TreeNode(postorder[-1])
        rootData = root.val
        
        rootIndex = inorder.index(rootData)
        
        root.left = self.buildTree(inorder[0:rootIndex],postorder[0:rootIndex])
        root.right = self.buildTree(inorder[rootIndex+1:],postorder[rootIndex:-1])
        
        return root
        
