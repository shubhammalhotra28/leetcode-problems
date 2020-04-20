/*
Brute force approach 
time complexity o(n2)
*/


class Solution {
    public int maxArea(int[] height) {
         int max = Integer.MIN_VALUE;
        
        for(int i = 0;i<height.length;i++)
        {
            for(int j = i+1;j<height.length;j++)
            {
                int min = Math.min(height[i],height[j]);
                max = Math.max(max,((j-i)*min));
            }
        }
        return max;
    }
}
