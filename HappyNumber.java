class Solution {
    
    private int getNext(int n)
    {
        int sum = 0;
        while(n>0)
        {
            int a = n%10;
            n = n/10;
            sum += a*a; 
        }
        return sum;
    }
    public boolean isHappy(int n) {
        Set<Integer> s = new HashSet<>();
        
        while(n!=1 && !s.contains(n))
        {
            s.add(n);
            n = getNext(n);
        }
        return n==1;
    }
}
