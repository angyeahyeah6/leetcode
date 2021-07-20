# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        end = ListNode(0, head)
        current = head
        cnt = 0
        new_head = None
        last = None
        if head.next == None:
            return head
        while end.next != None or (end.next == None and cnt == k):
            if cnt == k:
                prev = None
                ## reverse the list
                while cnt > 0:
                    temp = current.next
                    current.next = prev
                    prev = current
                    current = temp
                    cnt -= 1
                ## find the very first head
                if new_head == None:
                    new_head = prev
                ## previous revers list to point to new reverse list
                if last != None:
                    last.next = prev
                last = prev
                for i in range(k-1):
                    last = last.next
                ## current move to the next element
                current = end.next
            # end.next is not none
            else:
                cnt += 1
                end.next = end.next.next
        ## the remain will be concat to the end
        if cnt > 0:
            last.next = current
        return new_head
