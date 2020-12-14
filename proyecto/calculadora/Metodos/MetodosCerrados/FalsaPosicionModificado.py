from . import conversor as cn
import sympy
def RfalsaPosicion(cad,a,b,iteraciones):
    if a>b:
        xi,xs=a,b
    else:
        xi,xs=b,a
    if iteraciones>10:
        numeroIteraciones=10
    else:
        numeroIteraciones=iteraciones
    
    x=sympy.symbols('x')		#declaracion de variables
    poli=cn.aTransformar(cad)
    i=0

    ranterior=0
    error=100

    contenedor=[]           #arreglo contenedor contenedor principal
    valores=[0,0,0,-1]      #arreglo contenedor secundario valores[xi,xs,iteracions,error]
    while numeroIteraciones> 0: #si el error es mayor de 4 decimales
        valores[0]=xi
        valores[1]=xs
        fxi=sympy.sympify(poli).subs(x,xi)
        fxs=sympy.sympify(poli).subs(x,xs)

        ractual=(  xi*fxs-xs*fxi  )/(  fxs-fxi  )
        cond=fxi*fxs

        if cond<0:
            xs=ractual
        elif cond>=0:
            xi=ractual
        
        if i!=0:
            error=abs(((ractual - ranterior)/ractual)*100)
        ranterior=ractual
        i=i+1
        numeroIteraciones=numeroIteraciones-1        
        
        valores[2]=ractual 
        valores[3]=error
        contenedor.append(valores)                
        #dibujaMatriz(contenedor)
    return contenedor        