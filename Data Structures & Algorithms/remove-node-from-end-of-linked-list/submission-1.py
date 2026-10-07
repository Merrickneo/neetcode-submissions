# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Could store the position of each node then do the manipulation
        # return the node in the head position
        node_dict = dict()
        curr = head
        count = 0
        while curr:
            count += 1
            node_dict[count] = curr
            curr = curr.next
        # position to remove
        # get the prev and next positions

        '''
        1. First Node
        - Return next node
        2. Middle Node
        - Prev point to next and return head
        3. End Node
        - second last node remove last node
        '''
        position = count - n + 1
        if position == 1:
            return node_dict.get(position + 1, None)
        elif position == count:
            node_dict.get(position - 1).next = None
        else:
            prev = node_dict.get(position - 1, None)
            after = node_dict.get(position + 1, None)
            prev.next = after
        return head
        

        