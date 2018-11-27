def deleteNode(head, position):

    if position == 0:
        head = head.next
        return head

    temp = head
    while position:
        position -= 1
        prev = temp
        temp = temp.next
    
    prev.next = temp.next
    
    return head