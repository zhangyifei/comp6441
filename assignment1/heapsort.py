

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

def heap_adjust(list, start, end):
    temp = list[start]

    i = start
    j = 2*i

    while j <= end:
        if (j < end) and (list[j]<list[j+1]):
            j += 1
        if temp < list[j]:
            list[i]= list[j]
            i = j
            j = 2 * i
        else:
            break
    list[i] = temp
    

def heap_sort(list):

    start = time.time()

    list_length = len(list)-1

    first_sort_count =  int(list_length / 2)

    for i in range(first_sort_count):
        heap_adjust(list, first_sort_count - i, list_length)

    for i in range(list_length - 1):
        list = swap_param(list, 1, list_length-i)
        heap_adjust(list, 1, list_length-i-1)

    end = time.time()
    print("Execution time in seconds: ",(end - start))
    print("No. of lines sorted: ",len(list))

def main():
    # data = [9,7,10,14,3,5,1,22,12]
    data = readdata()
    data.insert(0,0)

    heap_sort(data)


if __name__ == "__main__":
    main()