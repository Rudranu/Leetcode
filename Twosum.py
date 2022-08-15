class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = {}
        for i in range(len(nums)):
                temp = target-nums[i]
                if temp in ans:
                 return i,ans[temp]
                ans[nums[i]] = i