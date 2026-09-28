class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        sort(intervals.begin(),intervals.end(),[](const vector<int>& a,const vector<int>& b){if(a[0] != b[0]) return a[0] < b[0]; return a[1] < b[1];});
        vector<int> res = intervals[0];
        int cnt = 0;
        for(int i=1;i<n;i++){
            if(res[1] <= intervals[i][0]){
                res = intervals[i];
            }
            else{
                res = res[1] < intervals[i][1] ? res : intervals[i];
                cnt += 1;
            }
        }
        return cnt;
    }
};
