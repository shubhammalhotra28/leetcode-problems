# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        temp = ListNode(-1);
        temp.next = head;
        prev = temp;
        
        while head and head.next:
            
            first = head;
            second = head.next;
            
            prev.next = second;
            first.next = second.next;
            second.next = first;
            
            prev = first;
            head = first.next;
            
        return temp.next;
