import math as m

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums.count(0) >= 2:
            return [0] * len(nums)

        product_all = m.prod(n for n in nums if n != 0)

        if m.prod(nums) == 0:

            return [product_all if n == 0 else 0 for n in nums]

        else:

            return [product_all//n for n in nums]        


# nums = [1,2,4,6]
# nums = [-1,0,1,2,3]
nums=[0,8,0,8]
# nums=[-1,1,0,-3,3]
# nums=[0,0]

print(Solution().productExceptSelf(nums))