class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        le=len(nums)
        for i in range(0,le):
            for j in range(i+1,le):
                if nums[i]+nums[j]==target:
                    return [i,j] 