class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next
        
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        length = 0

        current = head

        while (current is not None):
            current = current.next
            length += 1

        current = head
        max_sum = 0

        first_half = {}

        i = 0

        while (current is not None):
            if i <= (length / 2) - 1:
                first_half[i] = current.val
            else:
                s = first_half[length - 1 - i] + current.val
                if s > max_sum:
                    max_sum = s
            
            i += 1
            current = current.next
        
        return max_sum
            


if __name__ == '__main__':
    solution = Solution()
                        
    node1 = ListNode(5)
    node2 = ListNode(4)
    node3 = ListNode(2)
    node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(solution.pairSum(node1))    
    print()                      

