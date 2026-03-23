import time


def bubble_sort(
    arr: list[int], delay: float = 1.5, show_steps: bool = True
) -> list[int]:
    bubble = len(arr)
    while bubble >= 1:
        for i in range(0, bubble - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if show_steps:
                print(arr)
                if delay > 0:
                    time.sleep(delay)
        bubble -= 1

    return arr


if __name__ == "__main__":
    bubble_sort([2, 4, 6, 7, 2, 3, 4, 6])
