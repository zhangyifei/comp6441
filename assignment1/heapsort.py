from itertools import islice
import sys
import time
import tracemalloc


def readdata():
    file_name = 'rand.txt'

    data = [0]

    with open(file_name, mode='r') as datafile:
        while True:
            next_n_lines = list(islice(datafile, 10000))
            if not next_n_lines:
                break
            data.extend([int(line.rstrip()) for line in next_n_lines])
      
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

    list_length = len(list)-1

    first_sort_count =  int(list_length / 2)

    for i in range(first_sort_count):
        heap_adjust(list, first_sort_count - i, list_length)

    for i in range(list_length - 1):
        list = swap_param(list, 1, list_length-i)
        heap_adjust(list, 1, list_length-i-1)

def main():

    sys.stdout = open('result.txt', 'w')
    
    tracemalloc.start()
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Start time memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    start = time.time()

    data = readdata()
    heap_sort(data)
    data = data[1:]

    current, peak = tracemalloc.get_traced_memory()
    end = time.time()

    print(data)
    print(f"Execution memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    print("Execution time in seconds: ",(end - start))
    print("No. of lines sorted: ",len(data))

if __name__ == "__main__":
    main()