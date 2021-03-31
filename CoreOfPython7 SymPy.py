# ******* Simpy : calculus *******
# SumPy Library allows to perform all types of computations symbolically
# it provides the calculs functionality(limits, differentation,...) Discrete mathematics and polynomial operations
# Solving various types of equations, the functionality of matrix representations and operations and geometric functions

# ******* Simpy Sample Functions *******

import sympy as sym
import math as m
x = sym.Symbol("x")
y, i, n, a, b = sym.symbols("y i n a b")

f = x**2+1
print(f.subs(x,2))

print(sym.expand((x+y)**3))
print(sym.simplify((x+x*y)/x))
print(sym.limit(sym.sin(x)/x,x,0))
print(sym.diff(x**4,x))
print(sym.integrate(6*x**5,x))
print(sym.solveset(x-1,x))
solution = sym.solve((x+5*y-2, -3*x+6*y-15),(x,y))
print(solution[x],solution[y])
# print(sym.integrate(m.exp(x) * m.sin(x)+m.exp(x) * m.cos(x),x))
# print(sym.summation(1/2**i,(i,0,sym.oo)))
# print(sym.summation(1/m.log(n)**n, (n,2, sym.oo)))
print(sym.summation(2*i-1, (i,1,n)))

a = (x + 1)**2 + 5*x
b = x**2 + 2*x + 4
print(sym.simplify(a-b))
func = x**2 + 2*x*y - 2*z
print(func.subs([(x,1),(y,6),(z,-1)]))
str_func = "2*x+1"
func = sympify(str_func)
print(func)

func = sin(x)
print(func.evalf(subs={x:1.2}))

print(factor(x**3 - x**2 + x-1))
print(factor(x**2*z + 4*x*y*z + 4*y**2*z))

print(sym.integrate(exp(-x**2 - y**2),(x,sym.oo,sym.oo),(y, -sym.oo, sym.oo)))
print(sym.Solvest(x-2, x))
print(sym.solvest(Eq(x-2,1),x))
m1 = sym.Matrix([[1,2,3],[3,2,1]])
m2 = sym.Matrix([0,1,1])
m2 = sym.Matrix([2,3,0])
print(m1)
print(m1*m2)
print(m2+m3)

m4 = sym.zeros(2,3)
m5 = sym.eye(3)
print(m4)
print(m5)
print(sym.ones(3,2))
print(sym.diag(1,2,3))

# ******* Plotting *******
from sympy import symbols
from sympy.plotting import plot
x = symbols('x')
plot(x**2,(x,-5,5))
plot((x**2,(x, -6, 6)),(x, (x, -5, 5)))

##########################################

plot(x**2, adaptive = False , nb_of_points=4)
plot(x**2, adaptive = False, nb_of_points=50)

##########################################

