class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
       
        sort(A.begin(),A.end());
        int sum = -1;
        int i = 0;
        int j = A.size()-1;
        
        while(i<j)
        {
            if((A[i]+A[j]) < K)
            {
                sum = max(sum,(A[i]+A[j]));
                i++;
            }
            else{j--;}
            
        }
        return sum;
    }
};
