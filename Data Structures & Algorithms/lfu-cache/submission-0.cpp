class LFUCache {
    struct ListNode {
        int key;
        int value;
        int freq;
        ListNode* prev;
        ListNode* next;

        ListNode(int k,int v) : key(k), value(v), freq(1), prev(nullptr), next(nullptr) {}
    };

    struct LinkedList {
        ListNode* left;
        ListNode* right;
        int size;

        LinkedList() {
            left = new ListNode(0,0);
            right = new ListNode(0,0);
            left->next = right;
            right->prev = left;
            size = 0;
        }

        ~LinkedList() {
            delete left;
            delete right;
        }

        int length() {
            return size;
        }

        void push_right(ListNode* node){
            ListNode* prev = right->prev;
            prev->next = node;
            node->prev = prev;
            node->next = right;
            right->prev = node;
            size++;
        }

        void pop(ListNode* node){
            ListNode* prev = node->prev;
            ListNode* next = node->next;
            prev->next = next;
            next->prev = prev;
            node->prev = nullptr;
            node->next = nullptr;
            size--;
        }

        ListNode* pop_left(){
            ListNode* node = left->next;
            pop(node);
            return node;
        }
    };

    int cap;
    int lfucnt;
    unordered_map<int,ListNode*> nodeMap; // (key,Node*)
    unordered_map<int,LinkedList*> listMap;// (freq,LinkedList*)

    void count(ListNode* node){
        int freq = node->freq;
        listMap[freq]->pop(node);
        node->freq++;
        if(freq == lfucnt && listMap[freq]->length() == 0){
            lfucnt++;
        }
        if(listMap.find(freq+1) == listMap.end()){
            listMap[freq+1] = new LinkedList();
        }
        listMap[freq+1]->push_right(node);
    }

public:
    LFUCache(int capacity) {
        cap = capacity;
        lfucnt = 0;
    }

    ~LFUCache() {
        for(auto& pair : nodeMap){
            delete pair.second;
        }
        for(auto& pair : listMap){
            delete pair.second;
        }
    }
    
    int get(int key) {
        if(nodeMap.find(key) == nodeMap.end()) return -1;
        ListNode* node = nodeMap[key];
        count(node);
        return node->value;
    }
    
    void put(int key, int value) {
        if(nodeMap.find(key) != nodeMap.end()){
            ListNode* node = nodeMap[key];
            node->value = value;
            count(node);
            return;
        }
        if(nodeMap.size() == cap){
            ListNode* node = listMap[lfucnt]->pop_left();
            nodeMap.erase(node->key);
            delete node;
        }
        ListNode* new_node = new ListNode(key,value);
        if(!listMap.count(1)) listMap[1] = new LinkedList();
        listMap[1]->push_right(new_node);
        nodeMap[key] = new_node;
        lfucnt = 1;
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */