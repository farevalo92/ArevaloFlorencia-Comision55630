from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', base, name="base"),
    path('aboutMe/', aboutMe, name="aboutMe"),
    path('home/', home, name="home"),
    
       




    path('fci/', FciList.as_view(), name="fci" ),
    path('create_fci/', FciCreate.as_view() , name="create_fci" ),    
    path('update_fci/<int:pk>/', FciUpdate.as_view() , name='update_fci' ),
    path('delete_fci/<int:pk>/', FciDelete.as_view() , name="delete_fci" ),


    path('acciones/', AccionesList.as_view(), name="acciones" ),
    path('create_acciones/', AccionesCreate.as_view() , name="create_acciones" ),    
    path('update_acciones/<int:pk>/', AccionesUpdate.as_view() , name='update_acciones' ),
    path('delete_acciones/<int:pk>/', AccionesDelete.as_view() , name="delete_acciones" ),


    path('bonos/', BonoList.as_view(), name="bonos" ),
    path('create_bonos/', BonoCreate.as_view() , name="create_bonos" ),    
    path('update_bonos/<int:pk>/', BonoUpdate.as_view() , name='update_bonos' ),
    path('delete_bonos/<int:pk>/', BonoDelete.as_view() , name="delete_bonos" ),



    path('cauciones/', CaucionesList.as_view(), name="cauciones" ),
    path('create_cauciones/', CaucionesCreate.as_view() , name="create_cauciones" ),    
    path('update_cauciones/<int:pk>/', CaucionesUpdate.as_view() , name='update_cauciones' ),
    path('delete_cauciones/<int:pk>/', CaucionesDelete.as_view() , name="delete_cauciones" ),


    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarModificarBorrarAvatar, name="agregar_avatar" ),


    path('ver_grafico_a/<str:nomenclatura>/<int:pk>/', ver_grafico_a, name='ver_grafico_a'),


    path('buscar_fci/', buscarFci, name='buscar_fci'),
    path('buscar_fci2/', buscarFci2, name='buscar_fci2'),
    path('buscar_acciones/', buscarAccion, name='buscar_acciones'),
    path('buscar_accion2/', buscarAccion2, name='buscar_accion2'),
    path('buscar_cauciones/', buscarCaucion, name='buscar_cauciones'),
    path('buscar_caucion2/', buscarCaucion2, name='buscar_caucion2'),
    path('buscar_bonos/', buscarBono, name='buscar_bonos'),
    path('buscar_bono2/', buscarBono2, name='buscar_bono2'),







]
