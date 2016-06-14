from SingleNode import SingleNode

# ============ find the kth to last node ======================================
def kthToLast(node, k):
    # reached the end of ther list
    if(node == None):
        return (None,k)
    else:
        (rtnNode, rtnK) = kthToLast(node.next, k)
        if(rtnK == 0):
            return (node ,-1)
        else:
            return (rtnNode,rtnK-1)
# ============ Delete the middle node =========================================
def DelMidNode(node):
    current = node
    next = node.next
    prev = None
    while(next != None):
        current.val = next.val
        prev = current
        current = next
        next = next.next
    prev.next = None
# ========== partition a list based on a value ================================
def partition(root, k):
    tailGreater = None
    headGreater = None
    tailLesser = None
    headLesser = None
    itr = root
    while(itr != None):
        if(itr.val < k):
            if(headLesser == None):
                tailLesser = SingleNode(itr.val)
                headLesser = tailLesser
                tailLesser.next = None
            else:
                tailLesser.next = SingleNode(itr.val)
                tailLesser = tailLesser.next
                tailLesser.next = None
        elif(itr.val >= k):
            if(headGreater == None):
                tailGreater = SingleNode(itr.val)
                headGreater = tailGreater
                tailGreater.next = None
            else:
                tailGreater.next = SingleNode(itr.val)
                tailGreater = tailGreater.next
                tailGreater.next = None
        itr = itr.next
    tailLesser.next = headGreater
    return headLesser


# =================================== main ====================================
root = SingleNode(3)
root.append(1)
root.append(0)
root.append(2)
root.append(4)

print "Before Test:"
itr = root
while(itr != None):
    print itr.val
    itr = itr.next

# (node, k) = kthToLast(root, 0)
# print "Result:"
# print node.val
# node = root.next.next
# DelMidNode(node)
root = partition(root, 2)


print "After Test:"
itr = root
while(itr != None):
    print itr.val
    itr = itr.next
