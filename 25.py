# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        right = head
        def reverse(arr):
            l = 0
            r = len(arr) - 1
            while l < r:
                arr[l],arr[r] = arr[r], arr[l]
                l += 1
                r -=1
    
        while True:
            # move right k steps ahead
            elems = []
            s = k
            while s:
                elems.append(right.val)
                if not right.next:
                  if s-1 == 0:
                    break
                  else:
                     return head 
                right = right.next
                s -= 1
            
            reverse(elems)
            for num in elems:
                left.val = num
                if (left.next == None):
                  return head
                left = left.next
            
        return head
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print(Solution().reverseKGroup(head, 3))