class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intv = sorted(intervals)
        ans = [intv[0]]
        for i in range(1,len(intv)):
            if intv[i][0] <= ans[-1][1]  :
                ans[-1][1] = max(ans[-1][1],intv[i][1])
            else:
                ans.append(intv[i])
        return ans