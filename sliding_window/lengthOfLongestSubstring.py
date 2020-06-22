class Solution:
    '''
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:
    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:

        # max_length为最大长度 i 为左区间 j为右区间 往右移动
        max_length, i, j = 0, 0, 0
        # 不重复子字符串集合 字符串s中i索引开始的最大不重复子字符
        new_set = set()
        s_length = len(s)
        while i < s_length and j < s_length:
            if not new_set.__contains__(s[j]):
                #
                new_set.add(s[j])
                # j向右移动1个字符
                j += 1
                # 找到最大的长度
                max_length = max(max_length, j - i)
            else:
                # i索引开始的最大不重复子字符已经被找到,此时max_length记录的是以i索引开始最大不重复子字符的长度
                new_set.remove(s[i])

                # i向右移动1个字符
                i += 1
        return max_length


#  关键点：滑动窗口算法、集合查找数据快
