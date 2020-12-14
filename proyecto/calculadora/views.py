# from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
#from django.contrib.auth.models import User, auth
from calculadora.models import Metodo
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

#class biseccion(HttpRequest):
    #template_name=''
#	def recogerIntroduccion(self,request):
#		introduccion =Metodo.objects.get(Nombre="Biseccion")
#        return render (request, "biseccion/IntroduccionTema.html",{"intro":introduccion})

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

	#template_name = 'biseccion/Introducciontema.html'
	
    #def recogerIntroduccion(self,request):
	#	introduccion =Metodo.objects.get(Nombre="Biseccion")
    #	return render (request, "biseccion/IntroduccionTema.html",{"intro":introduccion})

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