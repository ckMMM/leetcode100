from typing import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # 滑动窗口
        # 1.Counter()记录
        res = []
        cnt_s = Counter()
        cnt_p = Counter(p)

        # 2.遍历
        for right in range(len(s)):
            # 入
            cnt_s[s[right]] += 1
            left = right - len(p) + 1
            if left < 0:
                continue
            
            # 更新
            if(cnt_s == cnt_p):
                res.append(left)

            # 出
            cnt_s[s[left]] -= 1
            if cnt_s[s[left]] == 0:
                del cnt_s[s[left]]

        # 3.返回结果
        return res