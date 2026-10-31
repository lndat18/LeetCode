class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = p2 = 0
        subsequence = []

        while p1 < len(s) and p2 < len(t):
            print("p1 = ", p1)
            print("p2 = ", p2)
            print("subsequence = ", subsequence)

            if s[p1] == t[p2]:
                subsequence.append(s[p1])
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        subsequence = "".join(subsequence)

        return subsequence == s


s = "node"
t = "neetcode"

print(Solution().isSubsequence(s, t))
