class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    right_head = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(right_head)

    dummy = ListNode(0)
    cur = dummy

    while left and right:
        if left.val < right.val:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next

        cur = cur.next

    if left:
        cur.next = left

    if right:
        cur.next = right

    return dummy.next


if __name__ == '__main__':
    l = [6, 4.2]
    dummy = ListNode(0)
    cur = dummy
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next


    head = sortList(dummy.next)

    while head:
        print head.val
        head = head.next
