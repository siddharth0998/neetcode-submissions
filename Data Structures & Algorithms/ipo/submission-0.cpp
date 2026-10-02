class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<pair<int,int>> cap_pro(n);
        for(int i=0;i<n;i++){
            cap_pro[i] = {capital[i],profits[i]};
        }
        sort(cap_pro.begin(),cap_pro.end());
        priority_queue<int> maxheap; // (profit)
        int i = 0;
        while(true){
            while(i < n && cap_pro[i].first <= w){
                maxheap.push(cap_pro[i].second);
                i++;
            }
            if(k > 0 && !maxheap.empty()){
                w += maxheap.top();
                maxheap.pop();
                k -= 1;
            }
            else break;
        }
        return w;
    }
};