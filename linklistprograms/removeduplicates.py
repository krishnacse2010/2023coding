from linklist import LinkedList
from typing import List, Optional
class Solution:
    def deleteDuplicates(self, head: Optional[LinkedList]) -> Optional[LinkedList]:
        if head is None:
            return
        t1=t2= head
        
        while t2.next:
            t2=t2.next
            if t2.val == t1.val:
                
                if t2.next is None:
                    t1.next = None
                    break

            else:
                t1.next = t2
                t1=t2
                
        return head

    def deleteDuplicates_betterapproach(self, head: Optional[LinkedList]) -> Optional[LinkedList]:
        t1 = t2 = head
        t2 = t1.next

        while t2:
            if t2.val == t1.val:
                t1.next = t2.next
                t2= t2.next
            else:
                t1=t1.next
                t2=t2.next
                
        return head
l1=LinkedList()
list1 = [1,1,2,3,3,4,5]
for elem in list1:
    l1.append(elem)

s=Solution()
s.deleteDuplicates_betterapproach(l1.head)
l1.print_list()