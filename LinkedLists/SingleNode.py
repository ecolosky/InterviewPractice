class SingleNode:
    def __init__(self, data):
        self.val = data
        self.next = None

    def append(root,data):
        end = SingleNode(data)
        itr = root
        while(itr.next != None):
            itr = itr.next
        itr.next = end
