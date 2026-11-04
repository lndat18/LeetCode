class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_frequent = dict()

        for num in nums:
            count_frequent[num] = count_frequent.get(num, 0) + 1

        return sorted(count_frequent, key=count_frequent.get, reverse=True)[:k]


nums = [1,2,2,3,3,3]
k = 2

print(Solution().topKFrequent(nums, k))