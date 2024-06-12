import heapq
import numpy as np

def heap_sort(iterable):
    # Create a minimal heap of all elements of the iterable object.
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    # Pull the elements in order, forming a sorted array.
    return [heapq.heappop(h) for _ in range(len(h))]

cables = np.random.randint(1, 100, 10)
print(f"Unsorted cables: {cables}")

unsorted_price = 0
for i in cables:
    inter_price = unsorted_price + i
    unsorted_price += inter_price

print(f"Unsorted cables price: {unsorted_price}\n")

sorted_cables = heap_sort(cables)
print(f"Sorted cables: {sorted_cables}")

sorted_price = 0
for i in sorted_cables:
    inter_price = sorted_price + i
    sorted_price += inter_price

print(f"Unsorted cables price: {sorted_price}")