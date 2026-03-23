import time

def bubble_sort(arr: list) -> list:
    bubble = len(arr)
    while bubble >= 1:
        for i in range(0, bubble - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(arr)
            time.sleep(1.5)
        bubble -= 1

    return arr

bubble_sort([2,4,6,7,2,3,4,6])