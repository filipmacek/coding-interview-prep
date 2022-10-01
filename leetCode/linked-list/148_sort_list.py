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
        print("ssa")


    def get_middle(self):


if __name__ == '__main__':
    list = [4,2,1,3]
    l1 = list_to_ListNode(list)
    print(Solution().sortList(l1))
