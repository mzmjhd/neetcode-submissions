class Solution:
    def trap(self, height: List[int]) -> int:
        prefMax = [0]*len(height)
        sufMax = [0]*len(height)
        max_vol = 0
        for l in range(len(height)):
            if l == 0:
                prefMax[l] = 0
            else:
                prefMax[l] = max(height[l-1], prefMax[l-1])
        for r in range(len(height)-1, -1, -1):
            if r == len(height)-1:
                sufMax[r] = 0
            else:
                sufMax[r] = max(height[r+1], sufMax[r+1])

        for n in range(len(height)):
            max_vol += max(min(prefMax[n],sufMax[n])-height[n],0)

        return max_vol