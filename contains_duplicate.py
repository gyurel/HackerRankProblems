from typing import List

# nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,1]
# nums = [1,2,3,4]


class Solution:
    # def __int__(self, nums):
    #     self.nums = nums

    def containsDuplicate(self, nums: List[int]) -> bool:
        stack_nums = set()
        for num in nums:
            stack_nums.add(num)

        if not 1 <= len(nums) <= 10**5:
            raise ValueError

        for i in range(len(nums)):
            if not -10**9 <= nums[i] <= 10**9:
                raise ValueError


        if len(nums) == len(stack_nums):
            return False

        return True

    def __call__(self):
        return self.containsDuplicate(nums)


result = Solution()

print(result())
