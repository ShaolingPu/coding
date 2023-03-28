#最大子数组问题

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10001
        
        sum_ = 0
        i = 0
        while i < len(nums):
            if sum_ <= 0:
                sum_ = nums[i]
            else:
                sum_ += nums[i]
            ans = max(ans, sum_)
            i += 1
        return ans
