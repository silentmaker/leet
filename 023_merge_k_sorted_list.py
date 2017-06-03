# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# TODO: better solution regardless of python itself

class Solution(object):
    def mergeKLists(self, lists):
        result = []
        count = 0
        i = 0
        k = len(lists)

        if k == 0:
            return lists
        else:
            while True:
                if lists[i] == None:
                    count = count + 1
                else:
                    result.append(lists[i].val)
                    lists[i] = lists[i].next
                
                if count == k:
                    break

                if i + 1 == k:
                    i = 0
                    count = 0
                else:
                    i = i + 1

        return sorted(result)