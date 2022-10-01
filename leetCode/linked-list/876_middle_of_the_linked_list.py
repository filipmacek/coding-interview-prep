"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __repr__(self):
        ### Lets and __repr__ method so its easier to debug
        return f"ListNode(val={self.val},next={self.next})"


def list_to_ListNode(array)->ListNode:
    if len(array)==0:return None
    if len(array)==1:
        return ListNode(array[0])
    return ListNode(array[0],next=list_to_ListNode(array[1:]))


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.two_pointers(head)

    def simple(self,list: ListNode):
        ## transfer to array
        ## WORKS but lets try different method,maybe two pointers, fast and slow
        result = []
        iter = list
        while iter:
            result.append(iter.val)
            iter = iter.next
        return list_to_ListNode(result[len(result)//2:])

    def two_pointers(self,list:ListNode):
        slow = list
        fast = list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    list =  [1,2,3,4,5]
    list1 = [1,2,3,4,5,6]
    l1 = list_to_ListNode(list)
    l2 = list_to_ListNode(list1)
    print(Solution().middleNode(l2))
