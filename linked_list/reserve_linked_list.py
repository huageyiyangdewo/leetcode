class ListNode(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            # 备份当前节点next
            temp = head.next
            # 改变head节点的next
            head.next = new_head
            # 移动new_head
            new_head = head
            head = temp

        return new_head


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
    ret = so.reverseList(s1)
    travel_link_list(ret)

