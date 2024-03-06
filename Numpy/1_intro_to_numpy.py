# import numpy as np
#
# a = np.zeros((10,10))
# print(a)
#
# a = np.zeros((10,10),dtype=int)
# print(a)
#
# # one-dimensional nd array
# a = np.arange(1,101)
# print(a)
#
# # two-dimensional nd array
# print(a.reshape((10,10)))
#
# # identity matrix
# a = np.identity(5)
# print(a)
#
# print(type(np))
# print(type(a))
# help(np.ndarray)

# # Example 1: Coefficient Matrix and value matrix
#
# # x+y = 2200
# # 3x + 8y = 10100
#
# import numpy as np
#
# a = np.array([[1,1],[3,8]])
# print(a)
# print(type(a))                     # <class 'numpy.ndarray'>
# b = np.array([2200,10100])
# print(b)
# print(type(b))                     # <class 'numpy.ndarray'>
# print(np.linalg.solve(a,b))
#
# import numpy as np
# from datetime import datetime
# a = np.array([10,20,30])
# b = np.array([1,2,3])

# # dot product: a.b = 10*1 + 20*2 + 30*3 = 140

# # Traditional Python Code: using nested loop
# def dot_product(a,b):
#     result = 0
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if i == j:
#                 result += a[i] * b[j]
#     return result
#
# before = datetime.now()
# for i in range(10000000):
#     dot_product(a,b)
# after = datetime.now()
#
# print('Time taken by traditional python nested for loop: ',after - before)

# # Alternatively: using zip()
# def dot_product1(a,b):
#     result = 0
#     for i, j in zip(a,b):
#         result += i*j
#     return result
#
# before = datetime.now()
# for i in range(10000000):
#     dot_product1(a,b)
# after = datetime.now()
# print('Time taken by traditional python zip(): ',after - before)

# # numpy library code
# before = datetime.now()
# for i in range(10000000):
#     np.dot(a,b)
# after = datetime.now()
# print('Time taken by numpy: ',after - before)

# creating Array

# # 1. Array Module
#
# import array
# L = [10,20,30]
# a = array.array('i',L)
# print(a)
# print(type(a))         # <class 'array.array'>
#
# print('Elements of Array one by one: ')
# for i in a:
#     print(i)
#
# # Note: Array module is not recommended as it lacks library support
# # when compared to numpy module

# # 2. numpy module
# import numpy
# L = [10,20,30]
# a = numpy.array(L)
# print(a)
# print(type(a))        # <class 'numpy.ndarray'>
#
# print('Elements of Array one by one: ')
# for i in a:
#     print(i)
#     print(type(i))     # <class 'numpy.int64'>

# # List vs. ndarray
#
# import numpy
# import sys
#
# # Element Types
# L = [10,20,'skg']
# a = numpy.array(L)
# print(L)                 # [10, 20, 'skg']
# print(a)                 # ['10' '20' 'skg']
#
# # Vector Operations
# L = [10,20,30]
# a = numpy.array(L)
# # print(L+2)            # TypeError: can only concatenate list (not "int") to list
# print(a+2)              # [12 22 32]
#
# # Memory Consumption
# L = [10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100]
# a = numpy.array([10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100])
# print('The size of list: ',sys.getsizeof(L))
# print('The size of ndarray: ',sys.getsizeof(a))         # ***** Surprised!
