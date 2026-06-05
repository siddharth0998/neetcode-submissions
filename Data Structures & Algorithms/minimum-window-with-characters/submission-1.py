class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count , window = {},{}

        for c in t:
            count[c] = 1 + count.get(c,0)

        have,req = 0,len(count)
        l = 0
        res,resLen = [-1,-1],float("infinity")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            
            while have == req:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""




