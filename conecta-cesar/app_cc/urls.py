"""
URL configuration for project_cc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    #aluno paths
    path('', views.index),
    path('index.html', views.index),
    path('avisos.html', views.aviso),
    path('disciplina.html', views.disciplinas_e_notas),
    path('boletim.html', views.boletim),
    path('frequencia.html', views.frequencia),

    #professor paths
    path('turmas.html', views.turmas),
    path('avisosp.html', views.avisosp),
    path('calendariop.html', views.calendariop),
    path('frequenciap.html', views.frequenciap),
    path('perfilp.html', views.perfilp),
    path('perfil.html', views.perfil),

]
"""Todos os arquivos html é preciso definir o path aqui"""