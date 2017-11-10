"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
两个非空链表，表示两个非负整数。数字由低位到高位存储，每个节点包含一个数字，将这两个数字相加并将其作为链表返回。除了数字0本身，两个数字不包含前导零。

exp:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
"""
def addTwoNumber(flag,l1,l2):
    """
    flag表示进位。
    需要特别注意两个数的位数不相等这种情况。
    对较短的数补0节点。
    """
    if sum < 10:
        i = 0
    else:
        sum -= 10
        i = 1
        n = ListNode(sum)
        if l1.next == None and l2.next == None and i ==0:
            n.next = None
        elif l1.next == None and l2.next == None and i == 1:
            n.next = ListNode(1)
        else:
            a = l1.next if l1.next != None else ListNode(0)
            b = l2.next if l2.next != None else ListNode(0)
            n,.next = add(i,a,b)
        return n

