import numpy as np


def np_arr(x, y):

    arr = np.random.rand(x, y) #to create array
    print(arr)

np_arr(4, 5)


print("####  ####  ####  ####  ####  ####  ####  ####  ####  ####")
temp_list = [12, 13, 14, 15, 16, 17, 18, 19, 20]
new_arr = np.array(temp_list)
print(new_arr)
print("####  ####  ####  ####  ####  ####  ####  ####  ####  ####")
new_arr_resize = np.resize(new_arr, (2, 5))
print(new_arr_resize)
