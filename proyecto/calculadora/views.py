import django
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

#--------Metodos Numericos---------
from calculadora.Metodos.MetodosCerrados.biseccionModificado import Rbiseccion
from calculadora.Metodos.MetodosCerrados.FalsaPosicionModificado import RfalsaPosicion
from calculadora.Metodos.MetodosAbiertos.newton_r import Rnewton
from calculadora.Metodos.MetodosAbiertos.punto_fijo import Rpuntofijo
from calculadora.Metodos.MetodosAbiertos.secante import Rsecante
from calculadora.Metodos.MetodosPolinomios.Bairstow import Rbairstow
from calculadora.Metodos.MetodosPolinomios.Muller import Rmuller
#---------Para funcion plot----

from calculadora.Metodos.MetodosAbiertos.conversor import aTransformar, evaluar
import numpy as np

#-------------------------------------#
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from bokeh.layouts import gridplot  #firstly import gridplot
#Variable global para almacenar funcion
FUNCTION = ""
RAICES = []
TYPEMETHOD = 0
def getF(): 
    global FUNCTION
    return FUNCTION
def setF(f):
    global FUNCTION
    FUNCTION = f
def getMethod(): 
    global TYPEMETHOD
    return TYPEMETHOD
def setMethod(n):
    global TYPEMETHOD
    TYPEMETHOD = n
def getRaices(): 
    global RAICES
    return RAICES
def setRaices(r):
    global RAICES
    RAICES = r
#-------------------------------------#
# Create your views here.

class index(TemplateView):
    template_name = 'index.html'

class curso(TemplateView):
    template_name = 'curso.html'

class tema(TemplateView):
    template_name = 'tema.html'

class indice(TemplateView):
    template_name = 'indice.html'

class quiz(TemplateView):
    template_name='quiz.html'

class biseccion(TemplateView):
    template_name='biseccion/tema.html'

class falsaposicion(TemplateView):
    template_name = 'falsaposicion/tema.html'

class puntofijo(TemplateView):
    template_name = 'puntofijo/tema.html'

class secante(TemplateView):
    template_name = 'secante/tema.html'

class newton(TemplateView):
    template_name = 'newton/tema.html'

class muller(TemplateView):
    template_name = 'muller/tema.html'

class bairstow(TemplateView):
    template_name = 'bairstow/tema.html'

class biseccionCalculadora(TemplateView):
    template_name = 'biseccion/calculadora.html'
   
class falsaposicionCalculadora(TemplateView):
    template_name = 'falsaposicion/calculadora.html'

class puntofijoCalculadora(TemplateView):
    template_name = 'puntofijo/calculadora.html'

class secanteCalculadora(TemplateView):
    template_name = 'secante/calculadora.html'

class newtonCalculadora(TemplateView):
    template_name = 'newton/calculadora.html'

class mullerCalculadora(TemplateView):
    template_name = 'muller/calculadora.html'

class bairstowCalculadora(TemplateView):
    template_name = 'bairstow/calculadora.html'

