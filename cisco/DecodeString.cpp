class Solution {
public:
    string decodeString(string s) {
       
        int i = 0;
        int n = s.length();
        stack<int> st1;
        stack<string> st2;
        string result = "";
        
        while(i<n)
        {
            if(isdigit(s[i]))
            { // if digit
                int count = 0;
                while(isdigit(s[i]))
                {
                    count = count*10+s[i]-'0';
                    i++;
                }
                st1.push(count);
            }
            else if(s[i]=='[')
            { // opening bracket
                st2.push(result);
                result = "";
                i++;
            }
            else if (s[i]==']')
            { // closing bracket
                int k = st1.top();
                st1.pop();
                string temp = st2.top();
                st2.pop();
                for(int j = 0;j<k;j++)
                {
                    temp += result;
                }
                result = temp;
                i++;
            }
            else
            { // simply add
                result += s[i];
                i++;
            }
        }
        return result;
        
        
    }
};
