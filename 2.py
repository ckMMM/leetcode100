from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #如何找字母异位词：sorted()
        #如何分类放在不同的列表里(使用字典)："异位词" ：列表
        #因为遍历过程中采用d[异位词].append() 而不是d[异位词] = 列表
        #所以数据结构使用 defaultdict(list) 创建一个默认值为列表的字典

        # 1.初始化字典
        d = defaultdict(list)

        # 2.遍历输入字符串列表，存放字典中
        for s in strs:
            signature = "".join(sorted(s))
            d[signature].append(s)

        # 3.获取字典中的值(即分类完的列表)
        return list(d.values())
