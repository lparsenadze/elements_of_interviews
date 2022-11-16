class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def test_cyclicity(head):
    def cycle_len(cycle_node):
        count = 0
        pointer = cycle_node
        while True:
            count += 1
            pointer = pointer.next
            if pointer is cycle_node:
                return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            c_len = cycle_len(slow)
            cycle_len_iterator = head
            for _ in range(c_len):
                cycle_len_iterator = cycle_len_iterator.next
                
            it = head
            while it is not cycle_len_iterator:
                it = it.next
                cycle_len_iterator = cycle_len_iterator.next
            return it
        return None



def test_cyclicity_2A(head):
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    if fast is slow:
        it = head
        while it is not slow:
            slow = slow.next
            it = it.next
        return it
   return None  


        
