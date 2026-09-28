class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        sort(intervals.begin(),intervals.end(),[](const vector<int>& a,const vector<int>& b){return a[0] < b[0];});
        vector<vector<int>> res;
        res.push_back(intervals[0]);
        for(int i=1;i<n;i++){
            if(res.back()[1] < intervals[i][0]){
                res.push_back(intervals[i]);
            }
            else{
                res.back() = {min(res.back()[0],intervals[i][0]),max(res.back()[1],intervals[i][1])};
            }
        }
        return res;
    }
};
