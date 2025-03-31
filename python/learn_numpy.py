import numpy as np

# creating array (ndarray)
a = np.array(1)
b = np.array([1,2,3,4,5])
c = np.array([[1,2],[3,4],[5,6]])
d = np.array([[[1,2], [3,4]],[[5,6],[7,8]]])
e = np.array([7,8,9], ndmin=4)
print(a.ndim, a)
print(b.ndim, b)
print(c.ndim, c)
print(d.ndim, d)
print(e.ndim, e)

#access
print(c[0,0]) # 1
print(d[0,1,0]) # 3
print(c[1,-1]) # 4

#shape = no. of elements in each dimension
print(e.shape) # (1,1,1,3)
print(c.shape) # (3,2)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(4,3))

# iteration
arr = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
for x in np.nditer(arr):
    print(x)

# sort(array,axis,kind,order)
arr = np.array([
    [7,1,4],
    [8,6,5],
    [1,2,3]
])
print(np.sort(arr))
'''
[[1 4 7]
 [5 6 8]
 [1 2 3]]
'''
print(np.sort(arr, axis=None))
# [1 1 2 3 4 5 6 7 8]
print(np.sort(arr, axis=0))
'''
[[1 1 3]
 [7 2 4]
 [8 6 5]]
'''

#sorted => returns a new list
arr = np.array([1,4,2,5,8,6,9,3,10])
newArr = sorted(arr)
print('original:', arr, type(arr))
print('new:', newArr, type(newArr))
'''
original: [ 1  4  2  5  8  6  9  3 10] <class 'numpy.ndarray'>
new: [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(8), np.int64(9), np.int64(10)] <class 'list'>
'''

# argsort => returns ndarray
arr = np.array([1,4,2,5,8,6,9,3,10])
newArr = np.argsort(arr)
print('original:', arr, type(arr))
print('new:', newArr, type(newArr)) # sorted indices of original
'''
original: [ 1  4  2  5  8  6  9  3 10] <class 'numpy.ndarray'>
new: [0 2 7 1 3 5 4 6 8] <class 'numpy.ndarray'>
'''