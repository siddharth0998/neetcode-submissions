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