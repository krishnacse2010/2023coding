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

l1=LinkedList()
list1 = [1,1,2,2,3,4]
for elem in list1:
    l1.append(elem)

s=Solution()
s.deleteDuplicates(l1.head)
print(l1.print_list())