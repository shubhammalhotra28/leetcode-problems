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
    private:
    ListNode* reverse(ListNode* head)
    {
        ListNode *curr,*prev,*next;
        curr = head;
        prev = NULL;
        while(curr!=NULL){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      
        l1 = reverse(l1);
        l2 = reverse(l2);
        ListNode* l3 = NULL;
        ListNode* node = NULL;
        int a = 0,b=0,c=0;
        while(l1||l2||c){
            a = b =0;
            if(l1)
            {
                a = l1->val;
                l1 = l1->next;
            }
            if(l2)
            {
                b = l2->val;
                l2 = l2->next;
            }
            c += a+b;
            if(node)
            {
                node->next = new ListNode(c%10);
                node = node->next;
            }
            else
            {
                node = new ListNode(c%10);
                l3 = node;
            }
            c = c/10;
        }
        return reverse(l3);
    }
};



