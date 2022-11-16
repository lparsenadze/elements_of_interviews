
def remove_kth(head, k):
    dummy = head
    p1 =  p2 = head
    for _ in range(k):
        p2 = p2.next
    while p2 and p2.next: #(!)
        p1 = p1.next
        p2 = p2.next
    p1.next = p1.next.next
    return dummy
