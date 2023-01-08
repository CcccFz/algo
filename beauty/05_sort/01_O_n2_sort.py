from typing import List

def bubble_sort(items: List[int]):
    size = len(items)
    if size <= 1:
        return
    for i in range(size):
        is_swap = False
        for j in range(size-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                is_swap = True
        if not is_swap:
            return

def insert_sort(items: List[int]):
    size = len(items)
    if size <= 1:
        return
    for i in range(1, size):
        val = items[i]
        j = i - 1
        while j >= 0 and items[j] > val:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = val

def select_sort(items: List[int]):
    size = len(items)
    if size <= 1:
        return
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if items[j] < items[min]:
                min = j
        items[i], items[min] = items[min], items[i] 

arr = [3,2,1,5,4,6,7]
bubble_sort(arr)
print(arr)
arr = [3,2,1,5,4,6,7]
insert_sort(arr)
print(arr)
arr = [3,2,1,5,4,6,7]
select_sort(arr)
print(arr)