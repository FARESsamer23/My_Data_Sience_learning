import numpy as np 
import sys as sys
import time as time

# elements = 15000000
# my_list1 = range(elements)
# my_list2 = range(elements)

# my_array1 = np.arange(elements) 
# my_array2 = np.arange(elements)

# list_start1 = time.time() 
# # hadi methode bah tloopi tow  arrays in same time
# result = [(n1 + n2)  for n1, n2 in zip(my_list1, my_list2)]

# list_end1 = time.time() 
# hadi methode bah tloopi tow  arrays in same time
# result = [expression for item in iterable] list de comprehension
# list_start = time.time()
# result = my_array1 + my_array2  # sum of each elemlent with other  kima fi la somme t3 les matrices
# list_end = time.time()    
 
# print(  " for the list ",str(list_end1 - list_start1)) # tidi we9t
# print( "for the array of numpy",str(list_end - list_start)) # tidi we9t 9lil  0,.....

my_array = np.arange(100)
print(my_array.itemsize) # size of each element in bite
print(my_array.size) # size of array number of elements
# list les elements size  ta3ha yedo memory bezzef
 