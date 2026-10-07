class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        size = 1
        arr = []
        for j in range(len(s)):
            if s[j] not in arr:
                arr.append(s[j])
                size = max(size,len(arr))
            else:
                cut = arr.index(s[j])
                arr = arr[cut+1:]
                arr.append(s[j])
        return size