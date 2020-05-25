/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
     
        
        ListNode* temp = new ListNode(0);
        ListNode* tempref = temp;
        while(l1 && l2)
        {
            if(l1->val >= l2->val)
            {
                tempref->next = l2;
                l2 = l2->next;
            }
            else
            {
                tempref->next = l1;
                l1 = l1->next;
            }
            tempref = tempref->next;
        }
        tempref->next = (l1==NULL)?l2:l1;
        return temp->next;
    }
};