import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        dict = {}
        
        for i, v in items:
            
            if i in dict:
                # if length less than 5 -> push to heap
                if len(dict[i])<5:
                    heappush(dict[i],v)
                elif (dict[i][0])<v: #if 0th value is les than current
                    heapreplace(dict[i],v) #replace
            else:
                dict[i] = [v] #set value with heap intialisation []
                
        output = [] 
        # making the output -> list
        for i in dict:
            
            li = []
            li.append(i)
            avg = sum(dict[i])//len(dict[i])
            li.append(avg)
            output.append(li)
            
        return output
        
        
