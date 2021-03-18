# ******* Numpy General *******
import numpy as np
a = np.array([0,30,45,60,90])
b = np.array([1.0,5.55,123,0.567,25.532])
print("sin(a) :", np.sin(a*np.pi))
print("b around :", np.around(b))
print("b around 1:", np.around(b, decimals = 1))
print("b around 2:", np.around(b, decimals = 2))
print("b floor :", np.floor(b))
print("b ceil :", np.ceil(b))

print("cos(pi) :", np.cos(np.pi))
print("tan(pi) :", np.tan(np.pi))
print("arcsin :", np.arcsin(np.pi/100))
print("degrees(pi) :", np.degrees(np.pi))

# ******* Numpy Array *******
b = np.array([1,4,7,5])
print(b)

c= np.array([[1,4,7,5],[2,0,3,2]])
print(c)

a = np.arange(12).reshape(3,4)
print(a)
print("a size : ", a.size)
print("a shape :", a.shape)
print("a ndim : ", a.ndim)
print("a dtype.name :", a.dtype.name)
print("a itemsize: ", a.itemsize) #in bytes

d = np.array([(1.5,2,3),(4,5,6)])
print(d)

f = np.array([[1,2],[3,4]], dtype = complex)
print(f)

e = np.zeros((4,10))
print(e)

g = np.ones((2,4), dtype=np.int16)
print(g)

i= np.arange(0,2,0.3)
print(i)

j = np.arange(24).reshape(2,3,4)
print(j)
##############################################
a = np.array([1,-1,7,3])
b = np.array([-9,4,0,5])
c = np.array([[10,6,0,2],[1,2,3,4]])
print("a-b:", a-b)
print("a*b:", a*b)
print("a.dot(b):", a.dot(b))
print("a*2:", a*2)
print("np.sin(a):",np.sin(a))
print("a<3:", a<3)
print("a.sum() :", a.sum())
print("a.min() :",a.min())
print("a.max() :",a.max())
print("a.mean() :", a.mean())
print("a average():", np.average(a))
print("a median() :", np.median(a))
print("a std() :",np.std(a))
print("a var() :", np.var(a))
print("c.cumsum() :", c.cumsum())
print("a[1:2] :", a[1:2])
print("a[2:] :", a[2:])
print("c[-1] :",c[-1])
##############################################
a = np.array([('Rex',9,81.9),
              ('Fido',3,27.0),
              ('Fox', 47,70)],
             dtype = [('name','U1O'),
                      ('age','i4'),
                      ('weight','f4')])

print("sort by age :")
print(np.sort(a, order='age'))
print('\n')
print("sort by weight, then name if ages are equal:")
print(np.sort(a, order=["weight","name"]))










