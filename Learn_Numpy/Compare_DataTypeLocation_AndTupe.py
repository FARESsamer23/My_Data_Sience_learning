import numpy as np


my_list = [1,3,2,5,6]

my_array = np.array(my_list)


print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_list[2]))

print(id(my_array[0]))
print(id(my_array[1]))
print(id(my_array[2]))
# Elements of numpy array are in the same place in memory  reversed array  is not possible
# we should  manipulate data all in the same homogenieus  data type in numpy




print("#"*50)
