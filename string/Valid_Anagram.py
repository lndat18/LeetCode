from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        

s = "racecar"
t = "carrace"


result = Solution().isAnagram(s, t)

print(result)  # Output: True
