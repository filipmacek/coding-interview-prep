"""
---
title: Palindrome Linked list
number: 234
difficulty: easy
tags: ['Linked list','Two pointers','Stack','Recursion']
solved: true
---
"""


"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""
from typing import Optional


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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.two_pointers(head)

    def simple(self,head:ListNode)->bool:
        ## lets try with array,then we will do with linkedlists
        array = []
        iter = head
        while iter:
            array.append(iter.val)
            iter = iter.next
        for index in range(len(array)//2):
            if array[index] != array[len(array)-index-1]:
                return False
        return True

    def two_pointers(self,head:ListNode):
        slow = head
        fast = head

        # Find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow =tmp


        # check palindrome with two pointers
        left,right = head,prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return  True


if __name__ == '__main__':
    l1 = list_to_ListNode([1,2,2,1])
    print(Solution().isPalindrome(l1))
