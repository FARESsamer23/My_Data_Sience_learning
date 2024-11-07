import numpy as np
 
#  shwo  array data type

my_array1 = np.array([1,2,3])
my_array2 = np.array([1.3,2.4,3.4])
my_array3 = np.array(["fares","anis","abdou"],)
print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)
print("#"*50)

#create array with specific data type
  
my_array1 = np.array([1,2,3],dtype=float) # float or "float" or "f"
print(my_array1.dtype)
my_array2 = np.array([1.3,2.4,3.4],dtype=int) #int or "int" or "i"
print(my_array2.dtype)

# change data type of Exxisting  array
my_array4 = np.array([13,24,34],dtype="f")
print(my_array4.dtype)
print(my_array4)
print(my_array4[0].itemsize)

print('#'*50)
my_array4 = my_array4.astype("float") 
print(my_array4.dtype)
print(my_array4)
print(my_array4[0].itemsize)

#Test Capacity
