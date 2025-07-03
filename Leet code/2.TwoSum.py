"""1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution(object):
    def twoSum(self, nums, target):
        new_list = []
        size = len(nums)
        for numbers in nums:
            difference = target - numbers
            new_list.append(difference)
        for i in range(size):
            if new_list[i] in nums and nums.index(new_list[i]) != i:
                return [i, nums.index(new_list[i])]
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(sol.twoSum([3, 2, 4], 6))        # Output: [1, 2]
    print(sol.twoSum([3, 3], 6))           # Output: [0, 1]