import cv2
import numpy
import math

def cvimg_to_list(img):
    """ checks each pixel and saves each bgr tuple as individual values b g r in a list"""

    bgr_list = []

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            b, g, r = img[x, y]
            bgr_list.append((b, g, r))
    return bgr_list


def unsharp_mask(N):
  """ calculates a 2D-list using the gaussisk blur formula"""

  s = 4.5
  return [[1.5] if (x,y) == (0,0) else 
          [(-1/(2 * math.pi * s**2)) * math.e ** (-(x**2 + y**2)/(2* s **2))]
          for x in range(math.ceil(-N/2), math.ceil(-N/2) + N) for y in range(math.ceil(-N/2), math.ceil(-N/2) + N)]


# img = cv2.imread('flowers.jpg')
# kernel = numpy.array(unsharp_mask(3))
# filtered_img = cv2.filter2D(img, -1, kernel)    
# #cv2.imshow("Filtered", filtered_img)
# #cv2.waitKey(0)