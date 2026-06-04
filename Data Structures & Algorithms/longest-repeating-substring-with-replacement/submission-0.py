class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mpp = {}
        n = len(s)
        maxF = 0
        l,r = 0,0
        ans = 0
        while r<n:
            if s[r] not in mpp:
                mpp[s[r]] = 1
            else:
                mpp[s[r]] += 1
            maxF = max(maxF,mpp[s[r]])
            if (r-l+1 - maxF) > k:
                mpp[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
            
            r += 1
        return ans 