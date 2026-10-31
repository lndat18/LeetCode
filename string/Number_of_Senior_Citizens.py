class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(d[11:13]) > 60 for d in details)


details = ["7868190130M7522","5303914400F9211","9273338290F4010"]

print(Solution().countSeniors(details))
