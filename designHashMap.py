
class MapNode:
    
    def __init__(self,key,value):
        
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
        

    def getCompressed(self,hc):
        
        return abs(hc%self.bucketSize)
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        hc = hash(key)
        index = self.getCompressed(hc)
        head = self.buckets[index]
        
        while head is not None:
            
            if head.key==key:
                head.value = value
                return
            head = head.next
        head = self.buckets[index]
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        hc = hash(key)
        index = self.getCompressed(hc)
        head = self.buckets[index]
        
        while head is not None:
            
            if head.key==key:
                
                return head.value
            head = head.next
            
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        
        hc = hash(key)
        index = self.getCompressed(hc)
        
        head = self.buckets[index]
        
        prev = None
        
        while head is not None:
            
            if head.key==key:
                
                # do 
                
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count-=1
                
            prev = head
            head = head.next
        
        
        
        
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
