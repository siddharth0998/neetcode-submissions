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
    bool canAttendMeetings(vector<Interval>& intervals) {
        int n = intervals.size();
        sort(intervals.begin(),intervals.end(),[](const Interval& a,const Interval& b){if(a.start!=b.start) return a.start < b.start; return a.end < b.end;});
        Interval res = intervals[0];
        for(int i=1;i<n;i++){
            if(res.end <= intervals[i].start){
                res = intervals[i];
            }
            else return false;
        }
        return true;
    }
};
