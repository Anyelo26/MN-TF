from . import conversor as cn
import sympy as sp

from math import*
#las funciones deberia 
#funcion,numero anterior,numero actual,tolerancia,numero maximo de iteraciones
def evaluar(poli, p0):
    x=sp.symbols('x')
    val = sp.sympify(poli).subs(x,p0)
    return val

contenedor=[]
def Rsecante(fn,p0,p1,tolerancia,n):
    funcion=cn.aTransformar(fn)    
    i=1
    while i<=n:
        #p=p1-(funcion(p1)*(p1-p0))/(funcion(p1)-funcion(p0))  
        #p=p1-(funcion(p1)*(p1-p0))/(funcion(p1)-funcion(p0))  
        p=p1-(evaluar(funcion,p1)*(p1-p0))/(evaluar(funcion,p1)-evaluar(funcion,p0))
        contenedor.append(p)
        #print("Iteracion: ", i, "; raiz: ", p)
        if abs(p1-p0)<tolerancia:
            return p
        p0=p1
        p1=p
        i+=1
    #print("Iteraciones agotadas")
    return contenedor

#secante("x^3+2x",-3.0,3.0,1e-10,100)