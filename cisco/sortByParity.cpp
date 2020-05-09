



// using extra space

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        
        vector<int> ans;
        
        for(int i = 0;i<A.size();i++)
        {
            if(A[i]%2==0)
            {
                ans.push_back(A[i]);
            }
        }
        for(int i = 0;i<A.size();i++){
        
            if(A[i]%2!=0)
            {
                ans.push_back(A[i]);
            }
        }
        return ans;
        
    }
};

 // Inplace Algorithm
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        
        int i=0;
        int j = A.size()-1;
        
        while(i<j)
        {
            if(A[i]%2 > A[j]%2)
            {
                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
            if(A[i]%2==0)
            {
                i++;
            }
            if(A[j]%2==1)
            {
                j--;
            }
        }
        
        return A;
    }
};
