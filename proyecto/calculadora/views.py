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
#---------Para funcion plot----
from calculadora.Metodos.MetodosAbiertos.conversor import aTransformar, evaluar
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
#-------------------------------------#
#Variable global para almacenar funcion
FUNCTION = ""
def getF(): 
    global FUNCTION
    return FUNCTION
def setF(f):
    global FUNCTION
    FUNCTION = f
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
def Biseccion(request):    
    try: 
        abc= request.POST['pol'] 
        setF(abc)
        a= int( request.POST['a'] )
        b= int( request.POST['b'] )
        resp= Rbiseccion(abc,a,b)
        return render(request,'biseccion/resultado.html',{'resp':resp})
    except ValueError:
        myError = {
            "error" :True,
            "message": "No se permiten letras"
        }
        return render(request,'biseccion/resultado.html',context=myError)

def FalsaPosicion(request): 
    try:
        abc= request.POST['pol'] 
        setF(abc)
        a= int( request.POST['a'] )
        b= int( request.POST['b'] )
        iteraciones= int( request.POST['iteraciones'] )

        resp= RfalsaPosicion(abc,a,b,iteraciones)

        return render(request,'falsaposicion/resultado.html',{'resp':resp})
    except ValueError:
        myError = {
            "error" :True,
            "message": "No se permiten letras"
        }
        return render(request,'falsaposicion/resultado.html',context=myError)
    
def Newton(request): 
    try:   
        abc= request.POST['pol']
        setF(abc)
        puntoInit= float( request.POST['pInicial'] )
        tol= float( request.POST['tol'] )
        iteraciones= int( request.POST['iteraciones'] )
        resp= Rnewton(abc,puntoInit,tol,iteraciones)
        if ( resp == -1):
            raise MyErrorInMethod("No converge")
        return render(request,'newton/resultado.html',{'resp':resp})    
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

def PuntoFijo(request): 
    try: 
        pol= request.POST['pol']
        polD= request.POST['polDespejado']
        setF(pol)
        puntoInit= float( request.POST['pInicial'] )
        tol= float( request.POST['tol'] )
        iteraciones= int( request.POST['iteraciones'] )
        resp= Rpuntofijo(pol,polD,puntoInit,tol,iteraciones)
        if ( resp == -1):
            raise MyErrorInMethod("No converge")
        return render(request,'puntofijo/resultado.html',{'resp':resp})
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

def Secante(request): 
    funcion= request.POST['pol']
    setF(funcion)
    p0= float( request.POST['x0'] )
    p1= float( request.POST['x1'] )
    tol= float( request.POST['tol'] )
    n= int( request.POST['iter'] )
    
    resp= Rsecante(funcion,p0,p1,tol,n)
    return render(request,'secante/resultado.html',{'resp':resp})    

def plot(request):
    funcionF = aTransformar(getF())
    #print(funcionF)
    x= np.arange(-10,10,0.01)
   # fx = lambda x: funcionF
    fig=Figure()
    
     # Creamos los ejes
    ax = fig.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    ax.plot(x, [evaluar(funcionF, i) for i in x])
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title("Mi función: " + "$"+getF()+"$")
    ax.grid()

    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    # Devolvemos la response
    return response

#https://www.youtube.com/watch?v=KOZY1-rLauc&list=PLS1QulWo1RIZz1aTTzz17L6rmN2ML3_p-&index=21  %CALCULATOR RESPUESTA 1
# https://www.youtube.com/watch?v=lgI6qvSGkSk&list=PLpOqH6AE0tNgL7Jg9Kx4SdfA5_oK6292j&index=23 %Como imprimir la lista 