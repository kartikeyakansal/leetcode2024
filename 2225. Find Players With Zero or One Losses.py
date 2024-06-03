class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        temp1, temp2 = [], []
        losses = {}
        for i in matches:
            if i[0] not in losses:
                losses[i[0]] = 0
            if i[1] not in losses:
                losses[i[1]] = 1
            else:
                losses[i[1]] += 1
        for key, value in losses.items():
            if value == 0:
                temp1.append(key)
            elif value == 1:
                temp2.append(key)
        ans.append(sorted(temp1))
        ans.append(sorted(temp2))
        return ans
