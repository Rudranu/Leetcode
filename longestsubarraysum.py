from ast import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        arr=[nums[0]]
        maxsum=arr[0]
        for i in range(1,len(nums)):
            arr.append(max(arr[i-1]+nums[i],nums[i]))
            if arr[i]>maxsum:
                maxsum=arr[i]
        return maxsum
        