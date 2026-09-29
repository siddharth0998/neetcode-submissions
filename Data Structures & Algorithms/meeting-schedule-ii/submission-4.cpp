/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int n = intervals.size();
        vector<int> start;
        vector<int> end;
        for(int i=0;i<n;i++){
            start.push_back(intervals[i].start);
            end.push_back(intervals[i].end);
        }
        sort(start.begin(),start.end());
        sort(end.begin(),end.end());
        int i=0,j=0,cnt=0,ans = 0;
        while(i < n){
            if(start[i] < end[j]){
                cnt += 1;
                ans = max(ans,cnt);
                i += 1;
            }
            else{
                cnt -= 1;
                j += 1;
            }
        }
        return ans;
    }
};
