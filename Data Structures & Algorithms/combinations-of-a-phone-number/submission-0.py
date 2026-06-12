class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToString = {"2" : "abc",
                         "3" : "def",
                         "4" : "ghi",
                         "5" : "jkl",
                         "6" : "mno",
                         "7" : "pqrs",
                         "8" : "tuv",
                         "9" : "wxyz" }

        def backTrack(i,curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for c in digitToString[digits[i]]:
                backTrack(i+1,curr + c)
        backTrack(0,"")
        if len(digits):return res
        return []
        