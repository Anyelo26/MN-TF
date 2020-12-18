from . import conversor as cn
import sympy as sp

from math import*
#las funciones deberia 
#funcion,numero anterior,numero actual,tolerancia,numero maximo de iteraciones


def Rsecante(fn,p0,p1,tolerancia,n):
    funcion=cn.aTransformar(fn)   
    contenedor=[]
    iter=1
    while iter<=n:
        ansDictionary = {
            "iter" : iter,
            "p0" : round(float(p0),10),
            "p1" : round(float(p1),10)
        }
        try:
            fp0=cn.evaluar(funcion,p0)
            fp1=cn.evaluar(funcion,p1)
            p=p1-(fp1*(p1-p0))/(fp1-fp0)
            ansDictionary["fp0"] = round(float(fp0),12)
            ansDictionary["fp1"] = round(float(fp1),12)
            ansDictionary["p2"] = round(float(p),12)

            errorAbs = abs(p1-p0)
            if errorAbs<tolerancia:
                return contenedor
            ansDictionary["errorA"] = round(float(errorAbs),12)
            contenedor.append(ansDictionary)
            p0=p1
            p1=p
            iter+=1
        except TypeError:
            return -1   #No converge
    #print("Iteraciones agotadas")
    return contenedor

#secante("x^3+2x",-3.0,3.0,1e-10,100)