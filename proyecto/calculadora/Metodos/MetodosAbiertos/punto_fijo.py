#Implementación del método del punto fijo
from math import *
from . import conversor as cn


contenedor=[]       #arreglo contenedor contenedor[raices]
def Rpuntofijo(cad, p0, tol, n): #Método del punto fijo
    f=cn.aTransformar(cad)
    i = 1
    while i<= n:
        p = cn.evaluar(f,p0)
        #print("Iter= ", "%03d" % i, "; p =", "%.14f" % p)
        contenedor.append(float(p))
        if abs(p-p0) < tol:
            return contenedor
        p0 = p
        i +=1
    #print("Iteraciones agotadas:Error!")
    return contenedor

#pol(x), po = 0.9, tol = 10^-10, n=100

#print("Pol prueba")
#puntofijo(pol_prima, 0, 0.00001, 12)
