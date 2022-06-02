
from itertools import islice
import sys
import time
from linkedList import LinkedList


def readdata():
    file_name = 'rand.txt'
    data = []
  
    #keeps a track of number of lines in the file
    with open(file_name, mode='r') as datafile:
        while True:
            next_n_lines = list(islice(datafile, 10000))
            if not next_n_lines:
                break
            data.extend([int(line.rstrip()) for line in next_n_lines])

    ll = LinkedList()

    for d in data:
        ll.append(d)

    return ll
    
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print(' ')




if __name__ == '__main__':

    sys.setrecursionlimit(1000000)    # adjust numbers for recursion

    #time at the start of program is noted
    start = time.time()
    list = readdata()
    print(list.count)

    list.mergeSort(list.head)
    #time at the end of program execution is noted
    end = time.time()
    printList(list.head)
    print("Execution time in seconds: ",(end - start))
    print("No. of lines sorted: ",list.count)


