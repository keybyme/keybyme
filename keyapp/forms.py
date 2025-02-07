from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Link, Clave, Contacto, Cat_clave, Cat_contacto, Cat_link, Qrcode, Reminder
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

######################## Register/Create a user

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']
        
######################## Login a user

class LoginForm(AuthenticationForm):
    
        username = forms.CharField(widget=TextInput())
        password = forms.CharField(widget=PasswordInput())
        
######################## Create record link

class CreateLinkForm(forms.ModelForm):
    
    class Meta:
        
        model = Link
        fields = ['entidad', 'url', 'remarks', 'fk_cat']
        
        labels = {
            'entidad': 'Nombre de la entidad',
            'url': 'Dirección URL',
            'remarks': 'Comentarios',
            'fk_cat': 'Categoría relacionada'
        }
        
######################## Create record clave

class CreateClaveForm(forms.ModelForm):
    
    class Meta:
        
        model = Clave
        fields = ['entidad', 'url', 'username', 'password', 'remarks', 'fk_cat']       
        
        labels = {
            'entidad': 'Nombre de la entidad',
            'url': 'Dirección URL',
            'username': 'User name',
            'password': 'Password',
            'remarks': 'Comentarios',
            'fk_cat': 'Categoría relacionada'
        } 
        
        
######################## Create record Categoria clave

class CreateCat_claveForm(forms.ModelForm):
    
    class Meta:
        
        model = Cat_clave
        fields = ['categoria']   
        labels = { 'categoria': "Categoria"}          
        
        
######################## Create record Categoria contacto

class CreateCat_contactoForm(forms.ModelForm):
    
    class Meta:
        
        model = Cat_contacto
        fields = ['categoria'] 
        labels = { 'categoria': "Categoria"}  
        
        
######################## Create record Categoria clave

class CreateCat_linkForm(forms.ModelForm):
    
    class Meta:
        
        model = Cat_link
        fields = ['categoria']   
        labels = { 'categoria': "Categoria"}              
        
        
######################## Create record contacto

class CreateContactoForm(forms.ModelForm):
    
    class Meta:
        
        model = Contacto
        fields = ['name', 'phone', 'email', 'remarks', 'fk_cat']       
        
        labels = {
            'name': 'Nombre del contacto',
            'phone': 'Phone',
            'email': 'E-mail',
            'remarks': 'Comentarios',
            'fk_cat': 'Categoría relacionada'
        } 
         
######################## Create record reminder

class CreateReminderForm(forms.ModelForm):
    
    class Meta:
        
        model = Reminder
        fields = ['rem_name', 'date', 'time', 'remarks', 'freq', 'freq_m_d']       
        
        labels = {
            'rem_name': 'Nombre del reminder',
            'date': 'date',
            'time': 'time',
            'remarks': 'Comentarios',
            'freq': 'frecuencia',
            'freq_m_d': 'freq_m_d'
        }          
                
######################## Update record link

class UpdateLinkForm(forms.ModelForm):
    
    class Meta:
        
        model = Link
        fields = ['entidad', 'url', 'remarks', 'fk_cat']
        labels = {
            'entidad': 'Nombre de la entidad',
            'url': 'Dirección URL',
            'remarks': 'Comentarios',
            'fk_cat': 'Categoría relacionada'
        }        


######################## Update record contacto

class UpdateContactoForm(forms.ModelForm):
    
    class Meta:
        
        model = Contacto
        fields = ['name', 'phone', 'email', 'remarks', 'fk_cat'] 
        labels = {
            'name': 'Nombre del contacto',
            'phone': 'Phone',
            'email': 'E-mail',
            'remarks': 'Comentarios',
            'fk_cat': 'Categoría relacionada'
        }  
        
  
######################## Update record clave
        
class UpdateClaveForm(forms.ModelForm):
    
    class Meta:
        
        model = Clave
        fields = ['entidad', 'url', 'username', 'password', 'remarks', 'fk_cat']   
        labels = {
            'entidad': 'Nombre de la entidad',
            'url': 'Dirección URL',
            'username': 'User name',
            'password': 'Password',
            'remarks': 'Comentarios',
            'fk_cat': 'Categoría relacionada'
        }      
        
        
######################## QRcode

class QrcodeForm(forms.ModelForm):
    class Meta:
        model=Qrcode
        fields=["link"]
        widgets={
            'link':forms.ClearableFileInput(attrs={'class': 'form-control'})
        }            

class QrcodeForm2(forms.Form):
    link = forms.URLField(label='Link')                