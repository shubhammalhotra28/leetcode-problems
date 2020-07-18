#iterative


class Solution:
        
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    
    
        dp = [[0 for j in range(target+1)]for i in range(d+1)]
        mod = (10**9)+7
        #base case
        dp[0][0] = 1
            
        for i in range(1,d+1):
            for j in range(1,target+1):
                # need optimization with 6*i+1
                for k in range(1,f+1):
                    
                    if (j-k)>=0:
                    
                        dp[i][j] = (dp[i][j]+dp[i-1][j-k])%mod
        
        
        return dp[d][target]
    
        
        
        
        



# memoizatiom
class Solution:
        
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    
    
        dp = [[-1 for j in range(target+1)]for i in range(d+1)]
        mod = (10**9)+7
        def numRollsToTargetHelper(d,target):
                
            #base case
        
            if d==0:
                if target!=0:
                    return 0
                elif target==0:
                    return 1
                
            ans = 0
            for i in range(1,f+1):            
                if (target-i)>=0:
                    if dp[d-1][target-i]==-1:
                    # calculate the ans
                        dp[d-1][target-i] = numRollsToTargetHelper(d-1,target-i) 
         
                    ans = (ans+dp[d-1][target-i])%mod
            return ans
    
        return numRollsToTargetHelper(d,target)
        
        
        #d = 2 (1,1)
        #f=3
        #tar = 3
        
        '''
        
        1) 
        
        d = 2 -> 2 count
        f = 5  (1,2,3,4,5)
        tar = 10
        Ans = 5,5 -> ans = 1
        
        
        2) 
        
        d = 2 -> 2 out of 6(1 to 6)
        f = 6 (1,2,3,4,5,6)
        tar = 7
        
        Ans = 1,6 + 2,5 + 3,4 + 4,3 + 5,2 + 6,1 => ans = 7
        
        '''
        
        
        '''
        
        d = 3
        f = 6
        target = 7
        
        Subproblem : 
        d = 2
        target = 7-f(i) => 7-f(1),7-f(2)....... # overlapping 
        
        '''
        
