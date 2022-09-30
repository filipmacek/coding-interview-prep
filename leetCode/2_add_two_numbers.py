"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
"""
I had some problems here because I implemented this with arrays in python.
But linked list is not array!
Especially in python implementation, you have to be carefull becase Pyhton is pass-by-object-reference language

"""


class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        ### Lets and __repr__ method so its easier to debug
        return f"ListNode(val={self.val},next={self.next})"

def list_to_ListNode(array)->ListNode:
    if len(array)<0:return None
    if len(array)==1:
        return ListNode(array[0])
    return ListNode(array[0],next=list_to_ListNode(array[1:]))

class Solution(object):
    def addTwoNumbers(self, l1:ListNode,l2:ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.elegant(l1,l2)

    def elegant(self,l1:ListNode,l2:ListNode):
        res = ListNode()
        current = res
        carry = 0
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            value = value1+value2+carry
            carry = value//10
            value = value%10
            current.next = ListNode(value)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next


    def simple(self,l1,l2):
        res = ListNode()
        curr = 0
        iterator = res
        while True:
            num_res = l1.val+l2.val+curr
            if num_res <=9:
                iterator.val = num_res
                curr = 0
            else:
                val = num_res%10
                iterator.val = val
                curr = num_res//10
            l1 = l1.next
            l2 = l2.next
            if l1 is None and l2 is None:
                iterator.val = iterator.val+curr
                iterator = None
                break
            if l1 is None and l2 is not None:
                l1 = ListNode()
            if l2 is None and l1 is not None:
                l2 = ListNode()
            iterator.next = ListNode()
            iterator = iterator.next

        return res



if __name__ == '__main__':
    l1_list = [2,4,3]
    l1 = list_to_ListNode(l1_list)
    l2_list = [5,6,4]
    l2 = list_to_ListNode(l2_list)
    result = [7,0,8]
    # l1 = list_to_ListNode([9, 9, 9, 9, 9, 9, 9])
    # l2 = list_to_ListNode([9, 9, 9, 9])
    print(Solution().addTwoNumbers(l1,l2))
