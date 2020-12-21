from . import conversor as cn
import sympy
from cmath import sqrt

contenedor=[]
susti=[]


def Rmuller(abc, a,b,c,tolerancia):    	
	x0=float(a)
	x1=float(b)
	x2=float(c)
	
	x,poli=sympy.symbols('x'),cn.aTransformar(abc)	
	errorPor=100
	iter=0
	while (errorPor>tolerancia):
		iter = iter+1
		ansDictionary = {
            "iter" : iter
        }
		f0=sympy.sympify(poli).subs(x,x0)
		#print(f0,"este es f0")
		f1=sympy.sympify(poli).subs(x,x1)
		#print(f1,"este es f1")
		f2=sympy.sympify(poli).subs(x,x2)
		#print(f2,"este es f2")


		h0 = x1 - x0
		#print(h0,"este es h0")
		h1 = x2 - x1
		#print(h1,"este es h1")
		if(h0==0 or h1==0):
				return False
		
		d0 = (f1 - f0) / h0
		#print(d0,"este es d0")
		d1 = (f2 - f1 )/ h1
		#print(d1,"este es d1")

		a = (d1-d0) / (h1+h0)
		#print(a,"este es a")
		b= a*h1 + d1
		#print(b,"este es b")
		c= f2
		#print(c,"este es c")
		rDisc=sqrt(b*b-4*a*c)
		x3=0.0
		temp1=b + rDisc
		temp2=b - rDisc
		if( b<0):
				x3=x2+(-2*c)/ (b - rDisc)	
		else:
				x3=x2+(-2*c)/ (b + rDisc)
		##Calculo del error
		#print(x3,"este es x3")
		
		errorPor=float(abs((x3-x2)/x3)*100)
		ansDictionary["errorP"] = round(float(errorPor),12)
		ansDictionary["x3"] = round(float(x3),12)
		'''
		######### ERROR EN LA AGREGACION DE SUSTI
		susti[0]=x3
		susti[1]=errorPor
		contenedor.append(susti)
		##########
		'''
		################
		contenedor.append(ansDictionary)
		#contenedor.append(errorPor)
		##########
		x0=x1
		x1=x2
		x2=x3	
	return contenedor	

#abc="x^3-13x-12"
#print(muller(abc,4.5,5.5,5,0.01))