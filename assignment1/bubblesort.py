from itertools import islice
import time


file_name = 'rand.txt'

def bubble_sort(numberlist):

    start = time.time()

    size = len(numberlist)
    for i in range(size-1):
        count = 0
        for j in range(0,size-i-1):
            
            if numberlist[j] > numberlist[j+1]:
                numberlist[j], numberlist[j+1] = numberlist[j+1], numberlist[j]
                count = count + 1
        print("times:", i)
        if count == 0:
                break
        #time at the end of program execution is noted
    end = time.time()
  
    #total time taken to print the file
    print("Execution time in seconds: ",(end - start))

    # print(numberlist)

def bubble_sort_op1(numberlist):

    start = time.time()

    size = len(numberlist)
    for i in range(size-1):
        flag = 0

        for j in range(0,size-flag-1):
            if numberlist[j] > numberlist[j+1]:
                numberlist[j], numberlist[j+1] = numberlist[j+1], numberlist[j]
                flag=j
        
        print("times:", i)
        
        if flag == 0:
                break
        #time at the end of program execution is noted
    end = time.time()
  
    #total time taken to print the file
    print("Execution time in seconds: ",(end - start))


def bubble_sort_op2(numberlist):

    start = time.time()

    size = len(numberlist)

    up = size -1
    down = 0
    flag = -1

    while True:
       
        for j in range(down,up):
            if numberlist[j] > numberlist[j+1]:
                numberlist[j], numberlist[j+1] = numberlist[j+1], numberlist[j]
                flag=j
        
        if flag == -1:
                break
        
        up = flag
        flag = -1

        for k in range(up, down, -1):
            if numberlist[k] < numberlist[k-1]:
                numberlist[k], numberlist[k-1] = numberlist[k-1], numberlist[k]
                flag=k
        
        if flag == -1:
                break

        down = flag
        flag = -1

        print("down:", down, "up:", up)

        #time at the end of program execution is noted
    end = time.time()
  
    #total time taken to print the file
    print("Execution time in seconds: ",(end - start))

    print(numberlist)


def readdata():
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


def main():
    # data = [9,7,10,14,3,5,1,22,7]
    data = readdata()
    bubble_sort_op2(data)


if __name__ == "__main__":
    main()