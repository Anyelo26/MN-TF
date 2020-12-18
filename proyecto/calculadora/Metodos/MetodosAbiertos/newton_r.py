#Implementación del método de Newton
from . import conversor as cn #from arriba.Metodos.MetodosAbiertos import conversor as cn
from math import *
import sympy as sp

def Rnewton(cad, p0, tol, n):
    x = sp.Symbol('x')
    poli=cn.aTransformar(cad)
    devPoli= sp.diff(poli,x) # derivada - salida simbolica
    contenedor=[]       #arreglo contenedor contenedor[raices]
    iter = 1
    while iter<=n:
        ansDictionary = {
            "iter" : iter,
            "xi" : round(float(p0),10)
        }
        fxi = cn.evaluar(poli,p0)
        fxidiff = cn.evaluar(devPoli, p0)
        try:
            p = p0-(fxi/fxidiff)  #evaluar newton formula

            ansDictionary["fxi"] = round(float(fxi),12)
            ansDictionary["fxidiff"] = round(float(fxidiff),12)
            ansDictionary["xii"] = round(float(p),12)

            errorAbs = abs(p-p0)
            if errorAbs <= tol:
                return contenedor
            ansDictionary["errorA"] = round(float(errorAbs),12)
            contenedor.append(ansDictionary)
            p0 = p
            iter += 1
        except TypeError:
            return -1   #No converge
    return contenedor


#print(" \n" +r"-- Newton funcion expo(x):" +" \n")
#newton("x^3-3*x^2+2*x", 4.0, 1e-8, 100)

