from lab5b import *
from lab5a import *
from cvlib import *

def test_constraint():
    func = pixel_constraint(100, 255, 100, 255, 100, 255)

    res = func((120, 120, 120))
    assert(res == 1)

    res1 = func((120, 100, 256))
    assert(res1 == 0)

    res2 = func((120, -3, 255))
    assert(res2 == 0)

    try:
        func((100, 120, 120, 255))
        assert False
    except ValueError:
        pass
    

def test_generator():
    test_list = [(1,2,3), (4,5,6), (7,8,9)]
    func = generator_from_image(test_list)

    error1 = [(1,2,3), (4,5,6)]
    error2 = [(1,2), (1,2,3), (7,9)]
    error3 = []
    error4 = (1,2,3)

    for i in range(len(test_list)):
        assert (func(i) == test_list[i])
        
        try:
            assert(func(i) == error1[i])
        except IndexError:
            pass

        try:
            assert func(i) != error3[i]
        except IndexError:
            pass
        
        assert func(i) != error2[i]
        assert func(i) != error4[i]

        

def test_combine():
    condition = pixel_constraint(50, 255, 50, 255, 50, 255)
    hsv_list = [(3,3,3), (3,3,3)]

    gen1 = [(2,2,2), (2,2,2)]
    gen2 = [(1,1,1), (1,1,1)]
    
    generator1 = generator_from_image(gen1)
    generator2 = generator_from_image(gen2)

    res = comb_images(hsv_list, condition, generator1, generator2)
    for i in range(len(res)):
        assert len(res[i]) == len(hsv_list[i])


    gen3 = [(2,2), (2,2)]
    gen4 = [(1,1,1), (1,1,1)]
    generator3 = generator_from_image(gen3)
    generator4 = generator_from_image(gen4)
    
    error1 = comb_images(hsv_list, condition, generator3, generator4)
        
    for i in range(len(error1)):
        assert len(error1[i]) != len(hsv_list[i])


    gen5 = [(2,2,2), (2,2,2), (2,2,2)]
    gen6 = [(1,1,1), (1,1,1)]
    generator5 = generator_from_image(gen5)
    generator6 = generator_from_image(gen6)

    try:
       comb_images(hsv_list, condition, generator5, generator6)
    except IndexError:
        print("IndexError")
        pass
    
    
def run_free_spans_tests():
    test_constraint()
    test_generator()
    test_combine()
    
    print("All tests passed")
run_free_spans_tests()
