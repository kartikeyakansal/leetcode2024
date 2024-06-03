class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_list, t_list = [0]*26, [0]*26
        pos, neg = 0, 0
        for c in s:
            s_list[ord(c)-ord('a')] += 1
        for c in t:
            t_list[ord(c)-ord('a')] += 1
        for i in range(len(s_list)):
            if s_list[i] > t_list[i]:
                neg += s_list[i] - t_list[i]
            elif s_list[i] < t_list[i]:
                pos += t_list[i] - s_list[i]
        
        return max(pos, neg)
