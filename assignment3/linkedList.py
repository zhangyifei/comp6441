class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append(self, new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        
        curr_node = self.tail

        curr_node.next = new_node

        self.tail = curr_node.next

        self.count += 1


    def sortedMerge(self, a:Node , b:Node):

        result = None

        if a == None:
            return b
        if b == None:
            return a
        
        if a.data < b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)

        return result


    def getMiddle(self, head:Node):
        if head == None:
            return head
        
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def mergeSort(self, h:Node):

        if h == None or h.next == None:
            return h

        
        middle = self.getMiddle(h)

        nextMiddle =  middle.next
        middle.next = None

        left = self.mergeSort(h)

        right = self.mergeSort(nextMiddle)

        sortedlist = self.sortedMerge(left, right)

        return sortedlist