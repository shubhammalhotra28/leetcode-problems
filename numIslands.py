class Solution:
    
    
    def dfs(self,grid,i,j):
        
        if(i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=='0'):
            return 0
        
        grid[i][j]='0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        return 1
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid)==0 or grid==None:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        numOfIslands = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    numOfIslands += self.dfs(grid,i,j) # setting the value to be 1 and rest of the islands to be 0
        return numOfIslands
        
