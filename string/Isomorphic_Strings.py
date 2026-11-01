class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        else:
            s2t, t2s = {}, {}

            for i in range(len(s)):

                if s2t.get(s[i], 0) == 0:
                    s2t[s[i]] = t[i]

                elif s2t.get(s[i]) != t[i]:
                    return False


            for i in range(len(s)):

                if t2s.get(t[i], 0) == 0:
                    t2s[t[i]] = s[i]

                elif t2s.get(t[i]) != s[i]:
                    return False

            return True

# s = "egg"
# t = "add"

# s = "paper" 
# t = "title"

# s = "foo"
# t = "bar"

# s="bbbaaaba"
# t="aaabbbba"

s="abbAB"
t="ABBAa"

print(Solution().isIsomorphic(s, t))