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
    ListNode* removeElements(ListNode* head, int val) {
        
        ListNode* temp = new ListNode(0);
        temp->next = head;
        
        ListNode* prev = temp;
        ListNode* curr = head;
        
        while(curr!=NULL)
        {
            if(curr->val==val)
            {
                prev->next = curr->next;
            }
            else
            {
                prev = curr;
            }
            curr = curr->next;
        }
        
        return temp->next;
        
        
    }
};
