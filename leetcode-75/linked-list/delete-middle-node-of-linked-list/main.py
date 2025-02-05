class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next

class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        current: ListNode | None = head
        middle: ListNode | None = head
        previous_middle: ListNode | None = None
        length = 0
        middle_index = 0

        while (current is not None):
            current = current.next

            if middle_index < length / 2:
                middle_index += 1
                previous_middle = middle
                middle = middle.next

            length += 1

        if middle_index == 0: return None

        previous_middle.next = middle.next

        return head



if __name__ == '__main__':
    solution = Solution()

    a = [1,3,4,7,1,2,6]

    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(7)
    node5 = ListNode(1)
    node6 = ListNode(2)
    node7 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    print(solution.deleteMiddle(node1))    
    print()                      

