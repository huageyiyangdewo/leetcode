class ListNode(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class Solution:
    '''
    92题
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
    说明:
    1 ≤ m ≤ n ≤ 链表长度。

    示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL

    '''

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n <= m:
            return head
        # 计算需要反转的节点个数
        change_count = n - m + 1
        # 第一个反转节点的前驱
        pre_head = None
        # 反转后链表的头结点
        ret_head = head

        # 找到开始反转的第一个节点,移动change_count-1个节点
        while m > 1:
            pre_head = head
            head = head.next
            m -= 1

        # 存储开始反转的第一个节点，反转后为尾节点
        modify_tail = head

        # 反转m到n之间的节点
        # 反转节点的头结点
        new_head = None
        while head and change_count:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
            change_count -= 1

        modify_tail.next = head
        if pre_head:
            # 不是从链表第一个节点开始反转，即m>1
            pre_head.next = new_head
        else:
            ret_head = new_head
        return ret_head


def travel_link_list(head):
    '''遍历链表'''
    while head:
        if head.next is not None:
            print(head.item, end='->')
        else:
            print(head.item)

        head = head.next


if __name__ == '__main__':
    s1 = ListNode(1)
    s2 = ListNode(2)
    s3 = ListNode(3)
    s4 = ListNode(4)
    s5 = ListNode(5)

    s1.next = s2
    s2.next = s3
    s3.next = s4
    s4.next = s5

    travel_link_list(s1)

    so = Solution()
    ret = so.reverseBetween(s1, 4, 5)
    travel_link_list(ret)

