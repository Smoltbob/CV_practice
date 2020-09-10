#!/usr/bin/env python3
import queue
"""
Connected components analysis implementation.
Given a 2D grid, return the number of connected components
"""

image = [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]
        ]


image = [[0,1],[1,1]]
"""
Get neighbors, using a 4 connectivity
 n
nx
"""
def get_neighbors(pixel: (int, int), height, width):
    res = []
    if pixel[1]-1 >= 0: # north
        res.append((pixel[0], pixel[1]-1))
    if pixel[0]-1 >= 0: # west
        res.append((pixel[0]-1, pixel[1]))
    if pixel[1]+1 < height: # south
        res.append((pixel[0], pixel[1]+1))
    if pixel[0]+1 < width: # east
        res.append((pixel[0]+1, pixel[1]))
    return res

"""
One component at a time
Once the first pixel of a connected component
is found, it is fully explored before going to
the next pixel.
We use a linked list / queue to keep indexes of pixels 
that are connected to each other.
"""
def connected_components(image):
    height = len(image)
    width = len(image[0])
    i = 0
    # convert to int
    while i < width * height:
        y = i // width
        x = i % width
        image[y][x] = int(image[y][x])
        i += 1
    for line in image:
        print(line)
    print()
    # Start from first pixel in the image 
    # and set current label to 2
    i = 0
    current = 2
    q = queue.Queue()
    while i < width * height:
        y = i // width 
        x = i % width
        pix = image[y][x]
        # if it is foreground and not labelled
        # give it the current label and add to a queue
        if pix == 1:
            image[y][x] = current
            q.put((x,y))
            # then explore all of the neighboring pixels,
            # as long as we find foreground pixels
            while not q.empty():
                pix2 = q.get()
                neigh = get_neighbors(pix2, height, width)
                for (nx, ny) in neigh:
                    if image[ny][nx] == 1:
                        image[ny][nx] = current
                        q.put((nx,ny))
            # we are done with this component,
            # increase the label counter
            current += 1
        else:
            i+=1

    return image

res = connected_components(image)

for line in res:
    print(line)


