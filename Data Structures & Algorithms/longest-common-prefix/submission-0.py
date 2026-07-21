class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ch = ''
        n = len(strs)
        s = 0
        ans = 0
        flag = True
        while flag:
            for i in range(n):
                if i == 0:
                    if s < len(strs[0]):
                        ch = strs[0][s]
                    else: 
                        flag = False
                        break
                else:
                    if s < len(strs[i]):
                        if ch != strs[i][s]:
                            flag = False
                            break
                    else:
                        flag = False
                        break
            ans += 1
            s += 1
        return strs[0][0:ans-1] 
