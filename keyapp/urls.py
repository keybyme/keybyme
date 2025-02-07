from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name=""),
    
    path('register', views.register, name="register"),
    
    path('my-login', views.my_login, name="my-login"),
    
    path('user-logout', views.user_logout, name="user-logout"),
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('mycontactos', views.contactosv, name="contactosH"),
    
    path('myreminders', views.remindersv, name="remindersH"),
    
    path('claves', views.claves, name='claves'),
    
    path('links', views.links, name="links"),
    
    path('create-link', views.create_link, name="create-link"),
    
    path('create-clave', views.create_clave, name="create-clave"),
    
    path('create-contacto', views.create_contacto, name="create-contacto"),
    
    path('create-reminder', views.create_reminder, name="create-reminder"),
    
    path('update-link/<int:pk>', views.update_link, name="update-link"),
    
    path('update-contacto/<int:pk>', views.update_contacto, name="update-contacto"),
    
    path('link/<int:pk>', views.singular_link, name="link"),
    
    path('contacto/<int:pk>', views.singular_contacto, name="contacto"),
    
    path('clave/<int:pk>', views.singular_clave, name="clave"),
    
    path('delete-link/<int:pk>', views.delete_link, name="delete-link"),
    
    path('delete-contacto/<int:pk>', views.delete_contacto, name="delete-contacto"),
    
    path('update-clave/<int:pk>', views.update_clave, name="update-clave"),
    
    path('delete-clave/<int:pk>', views.delete_clave, name="delete-clave"),
    
    path('cat_claves', views.cat_claves, name='cat_claves'),
    
    path('cat_contactos', views.cat_contactos, name='cat_contactos'),
    
    path('cat_links', views.cat_links, name='cat_links'),
    
    path('delete-cat_clave/<int:pk>', views.delete_cat_clave, name="delete-cat_clave"),
    
    path('create-cat_clave', views.create_cat_clave, name="create-cat_clave"),
    
    path('delete-cat_contacto/<int:pk>', views.delete_cat_contacto, name="delete-cat_contacto"),
    
    path('create-cat_contacto', views.create_cat_contacto, name="create-cat_contacto"),
    
    path('delete-cat_link/<int:pk>', views.delete_cat_link, name="delete-cat_link"),
    
    path('create-cat_link', views.create_cat_link, name="create-cat_link"),
    
    path('qrcode/', views.generate_qr_code, name="qrcodex"), 
    
    path('apagar', views.apagar, name='apagar'),
]