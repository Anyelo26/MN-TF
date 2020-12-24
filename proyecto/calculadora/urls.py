from django.urls import path
from . import views
from django.contrib import admin
from calculadora.views import *

urlpatterns = [
    path('', index.as_view(), name = ''),
    path('tema', tema.as_view(), name = 'tema'),
    path('curso', curso.as_view(), name = 'curso'),
    path('indice', indice.as_view(), name = 'indice'),
    path('quiz', quiz.as_view(), name='quiz'),
    path('biseccion', biseccion.as_view(), name = 'biseccion'),
    path('falsaposicion', falsaposicion.as_view(), name = 'falsaposicion'),
    path('puntofijo', puntofijo.as_view(), name = 'puntofijo'),
    path('secante', secante.as_view(), name = 'secante'),
    path('newton', newton.as_view(), name = 'newton'),
    path('muller', muller.as_view(), name = 'muller'),
    path('bairstow', bairstow.as_view(), name = 'bairstow'),
    path('biseccionCalculadora', biseccionCalculadora.as_view(), name = 'biseccionCalculadora'),
    path('falsaposicionCalculadora', falsaposicionCalculadora.as_view(), name = 'falsaposicionCalculadora'),
    path('puntofijoCalculadora', puntofijoCalculadora.as_view(), name = 'puntofijoCalculadora'),
    path('secanteCalculadora', secanteCalculadora.as_view(), name = 'secanteCalculadora'),
    path('newtonCalculadora', newtonCalculadora.as_view(), name = 'newtonCalculadora'),
    path('mullerCalculadora', mullerCalculadora.as_view(), name = 'mullerCalculadora'),
    path('bairstowCalculadora', bairstowCalculadora.as_view(), name = 'bairstowCalculadora'),
    path('ResultBiseccion',views.Biseccion,name='ResultBiseccion'),
    path('ResultFalsaPosicion',views.FalsaPosicion,name='ResultFalsaPosicion'),
    path('ResultPuntoFijo',views.PuntoFijo,name='ResultPuntoFijo'),
    path('ResultNewton',views.Newton,name='ResultNewtonRaphson'),
    path('ResultSecante',views.Secante,name='ResultSecante'),
    path('ResultMuller', views.Muller,name='ResultMuller'),
    path('ResultBairstow',views.Bairstow,name='ResultBairstow'),
    path('graficar', views.graficar, name='graficar'),
    path('grafica', views.graficaInit, name='grafica'),
]