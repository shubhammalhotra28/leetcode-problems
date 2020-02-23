class Solution {
public:
    bool isPalindrome(int x) {
        int n = x;
        unsigned reversed_num = 0;
        while(n>0)
        {
            int y = n%10;
            reversed_num = reversed_num*10+y;
            n = n/10;
        }
        return x == reversed_num;
    }
};
