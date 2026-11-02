class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count_map = dict()

        for num in nums:

            count_map[num] = count_map.get(num, 0) + 1

            if count_map.get(num, 0) > 1:
                return True

        return False


nums = [1, 2, 3, 3]

print(Solution().containsDuplicate(nums))