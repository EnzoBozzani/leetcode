class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None: return None
            
        current: ListNode | None = head
        previous: ListNode | None = None

        while (current is not None):
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous


if __name__ == '__main__':
    solution = Solution()
                        
    examples = []

    for e in examples:
        print(e)
        print(solution.func(e))    
        print()                      

