class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        current1 = l1
        current2 = l2

        current_sum = 0
        current_remainder = 0
        prev_remainder = 0

        if current1 is not None:
            current_sum += current1.val
            current1 = current1.next
        if current2 is not None:
            current_sum += current2.val
            current2 = current2.next
        
        prev_remainder = current_remainder

        if current_sum > 9:
            current_sum = current_sum - 10
            current_remainder = 1
        else:
            current_remainder = 0

        if current_sum + prev_remainder > 9:
            prev_remainder = current_remainder
            current_sum = 0
            current_remainder = 1

        head = ListNode(current_sum + prev_remainder)
        current = head
        nxt = None

        current_sum = 0

        while (current1 is not None or current2 is not None):
            if current1 is not None:
                current_sum += current1.val
                current1 = current1.next
            if current2 is not None:
                current_sum += current2.val
                current2 = current2.next
            
            prev_remainder = current_remainder

            if current_sum > 9:
                current_sum = current_sum - 10
                current_remainder = 1
            else:
                current_remainder = 0

            if current_sum + prev_remainder > 9:
                prev_remainder = current_remainder
                current_sum = 0
                current_remainder = 1

            nxt = ListNode(current_sum + prev_remainder)
            current.next = nxt
            current = nxt

            current_sum = 0

        if current_remainder == 1:
            nxt = ListNode(current_remainder)
            current.next = nxt
            current = nxt

        return head

def list_to_head(l: list[int]):
    head = ListNode(l[0])

    current = head
    nxt = None
    for i in range(len(l)):
        if i != 0:
            nxt = ListNode(l[i])
            current.next = nxt
            current = nxt

    return head

def print_list(h: ListNode):
    c = h

    while c is not None:
        print(c.val, end=" ")
        c = c.next
    
    print()


if __name__ == '__main__':
    solution = Solution()

    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    head1 = list_to_head(l1)
    
    head2 = list_to_head(l2)

    print_list(head1)
    print_list(head2)

    c = solution.addTwoNumbers(head1, head2)    

    print_list(c)




