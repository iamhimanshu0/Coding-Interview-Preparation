from linked_list import LinkedList


list1 = LinkedList()
list1.append("1")
list1.append("5")
list1.append("7")
list1.append("9")
list1.append("10")

list2 = LinkedList()
list2.append("2")
list2.append("3")
list2.append("4")
list2.append("6")
list2.append("8")


def merge_to_list(list1, list2):
    P = list1.head
    Q = list2.head
    S = None

    if not P:
        return Q

    if not Q:
        return P

    if P and Q:
        if P.data <= Q.data:
            S = P
            P = S.next
        else:
            S = Q
            Q = S.next

        new_head = S

    while P and Q:
        if P.data <= Q.data:
            S.next = P
            S = P
            P = S.next
        else:
            S.next = Q
            S = Q
            Q = S.next

    if not P:
        S.next = Q
    else:
        S.next = P

    return new_head


merge_to_list(list1, list2)
list1.print_list()
