# from django.shortcuts import redirect
import django
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
#from django.contrib.auth.models import User, auth
#from calculadora.models import Metodo
#from django.http import HttpResponse
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

#.----------Funcione para ver resultados-------------------
def Biseccion(request):    
    abc= request.POST['pol'] 
    setF(abc)
    a= int( request.POST['a'] )
    b= int( request.POST['b'] )
    resp= Rbiseccion(abc,a,b)
    return render(request,'biseccion/resultado.html',{'resp':resp})
def FalsaPosicion(request): 
    abc= request.POST['pol'] 
    setF(abc)
    a= int( request.POST['a'] )
    b= int( request.POST['b'] )
    iteraciones= int( request.POST['iteraciones'] )
    resp= RfalsaPosicion(abc,a,b,iteraciones)
    return render(request,'falsaposicion/resultado.html',{'resp':resp})    
    
def Newton(request):    
    abc= request.POST['pol']
    setF(abc)
    puntoInit= float( request.POST['pInicial'] )
    tol= float( request.POST['tol'] )
    iteraciones= int( request.POST['iteraciones'] )
    resp= Rnewton(abc,puntoInit,tol,iteraciones)
    return render(request,'newton/resultado.html',{'resp':resp})    

def PuntoFijo(request): 
    abc= request.POST['pol']
    setF(abc)
    puntoInit= float( request.POST['pInicial'] )
    tol= float( request.POST['tol'] )
    iteraciones= int( request.POST['iteraciones'] )
    resp= Rpuntofijo(abc,puntoInit,tol,iteraciones)
    return render(request,'puntofijo/resultado.html',{'resp':resp})    

def Secante(request): 
    abc= request.POST['pol']
    setF(abc)
    fn= float( request.POST['fn'] )
    p0= int( request.POST['p0'] )
    p1= int( request.POST['p1'] )
    tol= int( request.POST['tol'] )
    n= int( request.POST['n'] )
    
    resp= Rsecante(fn,p0,p1,tol,n)
    return render(request,'secante/resultado.html',{'resp':resp})    

def plot(request):
    funcionF = aTransformar(getF())
    print(funcionF)
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