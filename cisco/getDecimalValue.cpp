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
    int getDecimalValue(ListNode* head) {
        
        int n=0;
        while(head!=NULL)
        {
            n += head->val;
            n = n<<1;
            head = head->next;
        }
        n = n>>1;
        return n;
    }
};





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
    int getDecimalValue(ListNode* head) {
        
       ListNode* temp = head;
        int n = 0;
        while(temp!=NULL)
        {
            n++;
            temp = temp->next;
        }
        
        int ans = 0;
        int k = n-1;
        
        ListNode* temp1 = head;
        
        while(temp1!=NULL)
        {
            if(temp1->val==1){
            
                ans += pow(2,k);
            }
            temp1 = temp1->next;
            k--;
        }
        return ans;
        
    }
};




//.  101 
// 1*2^0 + 
