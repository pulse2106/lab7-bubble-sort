import pygame
import random

def shuffle(arr: list):
    for i in range(len(arr)):
        r = random.randint(0, len(arr)-1)
        arr[i], arr[r] = arr[r], arr[i]
    return arr

def genArr(n: int):
    arr = [i for i in range(1, n+1)]
    arr = shuffle(arr)
    return arr

# method to show the list of height
def show(arr, win):
    # initial position
    x = 0
    y = 0
    # width of each bar
    width = 30
    for i in range(len(arr)):
        # drawing each bar with respective gap
        if i % 2 == 0:
            pygame.draw.rect(win, (255, 0, 0), (x + 40 * i, y, width, (arr[i]*20)))
        else:
            pygame.draw.rect(win, (0, 255, 0), (x + 40 * i, y, width, (arr[i]*20)))


# infinite loop
def main():
    pygame.init()
    # setting window size
    win = pygame.display.set_mode((500, 400))
    # setting title to the window
    pygame.display.set_caption("Bubble sort")
    run = True
    arr = genArr(16)
    while run:
        # execute flag to start sorting
        execute = False
        # time delay
        pygame.time.delay(10)
        # getting keys pressed
        keys = pygame.key.get_pressed()
        # iterating events
        for event in pygame.event.get():
            # if event is to quit
            if event.type == pygame.QUIT:
                # making run = false so break the while loop
                run = False
        # if space bar is pressed
        if keys[pygame.K_SPACE]:
            # make execute flag to true
            execute = True
        # checking if execute flag is false
        if execute == False:
            # fill the window with black color
            win.fill((0, 0, 0))
            # call the height method to show the list items
            show(arr, win)
            # update the window
            pygame.display.update()
            run == False
        # if execute flag is true
        else:
            for i in range(len(arr) - 1):
                for j in range(len(arr) - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    win.fill((0, 0, 0))
                    # call show method to display the list items
                    show(arr, win)
                    # create a time delay
                    pygame.time.delay(30)
                    # update the display
                    pygame.display.update()

# exiting the main window
pygame.quit()

# sourced from https://www.geeksforgeeks.org/python/bubble-sort-visualizer-using-pygame/

if __name__ == "__main__":
    main()