class MyErrorInMethod(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
#.----------Funcione para ver resultados-------------------
def Biseccion(request):     #TYPEMETHOD=1
    try: 
        abc= request.POST['pol'] 
        a= int( request.POST['a'] )
        b= int( request.POST['b'] )
        resp= Rbiseccion(abc,a,b)
        if (resp ==-1):
            myError = {
            "error" :True,
            "message": "Prueba con otro intervalo"
            }
            return render(request,'biseccion/resultado.html',context=myError)
        raices = []
        for r in resp:
            raices.append(r["xr"])
        setRaices(raices)
        setMethod(1)
        setF(abc)
        return render(request,'biseccion/resultado.html',{'resp':resp, 'pol':getF()})
    except ValueError:
        myError = {
            "error" :True,
            "message": "Revise los datos ingresados, intente nuevamente."
        }
        return render(request,'biseccion/resultado.html',context=myError)

def FalsaPosicion(request):  #TYPEMETHOD=2
    try:
        abc= request.POST['pol'] 
        a= int( request.POST['a'] )
        b= int( request.POST['b'] )
        iteraciones= int( request.POST['iteraciones'] )
        resp= RfalsaPosicion(abc,a,b,iteraciones)
        raices = []
        for r in resp:
            raices.append(r["xr"])
        setRaices(raices)
        setMethod(2)
        setF(abc)
        return render(request,'falsaposicion/resultado.html',{'resp':resp, 'pol':getF()})
    except ValueError:
        myError = {
            "error" :True,
            "message": "Revise los datos ingresados, intente nuevamente."
        }
        return render(request,'falsaposicion/resultado.html',context=myError)
    
def Newton(request):  #TYPEMETHOD=3
    try:   
        abc= request.POST['pol']
        puntoInit= float( request.POST['pInicial'] )
        tol= float( request.POST['tol'] )
        iteraciones= int( request.POST['iteraciones'] )
        resp= Rnewton(abc,puntoInit,tol,iteraciones)
        if ( resp == -1):
            raise MyErrorInMethod("No converge")
        raices = []
        for r in resp:
            raices.append(r["xii"])
        setRaices(raices)
        setMethod(3)
        setF(abc)

        return render(request,'newton/resultado.html',{'resp':resp, 'pol':getF()})    
    except ValueError:
        myError = {
            "error" :True,
            "message": "No se permiten letras"
        }
        return render(request,'newton/resultado.html',context=myError)
    except MyErrorInMethod as e:
        myError = {
            "error" :True,
            "message": e.mensaje
        }
        return render(request,'newton/resultado.html',context=myError)

def PuntoFijo(request):  #TYPEMETHOD=4
    try: 
        pol= request.POST['pol']
        polD= request.POST['polDespejado']
        puntoInit= float( request.POST['pInicial'] )
        tol= float( request.POST['tol'] )
        iteraciones= int( request.POST['iteraciones'] )
        resp= Rpuntofijo(pol,polD,puntoInit,tol,iteraciones)
        
        if ( resp == -1):
            raise MyErrorInMethod("No converge")
        raices = []
        for r in resp:
            raices.append(r["x0"])
        setRaices(raices)
        setMethod(4)
        setF(pol)    
        return render(request,'puntofijo/resultado.html',{'resp':resp, 'pol':getF()})
    except ValueError:
        myError = {
            "error" :True,
            "message": "No se permiten letras"
        }
        return render(request,'puntofijo/resultado.html',context=myError)
    except MyErrorInMethod as e:
        myError = {
            "error" :True,
            "message": e.mensaje
        }
        return render(request,'puntofijo/resultado.html',context=myError)

def Secante(request):       #TYPEMETHOD=5
    try:
        funcion= request.POST['pol']
        p0= float( request.POST['x0'] )
        p1= float( request.POST['x1'] )
        tol= float( request.POST['tol'] )
        n= int( request.POST['iter'] )
        
        resp= Rsecante(funcion,p0,p1,tol,n)
        raices = []
        for r in resp:
            raices.append(r["p2"])
        setRaices(raices)
        setMethod(5)
        setF(funcion)
        return render(request,'secante/resultado.html',{'resp':resp, 'pol':getF()})
    except ValueError:
        myError = {
            "error" :True,
            "message": "No se permiten letras"
        }
        return render(request,'puntofijo/resultado.html',context=myError)

def Muller(request):       #TYPEMETHOD=6
    try:
        funcion= request.POST['pol']
        p0= float( request.POST['x0'] )
        p1= float( request.POST['x1'] )
        p2= float( request.POST['x2'] )
        tol= float( request.POST['tol'] )
        
        resp= Rmuller(funcion,p0,p1,p2,tol)
        raices = []
        for r in resp:
            raices.append(r["x3"])
        setRaices(raices)
        setMethod(6)
        setF(funcion)
        return render(request,'muller/resultado.html',{'resp':resp, 'pol':getF()})
    except ValueError:
        myError = {
            "error" :True,
            "message": "No se permiten letras"
        }
        return render(request,'muller/resultado.html',context=myError)

def Bairstow(request):       #TYPEMETHOD=7
    try: 
        r= float( request.POST['r'] )
        s= float( request.POST['s'] )
        coefs = []
        coef= float( request.POST['coef1'] )
        coef2= float( request.POST['coef2'] )
        coef3= float( request.POST['coef3'] )
        coefs.append(coef)
        coefs.append(coef2)
        coefs.append(coef3)
        resp = Rbairstow(coefs,r,s,2,[])
        return render(request,'bairstow/resultado.html',{'resp':resp})
    except ValueError:
        myError = {
            "error" :True,
            "message": "No se permiten letras"
        }
        return render(request,'bairstow/resultado.html',context=myError)

def graficar(request):
    funcionF = aTransformar(getF())
    #Funcion
    x= np.arange(-10,10,0.01)
    y0 = [float (evaluar(funcionF, i)) for i in x]
    #Raices
    xR = getRaices()
    yR = [float (evaluar(funcionF, i)) for i in xR]
    xFinal = xR[len(xR)-1]
    yFinal = float (evaluar(funcionF, xFinal)) 
    #Graficas
    titulodePlot = "Mi función: " + getF()
    plot = figure(title=titulodePlot)
    plot.line(x,y0, legend="Funcion f(x)", line_color="blue")
    plot.circle(xR,yR, legend="Raiz", fill_color="red", size=5)
    plot.circle(xFinal,yFinal, legend="Última raiz", fill_color="yellow", size=6)
    p4 = gridplot([[plot]])
    script, div = components(p4)
    
    if getMethod()==1: 
        return render(request, 'biseccion/grafica.html',{'script':script, 'div':div, 'pol':getF()})
    elif getMethod()==2:
        return render(request, 'falsaposicion/grafica.html',{'script':script, 'div':div, 'pol':getF()})
    elif getMethod()==3:
        return render(request, 'newton/grafica.html',{'script':script, 'div':div, 'pol':getF()}) 
    elif getMethod()==4:
        return render(request, 'puntofijo/grafica.html',{'script':script, 'div':div, 'pol':getF()}) 
    elif getMethod()==5:
        return render(request, 'secante/grafica.html',{'script':script, 'div':div, 'pol':getF()}) 
    elif getMethod()==6:
<<<<<<< HEAD
        return render(request, 'muller/grafica.html',{'script':script, 'div':div, 'pol':getF()}) 
    elif getMethod()==7:
        return render(request, 'bairstow/grafica.html',{'script':script, 'div':div}) 


def graficaInit(request):
    tipo = float(request.POST['metodo'])
    setMethod(tipo)
    if getMethod()==7:
        coefs = []
        coef= float( request.POST['coef1'] )
        coef2= float( request.POST['coef2'] )
        coef3= float( request.POST['coef3'] )
        coefs.append(coef)
        coefs.append(coef2)
        coefs.append(coef3)
        funcion = polinomio(coefs)
    else:
        funcion = request.POST['pol']
    
    funcionF = aTransformar(funcion)
    #Funcion
    x= np.arange(-10,10,0.01)
    y0 = [float (evaluar(funcionF, i)) for i in x]
   
    #Graficas
    titulodePlot = "Mi función: " + funcion
    plot = figure(title=titulodePlot)
    plot.line(x,y0, legend="Funcion f(x)", line_color="blue")
    p4 = gridplot([[plot]])
    script, div = components(p4)
    
    if getMethod()==1: 
        return render(request, 'biseccion/grafica.html',{'script':script, 'div':div, 'pol':funcion})
    elif getMethod()==2:
        return render(request, 'falsaposicion/grafica.html',{'script':script, 'div':div, 'pol':funcion})
    elif getMethod()==3:
        return render(request, 'newton/grafica.html',{'script':script, 'div':div, 'pol':funcion}) 
    elif getMethod()==4:
        return render(request, 'puntofijo/grafica.html',{'script':script, 'div':div, 'pol':funcion}) 
    elif getMethod()==5:
        return render(request, 'secante/grafica.html',{'script':script, 'div':div, 'pol':funcion}) 
    elif getMethod()==6:
        return render(request, 'muller/grafica.html',{'script':script, 'div':div, 'pol':funcion}) 
    elif getMethod()==7:
        return render(request, 'bairstow/grafica.html',{'script':script, 'div':div}) 
  
=======
        return render(request, 'muller/grafica.html',{'script':script, 'div':div}) 
    
>>>>>>> parent of eab7032... Merge branch 'main' of https://github.com/Anyelo26/MN-TF into main
#https://www.youtube.com/watch?v=KOZY1-rLauc&list=PLS1QulWo1RIZz1aTTzz17L6rmN2ML3_p-&index=21  %CALCULATOR RESPUESTA 1
# https://www.youtube.com/watch?v=lgI6qvSGkSk&list=PLpOqH6AE0tNgL7Jg9Kx4SdfA5_oK6292j&index=23 %Como imprimir la lista 
#https://stackoverrun.com/es/q/9673979