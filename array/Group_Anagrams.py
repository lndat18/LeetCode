class Solution:
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        bucket = dict()

        for word in strs:
            label = "".join(sorted(word))

            if bucket.get(label, None) == None:
                bucket[label] = [word]
            else:
                bucket[label].append(word)

        for value in bucket.values():
            result.append(value)

        return result
    

# strs = ["act","pots","tops","cat","stop","hat"]
strs=["ddddddddddg","dgggggggggg"]

print(Solution().groupAnagrams(strs))