class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def text_overlap(l1, l2):
    def get_len(node):
    tail = node
    count = 0
    while tail:
        tail = tail.next
        count +=1
    return count

    len1 = get_len(l1)
    len2 = get_len(l2)
        
    if len1 > len2:
        l1, l2 = l2, l1

    for _ in range(abs(len1 - len2)):
        l2 = l2.next

    while l1 and l2 and l1 is not l2:
        l1 = l1.next
        l2 = l2.next
    return l1
    
        
    

