class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(min(strs, key=len))

        for i in range(n):
            char = {w[i] for w in strs}
            if len(char) != 1:
                return strs[0][:i]

        return strs[0][:n]


strs = ["bat","bag","bank","band"]

print(Solution().longestCommonPrefix(strs))