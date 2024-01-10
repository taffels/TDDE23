import cv2
import numpy
import random
from lab5a import *
from cvlib import *

"""
Lab5b1
"""

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """ returns a function which checks if the values are in range and returns 1, else returns 0"""
    
    def pixel_range(hsv_tuple):
        h, s, v = hsv_tuple
        if hlow <= h <= hhigh and slow <= s <= shigh and vlow <= v <= vhigh:
            return 1
        else:
            return 0
    return pixel_range


hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
plane_list = cvimg_to_list(hsv_plane)

is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

cv2.imshow('Sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
cv2.waitKey(0)


"""
Lab5b2
"""

def generator_from_image(orig_list):
    """ returns a function which returns the color of a pixel """
    def check_color(pixel):
        return orig_list[pixel]
    return check_color


orig_img = cv2.imread("plane.jpg")
orig_list = cvimg_to_list(orig_img)

generator = generator_from_image(orig_list)

new_list = [generator(i) for i in range(len(orig_list))]

cv2.imshow('Original', orig_img)
cv2.imshow('New', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
cv2.waitKey(0)


"""
Lab5b3
"""

plane_img = cv2.imread("plane.jpg")

condition = pixel_constraint(100, 150, 50, 200, 100, 255) 

hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))     
plane_img_list = cvimg_to_list(plane_img)                

def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

generator2 = generator_from_image(plane_img_list)

def comb_images(bgr_list, condition, generator3, generator4):
    """ combines two images by using the gradient condition for each pixel """
    return [add_tuples(multiply_tuple(generator3(i), condition(bgr_list[i])),
            multiply_tuple(generator4(i), (1 - condition(bgr_list[i])))) for i in range(len(bgr_list))]

result = comb_images(hsv_list, condition, generator1, generator2)
new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
cv2.imshow("Final image", new_img)
cv2.waitKey(0)


"""
Lab5b4
"""


plane_img = cv2.imread("plane.jpg")
flower_img = cv2.imread("flowers.jpg")
gradient_img = cv2.imread("gradient.jpg")

gradient_list = cvimg_to_list(gradient_img)
plane_list = cvimg_to_list(plane_img)
flower_list = cvimg_to_list(flower_img)

generator3 = generator_from_image(flower_list)
generator4 = generator_from_image(plane_list)


def gradient_condition(bgr_tuple):
    """ the function returns a rounded float value between 1 and 0 """
    return round(bgr_tuple[0]/255, 1)
    
res = comb_images(gradient_list, gradient_condition, generator3, generator4)
img2 = rgblist_to_cvimg(res, gradient_img.shape[0], gradient_img.shape[1])
cv2.imshow("Result", img2)
cv2.waitKey(0)

