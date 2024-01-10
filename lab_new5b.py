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
        if isinstance(hsv_tuple, tuple):
            if len(hsv_tuple) == 3:
                for i in hsv_tuple:
                    if 0 > i or i > 255:
                        raise ValueError ("Each pixel must have a value between 0 and 255")
                h, s, v = hsv_tuple
                if hlow <= h <= hhigh and slow <= s <= shigh and vlow <= v <= vhigh:
                    return 1
                else:
                    return 0
            else:
                raise ValueError ("Hsv_tuple must be 3 units long")
        else:
            raise TypeError ("must be tuples")
    return pixel_range


"""
# Lab5b2
"""

def generator_from_image(orig_list):
    """ returns a function which returns the color of a pixel """

    if not isinstance(orig_list, list):
            raise TypeError ("Input must be a list")
            
    elif len(orig_list) == 0:
            raise IndexError ("Input can't be an empty list")
        
    def check_color(pixel):
        if pixel > len(orig_list):
            raise IndexError ("Pixel index cant be longer than list")
        else:
            if len(orig_list[pixel]) == 3:
                if isinstance(orig_list[pixel], tuple):
                    return orig_list[pixel]
                else:
                    raise TypeError ("Pixel must be a tuple")
            else:
                raise ValueError ("Each pixel tuple must be of of length 3")
        
    return check_color



"""
Lab5b3
"""
      

def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)


def comb_images(bgr_list, condition, generator1, generator2):

    try:
        generator1_list = [generator1(i) for i in range(len(bgr_list))]
        generator2_list = [generator2(i) for i in range(len(bgr_list))]
    except IndexError:
        raise IndexError ("Lists and tuples must be of SAME length")
    except ValueError:
        raise ValueError ("Each pixel must be of length 3")
    except TypeError:
        raise TypeError ("Pixel must be a tuple")
   
    return [add_tuples(multiply_tuple(generator1_list[i], condition(bgr_list[i])),
            multiply_tuple(generator2_list[i], (1 - condition(bgr_list[i])))) for i in range(len(bgr_list))]


"""
Lab5b4
"""

def gradient_condition(bgr_tuple):
    """ the function returns a rounded float value between 1 and 0 """
    return round(bgr_tuple[0]/255, 3)


def test_combine():
    """ Tests comb_images with different cases of both errors and right inputs"""

    condition = pixel_constraint(50, 255, 50, 255, 50, 255)
    hsv_list = [(3,3,3), (3,3,3), (3,3,3), (3,3,3)]

    gen5 = [(1,1,1), (1,1,1), (1,1,1)]
    gen6 = [(1,1,1), (1,1,1)]
    generator5 = generator_from_image(gen5)
    generator6 = generator_from_image(gen6)

    gen2 = [(1,1,1), (1,1,1), (1,1)]
    gen3 = [(1,1,1), (1,1,1), (1,1,1)]
    generator2 = generator_from_image(gen2)
    generator3 = generator_from_image(gen3)

    gen7 = [[1,1,1], [1,1,1], [1,1,1]]
    gen8 = [[1,1,1], [1,1,1], [1,1,1]]
    generator7 = generator_from_image(gen7)
    generator8 = generator_from_image(gen8)


    try: #tests when one list is too short
        comb_images(hsv_list, condition, generator5, generator6)
        raise AssertionError
    except IndexError:
        print("IndexError - comb")

    try: #test that sees that the tuple is not of the right lenght
        comb_images(hsv_list, condition, generator2, generator3)
        raise AssertionError
    except ValueError:
        print("ValueError - comb")

    try: # test that sees that the input is wrong (list instead of tuples)
        comb_images(hsv_list, condition, generator7, generator8)
        raise AssertionError
    except TypeError:
        print("TypeError - comb")


    bgr_list = [(2,2,2), (2,2,2)]
    gen1 = [(2,2,2), (2,2,2)]
    gen4 = [(1,1,1), (1,1,1)]
    
    generator1 = generator_from_image(gen1)
    generator2 = generator_from_image(gen4)

    res = comb_images(bgr_list, condition, generator1, generator2)
    for i in range(len(res)): 
        assert res[i] == gen4[i]    #tests that the result is the same as gen4 since its  
                                    #the generator which matches the condition


    bgr_list1 = [(120,120,120), (49,49,49)]
    gen1 = [(120,120,120), (49,49,49)]
    gen4 = [(49,49,49), (120,120,120)]

    generator1 = generator_from_image(gen1)
    generator2 = generator_from_image(gen4)

    res1 = comb_images(bgr_list1, condition, generator1, generator2)
    for i in range(len(res1)): 
        assert res1 == [(120,120,120), (120,120,120)] #tests values from both lists
    



def test_generator():
    """"
    tests generator_from_image with different cases of errors that can occur
        also tests if the code is working the right way for right input
    
    """
       
    error1 = [[1,3,4], [1,3,5], [1,2,3]]
    error2 = [(1,2), (1,2), (7,9)]
    error3 = []
    error4 = (1,2,3)
        
    test_list = [(1,2,3), (4,5,6), (7,8,9)]
    func = generator_from_image(test_list)

    assert func(2) == (7,8,9)

    try:                            #test with wrong input, should be list of tuples
        res1 = generator_from_image(error1)
        res1(2)
        raise AssertionError
    except TypeError:
        print ("TypeError1 - gen")
    try:                            #tests empty list 
        generator_from_image(error3)
        raise AssertionError
    except IndexError:
        print("indexError - gen")

    try:                            #tests too short list of tuples
        res = generator_from_image(error2)
        res(2)
        raise AssertionError
    except ValueError:
        print("ValueError - gen")

    try:                            #tests wrong input, should be list of tuples
        generator_from_image(error4)
        raise AssertionError
    except TypeError:
        print("TypeError - gen")

    try:                            #tests index outside of list length
        res2 = generator_from_image([(1,2,3), (1,2,3)])
        res2(4)
        raise AssertionError
    except IndexError:
        print("IndexError - gen")



def test_constraint():
    """ 
    Tests pixel_constratint for values inside and outside of the condition and 
        different kinds of errors
    """

    func = pixel_constraint(100, 254, 100, 254, 100, 254)

    assert func((120, 50, 50)) == 0       #tests value out of wanted range
    assert func((120, 120, 120)) == 1     #test a value inside of range
    assert func((99, 120, 120)) == 0       #tests edge values under
    assert func((120, 255, 255)) == 0       #test edge value over
            

    try:                                #tests too high value
        func((120, 120, 256))
        raise AssertionError
    except ValueError:
        print("ValueError - const")
    try:                                #tests too low value
        func((120, -3, 255))
        raise AssertionError
    except ValueError:
        print("ValueError2 - const")

    try:                                #tests too long tuple
        func((100, 120, 120, 255))
        raise AssertionError
    except ValueError:
        print("ValuError3 - const")
    
    try:                                #tests input thats not a tuple
        func([120, 120, 120])
        raise AssertionError
    except TypeError:
        print("TypeError - const ")


def run_free_spans_tests():
    test_constraint()
    test_generator()
    test_combine()
    
    print("All tests passed")
run_free_spans_tests()
