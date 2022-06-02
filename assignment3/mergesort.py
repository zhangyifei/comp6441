
from itertools import islice
import sys
import time
import math
from unittest import result
from linkedList import LinkedList, Node

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True  

def is_even(n: int) -> bool:
    return (n % 2) == 0

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

    ll_uo = LinkedList()
    ll_ue = LinkedList()
    ll_po = LinkedList()
    ll_pe = LinkedList()

    for d in data:
        prime = is_prime(d)
        even = is_even(d)

        if even and prime:
            ll_pe.append(d)
        elif even and (not prime):
            ll_ue.append(d)
        elif (not even) and prime:
            ll_po.append(d)
        else:
            ll_uo.append(d)

    return ll_uo, ll_ue, ll_po, ll_pe
    
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
    lists = readdata()
    print(lists[0].count)
    print(lists[1].count)
    print(lists[2].count)
    print(lists[3].count)

    
    result = None
    count = 0
    for i in range (0, len(lists)):
        node = LinkedList.mergeSort(lists[i].head)
        count += lists[i].count
        result= LinkedList.sortedMerge(result, lists[i].head)

    end = time.time()
    printList(result)
    print("Execution time in seconds: ",(end - start))
    print("No. of lines sorted: ", count)


