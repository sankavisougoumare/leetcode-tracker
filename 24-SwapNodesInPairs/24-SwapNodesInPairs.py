# Last updated: 23/07/2026, 11:00:35
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev forward
            prev = first
        
        return dummy.next