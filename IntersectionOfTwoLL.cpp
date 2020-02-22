/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *a = headA;
        ListNode *b = headB;
        while(a!=NULL || b!=NULL)
        {
            if(a!=NULL)
            {
                a = a->next;
            }
            else
            {
                headB = headB->next;
            }
            if(b!=NULL)
            {
                b = b->next;
            }
            else
            {
                headA = headA->next;
            }
        }
        while(headA!=headB)
        {
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
    }
    
};
