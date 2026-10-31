class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for i in range(len(words) - 1, -1, -1):
            w = words[i]

            if any(w != other and w in other for other in words):
                result.append(words.pop(i))

        return result


words = ["mass","as","hero","superhero"]
print(Solution().stringMatching(words))