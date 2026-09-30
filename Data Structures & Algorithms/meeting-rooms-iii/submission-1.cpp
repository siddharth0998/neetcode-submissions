/*
so in this question we use 2 min heap available and used available stores which room is available accoring to its room_number lower is 1st and used will store (ent_time,room_number) which says at some perticular time this room will become empty and ready to use again. now we loop through meetings array containing start,end time of every meeting and we check for below things:

1. so we need to check used min heap with our current meeting that whether we can delete some completed meeting from used and put it in available or not.

2. if available is empty then we have to wait. but we are not going to simulate waiting period we just update the top used meeting end time with our current meeting.

3. we assign the room to meeting and update neccessary things.

we also maintain 1 array for all rooms and whenever we add meeting we will update it's count by 1 and in last we can just find max from that array if max is same we go for lower index value that is our ans.
*/

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        int len = meetings.size();
        auto cmp = [](const pair<int,int>& a, const pair<int,int>& b){
            return a > b;
        };
        sort(meetings.begin(),meetings.end());
        priority_queue<pair<int,int>,vector<pair<int,int>>,decltype(cmp)> used(cmp); // (end_time , room_number)
        priority_queue<int,vector<int>,greater<int>> available; // {0 , 1, 2}
        for(int i=0;i<n;i++) available.push(i);
        vector<int> cnt(n,0);

        for(auto meet : meetings){
            int start = meet[0];
            int end = meet[1];

            while(!used.empty() && start >= used.top().first){
                pair<int,int> curr = used.top();
                used.pop();
                available.push(curr.second);
            }

            if(available.empty()){
                int curr_end = used.top().first;
                int curr_room = used.top().second;
                used.pop();
                end = curr_end + (end - start);
                available.push(curr_room);
            }

            int curr_room = available.top();
            available.pop();
            used.push({end,curr_room});
            cnt[curr_room] += 1;
        }
        int ans = -1;
        int maxi = -1;
        for(int i=0;i<n;i++){
            if(cnt[i] > maxi){
                ans = i;
                maxi = cnt[i];
            }
        }
        return ans;
    }
};