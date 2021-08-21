import pygame
import math
import random

'''
CHOOSE ALG BELOW 
'''
ALG = 'merge' #change alg here (insertion, bubble, merge)


WIDTH, HEIGHT = 600, 400 
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #window
pygame.display.set_caption("Path Finder")


#Colors
RED = (255, 0, 0) 
GREEN = (0, 255, 0) #Node added to set
BLUE = (0, 0, 255) 
YELLOW = (255, 255, 0)#Path color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) #Node is a barrier
PURPLE = (128, 0, 128) #End Node
ORANGE = (255, 165 ,0) #Start Node
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)#Node has been checked




class Node:
    def __init__(self, x, width, val):
        self.val = val
        self.width = width
        self.y = 0
        self.x = x*width#pos
        self.color = BLACK


    #draws Node
    def draw_node(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width-.1, self.val))



def mergeSort(arr):
    i,j = 2,0

    while(True):
        j=0

        while(j<len(arr)-1):
            right = j+i-1
            left = j

            if (right > len(arr)):
                right = len(arr)-1
            
            mid = (left+right)//2
            
            merge(arr, left, right, mid)
            j=j+i
        
        i = i*2
        if (i >= len(arr)):
            i = i//2
            merge(arr, 0, len(arr)-1, i-1)
            break


def merge(arr, l, r, mid):
    left_data = mid-l+1
    right_data = r-mid
    a,b,c = 0,0,l

    left = []
    right = []

    for i in range(left_data):
        left.append(arr[l+i])

    for i in range(right_data):
        right.append(arr[mid+1+i])
    

    while (a < left_data and b < right_data):
        if (left[a] < right[b]):
            arr[c] = left[a]
            a+=1
            c+=1
        else: 
            arr[c] = right[b]
            b+=1
            c+=1
        
        VISUALIZE(arr, 50)
    
    while (a < left_data):
        arr[c] = left[a]
        a+=1
        c+=1

        VISUALIZE(arr, 50)

    while (b < right_data):
        arr[c] = right[b]
        b+=1
        c+=1

        VISUALIZE(arr, 50)



def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                VISUALIZE(arr)
        VISUALIZE(arr)
    


def insertion(arr):
    for i in range(1, len(arr)):
        current = arr[i]

        j = i-1
        while j >= 0 and arr[j] > current:
                arr[j + 1] = arr[j]
                j -= 1

                VISUALIZE(arr)

        arr[j+1] = current
        VISUALIZE(arr)

    
def VISUALIZE(arr, delay=100):
    pygame.time.delay(delay)
    GRID = make_grid(20, WIDTH, arr)
    draw(WIN, GRID)


def make_grid(rows, width, arr):
    grid = []
    cube_width = width//rows #width is the width of the grid

    for i in range(len(arr)):
        node = Node(i, cube_width, arr[i]) 
        grid.append(node)

    return grid


#main draw method
def draw(win, grid):
    win.fill(WHITE)

    for node in grid:
        node.draw_node(win) #draws nodes

    pygame.display.update()


def initArr():
    l = []
    for i in range(20):
        l.append(random.randint(20,340))

    return l


def main(win, width, alg):
    ROWS = 20
    ARR = initArr()
    print(ARR)
    GRID = make_grid(ROWS, width, ARR)

    clock = pygame.time.Clock()
    run = True
    alg = alg

    draw(win, GRID)
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #insertion sort
                    if alg == 'insertion':
                        insertion(ARR)
                    elif alg == 'bubble':
                        bubble(ARR)
                    elif alg == 'merge':
                        mergeSort(ARR)

                if event.key == pygame.K_r:
                    main(win, width, alg)

    pygame.quit()


main(WIN, WIDTH, ALG)