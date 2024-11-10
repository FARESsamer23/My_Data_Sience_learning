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
print(b[0::2]) #  min index 0 lel tali bl pas 2
print("#"*50)
print(b[-2:,0])
# expamle brk a[:1,2] = 4 ma3aha  kamel les rows el 3mod 2  hatli fihom 4
# ne9der nhadd 3onser  juste by slicing 
#print(b[1::2,0]) # 2nd row 1st col
# v = b[a>50]  return array of elements > 50  swith your condition






