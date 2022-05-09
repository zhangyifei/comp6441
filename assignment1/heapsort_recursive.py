

from collections import deque
from itertools import islice
import time


def readdata():
    file_name = 'rand.txt'


    data = []

    #time at the start of program is noted
    start = time.time()
  
    #keeps a track of number of lines in the file
    with open(file_name, mode='r') as datafile:
        while True:
            next_n_lines = list(islice(datafile, 10000))
            if not next_n_lines:
                break
            data.extend([int(line.rstrip()) for line in next_n_lines])
      
    #time at the end of program execution is noted
    end = time.time()
  
    #total time taken to print the file
    print("Execution time in seconds: ",(end - start))
    print("No. of lines printed: ",len(data))
    return data

def swap_param(list, i, j):
    list[i], list[j] = list[j], list[i]
    return list

def heapify(arr:list, n:int, i:int):
    if i >= n:
        return

    largest = i
    lchild = i*2+1
    rchild = i*2+2

    if lchild < n and arr[lchild] > arr[largest]:
        largest = lchild
    
    if rchild < n and arr[rchild] > arr[largest]:
        largest = rchild

    if largest != i:
        swap_param(arr, i, largest)
        heapify(arr,n, largest)

def heap_sort(arr:list):
    start = time.time()

    n= len(arr)

    for i in range (n, -1, -1):
        heapify(arr, n, i)

    for i in range (n-1, 0, -1):
        swap_param(arr, 0, i)
        heapify(arr, i, 0)

    end = time.time()
    print("Execution time in seconds: ",(end - start))
    print("No. of lines sorted: ",len(arr))

def main():
    # data = [9,7,10,14,3,5,1,22,12]
    data = readdata()

    heap_sort(data)

    # print(data)


if __name__ == "__main__":
    main()