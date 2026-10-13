class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = -1
        for i in range(-2, -len(nums)-1, -1):
            if i+nums[i] >= dest:
                dest = i
        return (dest == -len(nums))