"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""
from typing import Optional

"""
Get helper function that converts array to ListNode for debugging
- How to find the middle of linkedlist - two pointer techniques?
- Then recursion
"""

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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)


    def merge_sort(self,list:ListNode):
        # This is recursive
        if not list or not list.next:
            return list
        left = list
        right = self.get_middle(list)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left,right)

    def merge(self,left:ListNode,right:ListNode)->ListNode:
        result = None
        if left == None:
            return right
        if right == None:
            return left

        if left.val <= right.val:
            result = left
            result.next = self.merge(left.next,right)
        else:
            result = right
            result.next = self.merge(right.next,left)
        return result



    def get_middle(self,list:ListNode):
        slow = list
        fast = list.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

if __name__ == '__main__':
    list = [4,2,1,3]
    l1 = list_to_ListNode(list)
    print(Solution().sortList(l1))
