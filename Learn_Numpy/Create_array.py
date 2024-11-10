import numpy as np 


# my_list = [1,3,2,5,6]

# my_array = np.array(my_list)

# print(my_list)
# print(my_array)

# print("#"*50)

# # Type
# print(type(my_list))
# print(type(my_array))

# # Accessing elemnet 
# print(my_list[0])
# print(my_array[0])

# print("#"*50)

# #0D
# a = np.array(10)
# #1D
# b= np.array([10,20])
# #2D
# c = np.array([[10,20],[30,40]])
# #3D
# d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(d[1][1][0])
# print(d[1,1,0]) # the same to get  and  than you can get it withe negative indexing
# print(d[-1,-1,0]) # the same to get  and  than you can

# print("#"*50)
# #number of dimensions
# print(d.ndim)
# print("#"*50)
# #custom Dimensions
# my_custom_array = np.array([1,2,3],ndmin=3)
# print(my_custom_array[0,0,0]) #  the first array 2d  the  first 1d array in 2d and the first elemnet in 1d array in 2d array in the 3d array 
# print(my_custom_array.ndim)

ar2 = np.random.rand(4,56) # min 0 l 1  thaddidilha chhal min array ou fi kol array chhal min ra9m mahsor bin 0 w 1
ar1 = np.random.randint(5,25,4) # min ra9m l ra9m 
ar3 = np.random.random((3,4))# min 0 ll 1  ydirelk 3 rows ou 4 coloms
ar4 = np.random.randint(1,20,(3,5))  # min 1 lel 20 3 rows 5 coloms

print(ar4)