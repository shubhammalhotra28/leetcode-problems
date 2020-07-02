# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        li = []
        
        if not root:
            return li
        
        def helper(node,level):
            # curr level check
            
            if len(li)==level:
                li.append([])
                
            li[level].append(node.val)
            
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
            
        helper(root,0)
        
        return li[::-1]
            
            
