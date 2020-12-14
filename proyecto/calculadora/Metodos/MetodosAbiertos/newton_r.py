#Implementación del método de Newton
from . import conversor as cn #from arriba.Metodos.MetodosAbiertos import conversor as cn
from math import *
import sympy as sp

contenedor=[]       #arreglo contenedor contenedor[raices]
def Rnewton(cad, p0, tol, n):
    x = sp.Symbol('x')
    poli=cn.aTransformar(cad)
    devPoli= sp.diff(poli,x) # derivada - salida simbolica
    i = 1
    while i<=n:
        p = p0-cn.evaluar(poli,p0)/cn.evaluar(devPoli, p0)
        #print(" I ter = " , " %03d " % i, " ; p = " , " %.14f " % p)
        contenedor.append(p)
        if abs(p-p0) < tol:
            return contenedor
        p0 = p
        i += 1
    #print(" Iteraciones agotadas: Error!")
    return contenedor

#print(" \n" +r"-- Newton funcion expo(x):" +" \n")
#newton("x^3-3*x^2+2*x", 4.0, 1e-8, 100)

