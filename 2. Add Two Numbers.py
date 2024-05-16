def addTwoNumbers(self, l1, l2):
    l3 = ListNode(0)
    curr = l3
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        l1val = l1.val if l1 else 0
        l2val = l2.val if l2 else 0
        sumnode = l1val + l2val + carry
        carry = sumnode // 10
        newNode = ListNode(sumnode%10)
        curr.next = newNode
        curr = newNode
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return l3.next