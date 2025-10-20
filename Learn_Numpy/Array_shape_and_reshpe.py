import numpy  as np

# my_array =  np.array([[1,2,3,4],[5,6,7,8]])
# print(my_array.ndim)
# print(my_array.shape) # (rows ,coloms) 2d array but in 1d array (coloms)
# print(my_array.reshape())
# (chhal 3andek min array f dimension ta3ek,arrays ta3ek chhal fihom mon elemnet )

my_array =  np.array([
                      [[1,2,3,4,1],[5,6,7,8,1]],
                      [[11,12,13,14,1],[15,16,17,18,1]],
                     ])

print(my_array.ndim)
print(my_array.shape) 
print(my_array)

print('#'*50)

print( my_array.reshape(5,4)) # haka rahi 2d
print(my_array.reshape(2,5,2)) # haka rahi 3d
print(my_array.ndim)


# for x in my_array :
#     for n in x:
#         for f in n:
#             print(f)


'''
reshape(-1) :  tronsferm the array  to 1 dimension
 
'''
       