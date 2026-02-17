class Solution:
    def solve(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        num_len = len(nums3)
        mid = num_len//2
        if num_len%2 == 0: 
            return (nums3[mid] + nums3[mid-1]) / 2
        return nums3[mid]