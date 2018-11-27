def removeDuplicates(head):
    temp = head
    i = 0
    while (temp.next):
        prev = temp
        temp = temp.next
    
        while(True):
            print('Iteration: {}, Prev: {}, temp: {}'.format(i, prev.data, temp.data))
            if(prev.data == temp.data):
                prev.next = temp.next
                if(temp.next):
                    temp = temp.next
                else:
                    break
            else:
                break

        i += 1
    return head