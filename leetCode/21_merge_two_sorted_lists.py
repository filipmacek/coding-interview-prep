"""
---
title: Merge Two Sorted Lists
number: 21
difficulty: easy
tags: ['Linked List','Recursion']
solved: true
---
"""

from typing import Optional

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.simple_splice(list1,list2)

    def simple_splice(self,list1:ListNode,list2:ListNode):
        res = ListNode()
        current = res
        while list1 and list1:
            if list1 is None and list2 is not None:
                current.next = list2
                list2 = list2.next
            elif list2 is None and list1 is not None:
                current.next = list1
                list1 = list1.next
            elif  list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next =list1
        elif list2:
            current.next = list2

        return res.next

    def simple(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """This solution is good but we are creating nodes from new elements instead of from target. we need to splice"""
        res = ListNode()
        current = res
        while list1 or list2:
            v1 = list1.val if list1 else None
            v2 = list2.val if list2 else None
            if v1 is None and v2 is not None:
                current.next = ListNode(v2)
                list2 = list2.next if list2 else None
            elif v2 is None and v1 is not None:
                current.next = ListNode(v1)
                list1 = list1.next if list1 else None
            elif v1 == v2:
                current.next = ListNode(v1)
                list1 = list1.next
            elif v1 < v2:
                current.next = ListNode(v1)
                list1 = list1.next
            else:
                current.next = ListNode(v2)
                list2 = list2.next
            current = current.next
        return res.next
if __name__ == '__main__':
    list1 = [1]
    l1 = list_to_ListNode(list1)
    list2 = [2]
    l2 = list_to_ListNode(list2)
    print(Solution().mergeTwoLists(l1,l2))
