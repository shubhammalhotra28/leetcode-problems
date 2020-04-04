class Solution {
public:
    bool isPalindrome(string s) {
        
        int start = 0;
        int end = s.length()-1;
        transform(s.begin(),s.end(),s.begin(),::tolower);
        cout<<s<<endl;
        // NOTE - isalnum is used to check the character is alphanumeric 
        
        while(start<end)
        {
            if(s[start]==s[end])
            {
                start++;
                end--;
            }
            else if (!isalnum(s[start]))
            {
                start++;
            }
            else if (!isalnum(s[end]))
            {
                end--;
            }
            else
            {
                return false;
            }
           // else if(s[start])
        }
        return true;
        //return false;
        
    }
};


