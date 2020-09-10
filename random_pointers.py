  """
        go through the list and add copies in between.
        """
        node = head
        while node:
            oldnext = node.next
            newNode = Node(node.val, next= oldnext, random=None)
            node.next = newNode
            node = oldnext
        
        """
        fix random pointers
        """
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
            
            
        # we have a copy
        ret = Node(0)
        headret = ret      
        node = head
        while node:
            ret.next = node.next
            ret = ret.next
            node = node.next.next
            
        return headret.next
