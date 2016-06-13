class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None

    def append(self, data):
        end = Node(data)
        n = self
        while(n.next != None):
            n = n.next

        n.next = end
        end.prev = n
