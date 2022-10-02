"""
---
title: Merge K Sorted lists
number: 23
difficulty: hard
tags: ['Linked List','Divide and conquer','Heap (Priority Queue)','Merge Sort']
solved: true
---
"""


"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

"""
from typing import List, Optional

"""
This is such a good example of merge sort,linkedlist and recursion!!!

"""


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.simple(lists)


    def simple(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.merge_lists(l1,l2))
            lists = mergedLists
        return lists[0]

    def merge_lists(self,a:ListNode,b:ListNode):
        result = None
        if a == None:return b
        if b==None: return a

        if a.val <= b.val:
            result = a
            result.next = self.merge_lists(a.next,b)
        else:
            result = b
            result.next = self.merge_lists(a,b.next)
        return result


if __name__ == '__main__':
    lists = [list_to_ListNode([1, 4, 5]), list_to_ListNode([1, 3, 4]), list_to_ListNode([2, 6])]
    print(Solution().mergeKLists(lists))



