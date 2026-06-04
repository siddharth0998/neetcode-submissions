class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for st in strs:
            n = len(st)
            ans += str(n) + "#" + st
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i,j=0,0
        while j < len(s):
            if s[j] != "#":
                j += 1
            else:
                sub = s[i:j]
                print(sub)
                temp = s[j+1:j+1+int(sub)]
                ans.append(temp)
                i,j = j+1+int(sub),j+1+int(sub)
        return ans 