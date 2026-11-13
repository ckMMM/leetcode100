class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashtable = dict()
        res,i = 0,-1
        n = len(s)
        for j in range(n):
            if s[j] in hashtable:
                i = max(hashtable[s[j]],i)
            hashtable[s[j]] = j
            res = max(res,j-i)
        return res

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        # 遇到重复字符更新窗口
        # 1.使用集合判断是否重复
        st = set()
        res = 0
        left = 0

        # 2.遍历
        for right in range(len(s)):
            # 3.出
            while s[right] in st:
                st.remove(s[left])
                left += 1

            # 4.入，更新
            st.add(s[right])
            res = max(res,right - left + 1)

        # 5.返回结果
        return res