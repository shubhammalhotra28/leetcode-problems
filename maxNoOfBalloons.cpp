class Solution {
public:
    int maxNumberOfBalloons(string text) {
        
        int b=0,a=0,l=0,o=0,n=0;
        
        for(auto hello : text)
        {
            if(hello=='b')
            {
                b++;
            }
            if(hello=='a')
            {
                a++;
            }
            if(hello=='l')
            {
                l++;
            }
            if(hello=='o')
            {
                o++;
            }
            if(hello=='n')
            {
                n++;
            }
            
        }
        
        return min(b,min(a,min(l/2,min(o/2,n))));
        
        
    }
};
