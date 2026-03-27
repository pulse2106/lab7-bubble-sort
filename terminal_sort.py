import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_screen(arr, algo):
    global vis
    if vis:
        clear_screen()
        to_show = []
        print("> Algorithm  : {}".format(algo))
        print('********************************************')
        for i in arr:
            if int(i) < 10:
                to_show.append('[{}]  : {}'.format(i, '#'*i))    
            else:
                to_show.append('[{}] : {}'.format(i, '#'*i))
        for i in to_show:
            print(i)
        print('********************************************')
        time.sleep(0.10)  

def compare_screen(arr, algo, j, k):
    global vis
    if vis:
        clear_screen()
        to_show = []
        print("> Algorithm  : {}".format(algo))
        print('********************************************')
        for i in arr:
            # Element to be compared
            if i == j or i == k:
                if int(i) < 10:
                    to_show.append('[{}]  : \033[33m{}\033[00m'.format(i, '#'*i))    
                else:
                    to_show.append('[{}] : \033[33m{}\033[00m'.format(i, '#'*i))
            else:
                if int(i) < 10:
                    to_show.append('[{}]  : {}'.format(i, '#'*i))    
                else:
                    to_show.append('[{}] : {}'.format(i, '#'*i))
        for i in to_show:
            print(i)
        print('********************************************')
        time.sleep(0.25)

def swap_screen(arr, algo, j, k):
    global vis
    if vis:
        clear_screen()
        to_show = []
        print("> Algorithm  : {}".format(algo))
        print('********************************************')
        for i in arr:
            # Element to be compared
            if i == j or i == k:
                if int(i) < 10:
                    to_show.append('[{}]  : \033[34m{}\033[00m'.format(i, '#'*i))    
                else:
                    to_show.append('[{}] : \033[34m{}\033[00m'.format(i, '#'*i))
            else:
                if int(i) < 10:
                    to_show.append('[{}]  : {}'.format(i, '#'*i))    
                else:
                    to_show.append('[{}] : {}'.format(i, '#'*i))
        for i in to_show:
            print(i)
        print('********************************************')
        time.sleep(0.25)

def bubble_sort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1):
            compare_screen(arr, "Bubble Sort", arr[j], arr[j+1])
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_screen(arr, "Bubble Sort", arr[j], arr[j+1])
    return (arr, "Bubble Sort")

def shuffle(arr):
    for i in range(len(arr)):
        r = random.randint(0, len(arr)-1)
        arr[i], arr[r] = arr[r], arr[i]
    return arr

def genArr(n):
    arr = [i for i in range(1, n+1)]
    arr = shuffle(arr)
    return arr

vis = True
row = os.get_terminal_size()[1]

# code was sourced from a git repo https://github.com/Naimish240/TerminalSort/blob/master/code/sort.py


if __name__ == "__main__":
    bubble_sort([2, 4, 6, 7, 2, 3, 4, 6])
