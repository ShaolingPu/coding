class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quiksort(nums, 0, len(nums)-1)
        return nums

    def quiksort(self, nums, i, j):
        if i >= j:
            return 
        low, high = i, j
        key = nums[low]
        while low < high:
            while low < high and nums[high] >= key:
                high -= 1
            if low < high:
                nums[low] = nums[high]
                low += 1
            while low < high and nums[low] < key:
                low += 1
            if low < high:
                nums[high] = nums[low]
                high -= 1
        nums[low] = key
        self.quiksort(nums, i, low-1)
        self.quiksort(nums, low+1, j)
