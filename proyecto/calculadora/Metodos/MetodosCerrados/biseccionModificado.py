from . import conversor 
import sympy
def Rbiseccion(cad,lim1,lim2):    
    x=sympy.symbols('x')		#declaracion de variables
    poli=conversor.aTransformar(cad)        
    
    if(lim1<lim2):
        a,b=lim1,lim2
    else:
        b,a=lim1,lim2        
    
    condi1=(sympy.sympify(poli).subs(x,a)>0 and sympy.sympify(poli).subs(x,b)<0)
    condi2=(sympy.sympify(poli).subs(x,a)<0 and sympy.sympify(poli).subs(x,b)>0)
    if not(condi1 or condi2):
        return False
    
    error=10    # error
    iter=1         #Contador de iteracion
    contenedor=[]       #arreglo contenedor contenedor[raices]
    while error> 1e-6: #si el error es mayor de 4 decimales
        ansDictionary = {
            "iter" : iter,
            "xi" : round(float(a),10),
            "xs" : round(float(b),10)
        }
        c=(a+b)/2  #Hallar nueva raiz
        fa=sympy.sympify(poli).subs(x,a)
        fc=sympy.sympify(poli).subs(x,c)

        
        if fc==0:
            ansDictionary["xr"] = round(float(c),10)
            ansDictionary["fxa"] = round(float(fa),10)
            ansDictionary["fxr"] = round(float(fc),10)

            break
        elif fa*fc<0:
            b=c
        else:
            a=c
        ansDictionary["xr"] = round(float(c),10)
        ansDictionary["fxa"] = round(float(fa),10)
        ansDictionary["fxr"] = round(float(fc),10)
        error=abs(fc)   #valor absoluto
        contenedor.append(ansDictionary)
        iter=iter+1
    
    return contenedor

#biseccion("x^2+3x^3+2x^7",0,4)