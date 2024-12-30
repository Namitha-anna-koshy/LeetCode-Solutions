class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index = {}
        for i, num in enumerate(nums):
            match = target - num
            if match in num_index:
                return [num_index[match], i]
            num_index[num] = i
        return []

        