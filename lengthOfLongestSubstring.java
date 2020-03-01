class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int first_ptr = 0;
        int second_ptr = 0;
        int max = 0;
        
        HashSet<Character> set = new HashSet();
        
        while(second_ptr < s.length()){
            
            if(!set.contains(s.charAt(second_ptr))){
                // if it doesnt contains then add and increment secondf ptr
                
                set.add(s.charAt(second_ptr));
                second_ptr++;
                max = Math.max(set.size(),max);
                
            }
            else{
                // if contains remove and increment the first ptr
                set.remove(s.charAt(first_ptr));
                first_ptr++;
            }
            
        }
        
        return max;
        
        
    }
}
