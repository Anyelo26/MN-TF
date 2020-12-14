######################33
#	parte funcional 
#
#############################

########################################
### Funcion encargada de convertir linea de caracteres a string para conversion a polinomio
from sympy.parsing.sympy_parser import parse_expr									#conversor de String-Funcion
from sympy.parsing.sympy_parser import standard_transformations						#importacion de Conversor a String
from sympy.parsing.sympy_parser import implicit_multiplication_application			#importacion de Transformation estandar para polinomio
import sympy as sp

def condic(pol): #funcion que detecta caracteres
	return pol.find("^")    # retorna posicion de caracter, -1 si no se encuentra

def conversion(pol): #funcion recursiva de concatenamiento de nuevo String para polinomio
	eo=condic(pol)
	if eo<0:
		return pol
	else:
		temp1=pol[0:eo]
		temp2=pol[eo+1:len(pol)]
		pol=temp1+"**"+temp2		
	return conversion(pol)  #retorna String polinomio cambiado
def aTransformar(cad):
	transformations=(standard_transformations+(implicit_multiplication_application,))	#almacenamiento de conversion a polinomio + 
	var=parse_expr(conversion(cad),transformations=transformations)	#variable que trabaja con String, y la conversion del polinomio
	return var

#pol= input("ingrese polinomio: ")
#print(aTransformar(pol))

##Evaluar la función generada en un punto
def evaluar(poli, p0):
    x=sp.symbols('x')
    val = sp.sympify(poli).subs(x,p0)
    return val