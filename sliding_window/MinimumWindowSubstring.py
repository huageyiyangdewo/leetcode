from collections import defaultdict


class Solution:
    '''
    给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

    示例：
    输入: S = "ADOBECODEBANC", T = "ABC"
    输出: "BANC"
    说明：

    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。
    '''

    def minWindow(self, s: str, t: str) -> str:
        # 当前滑动窗口中需要的各元素的数量
        need = defaultdict(int)
        for c in t:
            need[c] += 1

        # 所需元素的总数量
        need_count = len(t)
        i = 0  # 窗口左边界起始值
        res = (0, float('inf'))  # 最小字符串的起止位置坐标
        for index, sub_s in enumerate(s):
            if need[sub_s] > 0:
                need_count -= 1

            need[sub_s] -= 1
            if need_count == 0:  # 窗口包含了所有的t元素
                while True:  # 增加i，排除多余元素
                    # 窗口起始元素
                    sub_s = s[i]
                    if need[sub_s] == 0:  # i与index之间已经包含了所有t元素且i不能再向右移动
                        break

                    need[sub_s] += 1
                    # 窗口起始位置右移
                    i += 1

                if index - i < res[1] - res[0]:
                    res = (i, index)

                # i增加一个位置，寻找新的满足条件滑动窗口
                need[s[i]] += 1
                need_count += 1
                i += 1
        return '' if len(s) < res[1] else s[res[0]: res[1] + 1]


if __name__ == '__main__':
    s = "AABBCC"
    t = "ABC"
    so = Solution()
    ret = so.minWindow(s, t)
    print(ret)

