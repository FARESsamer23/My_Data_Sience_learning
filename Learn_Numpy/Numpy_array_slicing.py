import numpy as np

#slicing => [start:End:steps] not include End 

a = np.array(["a","b","c","d","e","f","g"]);
print(a.ndim)
print(a[1])
print(a[1:4])
print(a[:4])
print(a[1::2])
print("#"*50)

b = np.array([["a","b"],["c","d"],["f","g"]])
print(b.ndim)
print(b[1])
print(b[1:4])
print(b[:4])
print(b[1::])
print("#"*50)
print(b[-2:,0])






