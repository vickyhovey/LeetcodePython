class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            if target - value in hash_map:
                return [hash_map[value], index]
            else:
                hash_map[value] = index
