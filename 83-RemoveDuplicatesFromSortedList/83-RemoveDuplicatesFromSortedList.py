# Last updated: 23/07/2026, 11:00:17
class Solution:
    def deleteDuplicates(self, head):
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Skip duplicate
                current.next = current.next.next
            else:
                current = current.next
        
        return head