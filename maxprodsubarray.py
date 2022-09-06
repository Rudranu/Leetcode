from ast import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        minprod,maxprod=ans,ans
        for i in range(1,len(nums)):
            if nums[i]<0:
                minprod,maxprod  = maxprod,minprod
            maxprod=max(nums[i],maxprod*nums[i])
            minprod=min(nums[i],minprod*nums[i])
            ans=max(ans,maxprod)
        return ans