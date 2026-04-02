class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = right // 2

        while pivot != left:
            if nums[pivot] == target:
                return pivot

            if nums[pivot] > target:
                right = pivot
            else:
                left = pivot
            pivot = (right - left) // 2
            pivot += left

        if nums[pivot] == target:
            return pivot
        if len(nums) > 1 and nums[pivot+1] == target:
            return pivot + 1
        return -1
