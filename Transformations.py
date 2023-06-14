# **** imports ****
import math                                 # for math functions
import matplotlib.pyplot as plt             # for plotting

from skimage import io                      # for image io
from skimage import data                    # for image data
from skimage import transform               # for image transformation
from skimage.transform import swirl, warp   # for swirl transformation


# **** read gears image ****
gears = io.imread('./images/pexels-gears.jpg')

# **** print gears image shape ****
print(f'gears.shape: {gears.shape}')
print(f'gears.shape[0]: {gears.shape[0]}')
print(f'gears.shape[1]: {gears.shape[1]}')
print(f'gears.shape[2]: {gears.shape[2]}')

# **** display gears RGB image ****
plt.figure(figsize=(10, 10))
plt.imshow(gears)               # display the image
plt.title('Gears')
plt.show()


# **** Shape preserving transformation - only scalling,
#      translation, and rotation ****
tform = transform.SimilarityTransform(  scale=2.0,                  # scale factor
                                        translation=(-200, -400),   # translation
                                        rotation=math.pi/16         # rotation angle
                                     )

# **** apply transformation to gears image ****
rotated = transform.warp(   gears,
                            tform)

# **** apply inverse transformation to rotated image ****
back_rotated = transform.warp(  rotated,
                                tform.inverse)

# **** display rotated image ****
plt.figure(figsize=(10, 10))
plt.imshow(rotated)             # display the image
plt.title('Scale, Rotate & Translate')
plt.show()


# **** display back rotated image ****
plt.figure(figsize=(10, 10))
plt.imshow(back_rotated)        # display the image
plt.title('Back Rotated')
plt.show()


# **** swirl transformation ****
gears_swirl = swirl(gears, 
                    rotation=0, 
                    strength=20, 
                    radius=150,
                    mode='constant')

# **** display gears swirl image ****
plt.figure(figsize=(10, 10))
plt.imshow(gears_swirl)         # display the image
plt.title('Gears Swirl')
plt.show()


# **** swirl transformation ****
gears_swirl = swirl(gears, 
                    rotation=0, 
                    strength=20, 
                    radius=350,
                    mode='constant')

# **** display gears swirl image ****
plt.figure(figsize=(10, 10))
plt.imshow(gears_swirl)         # display the image
plt.title('Gears Swirl')
plt.show()


# **** swirl transformation ****
gears_swirl = swirl(gears, 
                    rotation=0, 
                    strength=10, 
                    radius=350,
                    mode='constant')

# **** display gears swirl image ****
plt.figure(figsize=(10, 10))
plt.imshow(gears_swirl)         # display the image
plt.title('Gears Swirl')
plt.show()