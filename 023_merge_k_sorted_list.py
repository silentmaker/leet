# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def mergeKLists(self, lists):
#         # lists: List[ListNode]
#         # example testing: [[1,2,3],[3,3,6]] => [1,2,3,3,3,6]
#         result = []
#         minium = 'MAX'
#         min_index = 'M_INDEX'
#         count = 0
#         i = 0
#         k = len(lists)
#         if k == 0:
#             return lists
#         else:
#             while True:
#                 if lists[i] == None:
#                     count = count + 1
#                 elif lists[i].val < minium:
#                     minium = lists[i].val
#                     min_index = i           
#                 if count == k:
#                     break
#                 if i + 1 == k:
#                     i = 0
#                     if min_index != 'M_INDEX':
#                         lists[min_index] = lists[min_index].next
#                     result.append(minium)
#                     minium = 'MAX'
#                     min_index = 'M_INDEX'
#                     count = 0
#                 else:
#                     i = i + 1
#         return result

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