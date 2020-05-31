# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head,k):
        
        prev = None;
        curr = head;
        next_p = None;
        
        while k>0:
            next_p = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next_p;
            k-=1;
        
        return prev;
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        ptr = head;
        count = 0;
        
        while(count<k and ptr!=None):
            
            ptr = ptr.next;
            count+=1;
        
        if count==k:
            #print(head.val);
            reversedhead = self.reverse(head,k);
            #print(head.next.val);
            #print(ptr.val);
            head.next = self.reverseKGroup(ptr,k);
            return reversedhead;
        
        return head;
            
    
    
