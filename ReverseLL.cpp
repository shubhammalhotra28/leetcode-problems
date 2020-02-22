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
    ListNode* reverseList(ListNode* head) {
        if(head==NULL || head->next == NULL)
        {
            return head; 
        }
        ListNode *smaller_LL = reverseList(head->next);
        // smaller_LL = head;
        // head->next = NULL;
        ListNode *tail = head->next;
        tail->next = head;
        head->next = NULL;
        return smaller_LL;
    }
};
