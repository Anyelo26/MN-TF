from . import conversor as cn
import sympy
def RfalsaPosicion(cad,a,b,iteraciones):
    if a<b:
        xi,xs=a,b
    else:
        xi,xs=b,a
    if iteraciones>=8:
        numeroIteraciones=8
    else:
        numeroIteraciones=iteraciones
    
    x=sympy.symbols('x')		#declaracion de variables
    poli=cn.aTransformar(cad)

    ranterior=0
    error=100

    contenedor=[]           #arreglo contenedor principal,  almacena diccionarios por cada interación
    iter=1   
    while numeroIteraciones> 0: #si el error es mayor de 4 decimales
        ansDictionary = {
            "iter" : iter,
            "xi" : round(float(xi),10),
            "xs" : round(float(xs),10)
        }
        fxi=sympy.sympify(poli).subs(x,xi)
        fxs=sympy.sympify(poli).subs(x,xs)

        ractual= xs - (( fxs*(xi - xs) )/(  fxi-fxs  ))
        ansDictionary["fxi"] = round(float(fxi),10)
        ansDictionary["fxs"] = round(float(fxs),10)
        ansDictionary["xr"] = round(float(ractual),10)
        cond=fxi*fxs
        if cond<0:
            xi=ractual
        elif cond>0:
            xs=ractual
        
        if iter-1!=0:
            error=abs(((ractual - ranterior)/ractual)*100)
        ranterior=ractual
        iter=iter+1
        numeroIteraciones=numeroIteraciones-1        
        ansDictionary["errorRel"] = round(float(error),10)
        contenedor.append(ansDictionary)                
    return contenedor        