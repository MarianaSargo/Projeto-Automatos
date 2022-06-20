from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = "automatos"

urlpatterns = [
    path('', views.introducao_page_view, name='introducao'),
    path('automatos', views.automatos_page_view, name='automatos'),
    path('maquinas', views.mturing_page_view, name='mturing'),
    path('criarafd', views.criarafd_page_view, name='criarafd'),
    path('editarafd/<int:automato_id>', views.editarafd_page_view, name='editarafd'),
    path('apagarafd/<int:automato_id>', views.apagarafd_page_view, name='apagarafd'),
    path('visualafd/<int:automato_id>', views.visualafd_page_view, name='visualafd'),
    path('testarafd/<int:automato_id>', views.testarafd_page_view, name='testarafd'),
    path('jsonafd', views.jsonafd_page_view, name='jsonafd'),
    path('mturing', views.mturing_page_view, name='mturing'),
    path('criarmt', views.criarmt_page_view, name='criarmt'),
    path('visualmt/<int:mt_id>', views.visualmt_page_view, name='visualmt'),
    path('editarmt/<int:mt_id>', views.editarmt_page_view, name='editarmt'),
    path('apagarmt/<int:mt_id>', views.apagarmt_page_view, name='apagarmt'),
    path('jsonmt', views.jsonmt_page_view, name='jsonmt'),
    path('testarmt/<int:mt_id>', views.testarmt_page_view, name='testarmt'),

]



