from Node import Node
NULL = None
# ================== remove duplicates ======================================
def removeDups(root):
    anchor = root

    # move anchor pointer
    while anchor.next != NULL:
        cmp = anchor.next

        # iterate compare pointer
        while cmp != NULL:
            if cmp.val == anchor.val:

                # pinch node out of list
                next = cmp.next
                prev = cmp.prev

                # corner case of begining or end of list
                if(next != NULL):
                    next.prev = prev
                if(prev != NULL):
                    prev.next = next
            cmp = cmp.next
        anchor = anchor.next
        # corner case if removing last node from position n-1
        if anchor == NULL:
            return 0

# =================== main ==================================================
root = Node(9)
root.append(9)
root.append(4)
root.append(3)
root.append(4)
root.append(2)
root.append(2)

# before algorithm run
print "Before Test:"
n = root
while n != NULL:
    print n.val
    n = n.next

removeDups(root)

# after algorithm run
print "After Test:"
n = root
while n != NULL:
    print n.val
    n = n.next
