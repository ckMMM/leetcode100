from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # 滑动窗口 + 哈希表
        # 1.初始化window和need窗口，有效匹配值valid
        window = defaultdict(int)
        need = defaultdict(int)
        valid = 0
        
        # 2. 统计需要的字符
        for item in t:
            need[item] += 1
            
        res_left = 0
        min_len = float('inf') 
        left = 0

        # 3. 遍历 s
        for right, item in enumerate(s):
            # 入：扩大窗口
            if item in need:
                window[item] += 1
                if window[item] == need[item]:
                    valid += 1
                
            # 出：当窗口完全覆盖 t 时，尝试收缩
            while valid == len(need):
                # 判断是否需要更新最小长度
                if right - left + 1 < min_len:
                    min_len = right - left + 1 
                    res_left = left 

                # 移除左侧字符
                temp = s[left]
                if temp in need:
                    window[temp] -= 1
                    if window[temp] < need[temp]: 
                        valid -= 1
                left += 1
                
        # 4. 返回结果，如果 min_len 没变过，说明没找到
        return "" if min_len == float('inf') else s[res_left : res_left + min_len]
