 ptr1 = l1
        ptr2 = l2
        head_dummy = ListNode(0)
        ptr_head = head_dummy
        end = False
        ptr = None
        
        if ptr1 is None and ptr2 is None:
            end = True
                
        while not end:
            # to cover : if both are none
            if ptr2 is None:
                ptr = ptr1
                ptr1 = ptr1.next
            elif ptr1 is None:
                ptr = ptr2
                ptr2 = ptr2.next
            elif ptr1.val < ptr2.val:
                ptr = ptr1
                ptr1 = ptr1.next
            elif ptr1.val >= ptr2.val:
                ptr = ptr2
                ptr2 = ptr2.next
               
            ptr_head.next = ListNode(ptr.val)
            ptr_head = ptr_head.next
            
            if ptr1 is None and ptr2 is None:
                end = True
                
        return head_dummy.next  
