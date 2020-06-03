# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def nodesAtDepthK(self,root,k,s):
        
        if root is None:
            return
        if k==0:
            s.append(root.val)
        self.nodesAtDepthK(root.left,k-1,s)
        self.nodesAtDepthK(root.right,k-1,s)
        
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        s = [] # list
        
        if root.val == target.val:
            self.nodesAtDepthK(root,K,s)
            return 0
        
        left_dist = self.distanceK(root.left,target,K)
        
        if left_dist!=-1:
            
            dist_from_root = left_dist+1
            if dist_from_root==K:
                s.append(root.val)
                
            else:
                
                # its on right side
                self.nodesAtDepthK(root,K-left_dist-2,s)
                
        right_dist = self.distanceK(root.right,target,K)
        
        if right_dist!=-1:
            
            self.dist_from_root = right_dist+1
            if dist_from_root == K:
                
                s.append(root.val)
            else:
                # its on left side
                
                self.nodesAtDepthK(root,K-right_dist-2,s)
        return s
        
        
