import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order.
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    return found

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    return found

def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
    
def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

def benchmark_search():
    list_sizes = [500, 1000, 5000]
    target = 99999999  # Element that won't exist

    for size in list_sizes:
        # Sequential Search Benchmark
        total_time = 0
        for _ in range(100):
            my_list = get_me_random_list(size)
            start = time.time()
            check = sequential_search(my_list, target)
            total_time += time.time() - start
        avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")
        
        # Ordered Sequential Search Benchmark
        total_time = 0
        for _ in range(100):
            my_list = sorted(get_me_random_list(size))  # Must be sorted for ordered search
            start = time.time()
            check = ordered_sequential_search(my_list, target)
            total_time += time.time() - start
        avg_time = total_time / 100
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")

        # Binary Search Iterative Benchmark
        total_time = 0
        for _ in range(100):
            my_list = sorted(get_me_random_list(size))  # Must be sorted for binary search
            start = time.time()
            check = binary_search_iterative(my_list, target)
            total_time += time.time() - start
        avg_time = total_time / 100
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")

        # Binary Search Recursive Benchmark
        total_time = 0
        for _ in range(100):
            my_list = sorted(get_me_random_list(size))  # Must be sorted for binary search
            start = time.time()
            check = binary_search_recursive(my_list, target)
            total_time += time.time() - start
        avg_time = total_time / 100
        print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {size} elements")

if __name__ == "__main__":
    benchmark_search()
