class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size();
        int m = queries.size();
        sort(intervals.begin(),intervals.end());
        vector<int> temp = queries;
        sort(temp.begin(),temp.end());
        priority_queue<pair<int,int> , vector<pair<int,int>> ,                  greater<pair<int,int>>> minheap;
        unordered_map<int,int> res;
        vector<int> ans(m);
        int i=0;

        for(int q=0;q<m;q++){
            while(i < n && intervals[i][0] <= temp[q]){
                int start = intervals[i][0];
                int end = intervals[i][1];
                minheap.push({end-start+1 , end});
                i++;
            }
            while(!minheap.empty() && minheap.top().second < temp[q]){
                minheap.pop();
            }
            if(!minheap.empty()) res[temp[q]] = minheap.top().first;
            else res[temp[q]] = -1;
        }
        for(int i=0;i<m;i++){
            ans[i] = res[queries[i]];
        }
        return ans;
    }
};
