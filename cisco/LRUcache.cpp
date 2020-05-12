class LRUCache {
    private :
    int cap = 0;
    vector<int> v;
    unordered_map<int,int> m;
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if(m.find(key)==m.end())
        {
            return -1;
        }
        else
        {
            for(int i = 0;i<v.size();i++)
            {
                if(v[i]==key)
                {
                    v.erase(v.begin()+i);
                    break;
                }
            }
            v.push_back(key);
            return m[key];
        }
    }
    
    void put(int key, int value) {
        if(m.find(key)!=m.end())
        {
            for(int i = 0;i<v.size();i++)
            {
                if(v[i]==key)
                {
                    v.erase(v.begin()+i);
                    break;
                }
            }
            v.push_back(key);
            m[key] = value;
        }
        else
        {
            if(m.size()<cap){
                m[key] = value;
                v.push_back(key);
            }
            else
            {
                m.erase(v[0]);
                v.erase(v.begin());
                m[key] = value;
                v.push_back(key);
            }
        }
    }
    
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
