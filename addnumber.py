  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        ret = 0
        tant que n1 is not none and n2 is not none:
            d = n1.val + n2.val + ret
            si d > 10
            ret = 1
            d -= 10
            
        trouver quel n est pas none
        tant que n pas none
            d = ret + n.val
        """
        res = ListNode(0)
        ptcur = res
        ret = 0
        # process each digit and carry
        while l1 is not None and l2 is not None:
            d = l1.val + l2.val + ret
            ret = 0
            if d >= 10:
                ret = 1
                d -= 10
            ptcur.next = ListNode(d)
            ptcur = ptcur.next
            l1 = l1.next
            l2 = l2.next
            
        # check if there was a number bigger than the other
        if l1 is None and l2 is not None:
            n = l2
        elif l2 is None and l1 is not None:
            n = l1
        else:  
            # we're done. check carry and return
            if ret == 1:
                ptcur.next = ListNode(1)
                ptcur = ptcur.next
                ret = 0
            return res.next
        
        while n is not None:
            d = n.val + ret
            ret = 0
            # check the carry
            if d >= 10:
                ret = 1
                d -= 10
            ptcur.next = ListNode(d)
            ptcur = ptcur.next
            n = n.next
            
        # check the final carry before return
        if ret == 1:
            ptcur.next = ListNode(1)
            ptcur = ptcur.next
            ret = 0   
            
            
        return res.next
