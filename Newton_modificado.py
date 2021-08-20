from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr
import math

#6*log(x-0.1)**6+cos(x-0.1)-1.08
x=Symbol('x')

expr = input("Ingrese la funcion: ")#guarda expresion
y =	parse_expr(expr)#convierte tipo de variable

der = y.diff(x)#deriva
sec_der = der.diff(x)#segunda derivada

x0 = float(input("Ingrese el x0: "))

it=0
tol=1.e-3
it_max=100
x_v=1
while abs(x_v-x0)>tol and it<it_max:
#for k in range(0,6):
	libres=dict(x=x0)   #evalua funcion
	funcs = vars(math)	                                 #evalua en f(x0)
	fn=eval(expr, funcs,libres)#guarda resultado

	libres=dict(x=x0)   #evalua funcion derivada
	funcs = vars(math)	                                 #evalua en f'(x0)
	fn_der=eval(str(der), funcs,libres)#guarda resultado

	libres = dict(x=x0)   #evalua funcion derivada
	funcs = vars(math)	                                 #evalua en f''(x0)
	fn_sec_der = eval(str(sec_der), funcs,libres)#guarda resultado
	x_v = x0
	x0=x0-((fn*fn_der)/(fn_der**2-(fn*fn_sec_der)))
	
  	

	print(x0)







