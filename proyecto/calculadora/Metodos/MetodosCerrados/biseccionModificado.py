from . import conversor 
import sympy
def Rbiseccion(cad,lim1,lim2):    
    x=sympy.symbols('x')		#declaracion de variables
    poli=conversor.aTransformar(cad)        

    if(lim1>lim2):
        a,b=lim1,lim2
    else:
        b,a=lim1,lim2        
    error=10    # error
    i=0         #Contador
    contenedor=[]       #arreglo contenedor contenedor[raices]
    while error> 1e-6: #si el error es mayor de 4 decimales
        c=(a+b)/2
        fa=sympy.sympify(poli).subs(x,a)
        fc=sympy.sympify(poli).subs(x,c)
        if fc==0:
            raiz=c
            break
        elif fa*fc<0:
            b=c
        else:
            a=c
        raiz=c
        error=abs(fc)   #valor absoluto
        contenedor.append(raiz)
        i=i+1
    #print (contenedor)
    return contenedor

#biseccion("x^2+3x^3+2x^7",0,4)