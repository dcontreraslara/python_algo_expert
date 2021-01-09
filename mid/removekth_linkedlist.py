# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    count = 0

    p1 = head
    p2 = head

    while p1 is not None:
        p1 = p1.next

        if count == k:
            p2 = p2.next
        else:
            count = count + 1

    if count == k:
        if p2 == head:
            head.value = head.next.value
            head.next = head.next.next
        else:
            p1 = head
            while p1.next != p2:
                p1 = p1.next
            p1.next = p1.next.next







