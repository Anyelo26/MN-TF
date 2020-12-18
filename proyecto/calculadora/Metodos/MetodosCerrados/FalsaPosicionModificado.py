from . import conversor as cn
import sympy
def RfalsaPosicion(cad,a,b,iteraciones):
    if a<b:
        xi,xs=a,b
    else:
        xi,xs=b,a
    if iteraciones>=10:
        numeroIteraciones=10
    else:
        numeroIteraciones=iteraciones
    
    x=sympy.symbols('x')		#declaracion de variables
    poli=cn.aTransformar(cad)
    i=0

    ranterior=0
    error=100

    contenedor=[]           #arreglo contenedor principal,  almacena diccionarios por cada interación
    iter=0   
    while numeroIteraciones> 0: #si el error es mayor de 4 decimales
        iter=iter+1 #Valor de iteración que almacena el diccionario
        ansDictionary = {
            "iter" : iter,
            "xi" : round(float(xi),10),
            "xs" : round(float(xs),10)
        }
        fxi=sympy.sympify(poli).subs(x,xi)
        fxs=sympy.sympify(poli).subs(x,xs)

        ractual=(  xi*fxs-xs*fxi  )/(  fxs-fxi  )
        cond=fxi*fxs

        if cond<0:
            xi=ractual
        elif cond>=0:
            xs=ractual
        
        if i!=0:
            error=abs(((ractual - ranterior)/ractual)*100)
        ranterior=ractual
        i=i+1
        numeroIteraciones=numeroIteraciones-1        
        ansDictionary["errorRel"] = round(float(error),10)
        contenedor.append(ansDictionary)                
    return contenedor        