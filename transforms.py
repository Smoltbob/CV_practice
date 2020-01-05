#!/usr/bin/env python3
"""
Apply transforms to images
"""

from skimage import data, io
import numpy as np

img = data.coffee()


"""
Offset in x,y
thau the angle of rotation
We build the kernel used to compute the new coordinates
"""

offset = [20, 20]
thau = np.deg2rad(5)
kernel = np.array([[np.cos(thau),-np.sin(thau), offset[0]],
                   [np.sin(thau),np.cos(thau), offset[1]]])


res = np.zeros_like(img)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        # new coordinates
        nc = kernel.dot(np.array([x,y,1]))
        if 0 <= nc[1] < np.shape(img)[1] and 0 <= nc[0] < np.shape(img)[0]:
            res[int(nc[0]),int(nc[1])] = img[x,y]

io.imshow(res)
io.show()
