# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Find the middle node first using slow and fast pointers
        Reverse the second half then we merge them based on the flip
        boolean
        '''
        slow, fast = head, head
        middle = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # found the middle node
        # fast is now pointing to the last element
        second_half = slow.next
        slow.next = None # cut off the second half
        curr = second_half
        last = None
        while curr:
            next_node = curr.next
            curr.next = last
            last = curr
            curr = next_node
        #last is now the end of the linked list
        flip = False
        dummy = ListNode()
        curr = dummy
        while head and last:
            if flip:
                curr.next = last
                last = last.next
                flip = False
                curr = curr.next
            else:
                curr.next = head
                head = head.next
                flip = True
                curr = curr.next
        if head:
            curr.next = head
        if last:
            curr.next = last
        

        
        