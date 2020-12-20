#Implementación del método del punto fijo
from math import *
from . import conversor as cn
import sympy as sp

      #arreglo contenedor contenedor[raices]
def Rpuntofijo(cad,cadDesp, p0, tol, n): #Método del punto fijo
    f=cn.aTransformar(cad)
    g=cn.aTransformar(cadDesp)
    contenedor=[] 
    x = sp.Symbol('x')
    devGx= sp.diff(g,x) # derivada - salida simbolica
    
    condi1=sp.sympify(g).subs(x,p0)
    if abs(condi1)>1:
        return False
    
    iter = 1
    while iter<= n:
        ansDictionary = {
            "iter" : iter,
            "x0" : round(float(p0),10)
        }
        try:
            #if abs(cn.evaluar(devGx,p0)) < 1:
            #    return -1  #No converge
            p = cn.evaluar(g,p0)
            paux = cn.evaluar(f,p0)
            
            ansDictionary["fx0"] = round(float(paux),12)
            ansDictionary["gx0"] = round(float(p),12)
            
            errorAbs = abs(p-p0)
            if errorAbs <= tol:
                return contenedor
            ansDictionary["errorA"] = round(float(errorAbs),12)
            contenedor.append(ansDictionary)
            p0 = p
            iter +=1
        except TypeError:
            return -1   #No converge
    return contenedor

#pol(x), po = 0.9, tol = 10^-10, n=100

#puntofijo(pol_prima, 0, 0.00001, 12)
