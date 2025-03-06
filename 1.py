class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for pos, num in enumerate(nums):
            remaining = target - num

            if remaining in seen:
                return [seen[remaining], pos]

            seen[num] = pos

        return []

# print(Solution().twoSum([2, 7, 11, 15], 9))