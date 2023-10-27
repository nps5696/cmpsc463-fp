####
# Nikolay Sizov
# nps5696@psu.edu
# CMPSC 463
####

import random
import time

# counter for heapsort switchover
heap_used = False

def introsort(arr):
    # mesaure depth for switching from quicksort to heapsort
    depth = (len(arr).bit_length() -1) * 2
    # route to next step
    introsort_router(arr, 0, len(arr), depth)

def introsort_router(arr, start, end, depth):
    # base cond., single number or lower array => nothing to sort
    if end - start <= 1:
        return
    # if depth is 0 quicksort is no longer quick->(O(n^2)), switching to heapsort
    elif depth == 0:
        global heap_used
        heap_used = True
        do_heapsort(arr, start, end)
    else:
        # let's try to sort it with quicksort
        p = partition(arr, start, end)
        introsort_router(arr, start, p + 1, depth - 1)
        introsort_router(arr, p + 1, end, depth -1)

def do_heapsort(arr, start, end):
    do_max_heap(arr, start, end)
    for i in range(end-1, start, -1):
        arr[start], arr[i] = arr[i], arr[start]
        do_max_heapify(arr, index=0, start=start, end=i)

def do_max_heap(arr, start, end):
    def parent(i):
        return (i-1)//2

    length = end - start
    index = parent(length-1)
    while index >= 0:
        do_max_heapify(arr, index, start, end)
        index -= 1

def do_max_heapify(arr, index, start, end):
    def left(i):
        return 2 * i + 1
    def right(i):
        return 2 * i + 2

    size = end - start

    l = left(index)
    r = right(index)

    if (l < size and arr[start + 1] > arr[start + index]):
        largest = l
    else:
        largest = index
    if (r < size and arr[start + r] > arr[start + largest]):
        largest = r
    if largest != index:
        arr[start + largest], arr[start + index] = arr[start + index], arr[start + largest]
        do_max_heapify(arr, largest, start, end)

def partition(array, start, end):

    # choose start element as pivot
    pivot = array[start]
    low = start + 1
    high = end - 1

    while True:
        while low <= high and array[high] >= pivot:
            high -= 1
        while low <= high and array[low] <= pivot:
            low += 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    #print("partitioned array: ", arr)
    #print("pivot index: ", low, "pivot value: ", pivot)

    # Return the position from where partition is done
    array[start], array[high] = array[high], array[start]
    #print("pivot index: ", high, "pivot value: ", pivot)
    return high

def extract_smallest(arr_e):
    print("arr_e:", arr_e)
    smallest = ()
    for i in range(len(arr_e)):
        if smallest == ():
            smallest = (i, arr_e[i])

        if smallest[1] > arr_e[i]:
            print("smallest vs current:", smallest[1], arr_e[i])
            smallest = (i, arr_e[i])

    smallest_val = arr_e.pop(smallest[0])
    print("smallest_val", smallest_val)
    return smallest_val, arr_e


def heapsort(arr_l):
    heap = ['' for _ in arr_l]
    n = len(heap)
    for i in range(0, n):
        # print(i)
        print("arr:", arr_l)
        heap[i], arr_l = extract_smallest(arr)

    return heap



#arr = [4, 10, 3, 7, 4, 6] #[12, 11, 13, 5, 6, 7]

# 11, 12, 13, 5, , 6, 7
# 11, 12, 13 ..
# 11, 5, 13, 12, ..
# 11, 5, 13, 6, 12, 7
# 11, 5, 13

# print(heapsort(arr))

# print(extract_smallest(arr))

#print(partition(arr, 0,5))
def get_list_nums():
    return [random.randint(1, 1000) for _ in range(random.randint(10, 1000))]

# add list of tuples for length / time_delta records
func_performance = []
heap_used_counter = 0
num_runs = 100
# test run time
for i in range(num_runs):
    rand_arr = get_list_nums()
    start_time = time.time()
    introsort(rand_arr)
    end_time = time.time()

    if heap_used == True:
        heap_used_counter += 1
    heap_used = False

    # exec time
    time_delta = end_time - start_time
    func_performance.append((len(rand_arr), time_delta))

print("performance:", sorted(func_performance, key=lambda x: x[1], reverse=True))
print(heap_used_counter/num_runs)