class Node {
public:
    int key;
    int value;
    Node* prev;
    Node* next;

    Node(int k,int v) : key(k), value(v), prev(nullptr), next(nullptr) {} 
};

class LRUCache {
private:
    int cap;
    unordered_map<int,Node*> mpp;
    Node* left;
    Node* right;

    void remove(Node* node){
        Node* prev = node->prev;
        Node* next = node->next;
        prev->next = next;
        next->prev = prev;
    }

    void insert(Node* node){
        Node* prev = right->prev;
        prev->next = node;
        node->prev = prev;
        node->next = right;
        right->prev = node;
    }

    Node* update(Node* node ,int key,int value){
        remove(node);
        insert(node);
        node->value = value;
        return node;
    }


public:
    LRUCache(int capacity) {
        cap = capacity;
        mpp.clear();
        left = new Node(0,0);
        right = new Node(0,0);
        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        if(mpp.find(key) != mpp.end()){
            Node* node = mpp[key];
            remove(node);
            insert(node);
            return node->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(mpp.find(key) != mpp.end()){
            mpp[key] = update(mpp[key],key,value);
        }
        else{
            Node* node = new Node(key,value);
            if(mpp.size() < cap){
                insert(node);
                mpp[key] = node;
            }
            else{
                Node* lru = left->next;
                int k = lru->key;
                mpp.erase(k);
                remove(lru);
                insert(node);
                mpp.insert({key,node});
                delete lru;
            }
        }
    }
};
