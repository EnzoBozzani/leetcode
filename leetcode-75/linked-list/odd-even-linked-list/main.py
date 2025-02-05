class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next

class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None: return None

        odd = head
        even = head.next
        previous_odd = None
        start_even = even

        while (even is not None and odd is not None):
            previous_odd = odd
            odd.next = even.next if even is not None else None
            odd = odd.next if odd is not None else None
            even.next = odd.next if odd is not None else None
            even = even.next if even is not None else None
        
        if odd is not None:
            odd.next = start_even
        else:
            previous_odd.next = start_even

        return head
        

if __name__ == '__main__':
    solution = Solution()
                        
    examples = []

    for e in examples:
        print(e)
        print(solution.oddEvenList())    
        print()                      

