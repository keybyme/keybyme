from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateLinkForm, UpdateLinkForm, CreateClaveForm, CreateContactoForm, UpdateContactoForm, UpdateClaveForm, CreateCat_claveForm, CreateCat_contactoForm, CreateCat_linkForm, CreateReminderForm, CreateCodigoForm, UpdateCodigoForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .models import Cat_clave, Cat_link, Contacto, Clave, Link, Cat_contacto, Reminder, Codigo
from django.db.models import Q
from .forms import QrcodeForm2
import io
import pyqrcode
import base64
from io import BytesIO
from PIL import Image


########################  QRcode

def generate_qr_code(request):
    if request.method == 'POST':
        form = QrcodeForm2(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            qr_code = pyqrcode.create(link)

            # Generate the QR code image and save it to a BytesIO object
            buffer = io.BytesIO()
            qr_code.png(buffer, scale=5)
            buffer.seek(0)

            # Encode the image data as base64
            image_data = base64.b64encode(buffer.getvalue()).decode()

            return render(request, 'keyapp/qrcode.html', {'form': form, 'image_data': image_data})
    else:
        form = QrcodeForm2()

    return render(request, 'keyapp/qrcode.html', {'form': form})

##########################################

def home(request):
      
      return render(request, 'keyapp/index.html')

########################   Register

def register(request):
      
      form = CreateUserForm()
      if request.method == "POST": 
            form = CreateUserForm(request.POST)
            
            if form.is_valid():
                  form.save()
                  return redirect('my-login')
                 
      context = {'form':form}
      return render(request, 'keyapp/register.html', context=context)


########################   Login a user

def my_login(request):
      
      form = LoginForm()
      if request.method == "POST":
            
            form = LoginForm(request, data=request.POST)
            
            if form.is_valid():
                  username = request.POST.get("username")
                  password = request.POST.get("password")
                  user = authenticate(request, username=username, password=password)
                  
                  if user is not None:
                        auth.login(request, user)
                        return redirect("dashboard")
                        
      context = {'form':form}   
      return render(request, 'keyapp/my-login.html', context=context)

########################   Dashboard

@login_required(login_url='my-login')
def dashboard(request):
      return render(request, 'keyapp/dashboard.html')

########################   Contactos

@login_required(login_url='my-login')
def contactosv(request):
      busca_con=request.GET.get("busca_con")
                  
      my_contactos = Contacto.objects.filter(user=request.user).order_by('fk_cat__categoria', 'name')
      context = {'contactos': my_contactos}
      if busca_con:
            con=Contacto.objects.filter(Q(name__icontains=busca_con) | Q(remarks__icontains=busca_con) | Q(email__icontains=busca_con)| Q(fk_cat__categoria__icontains=busca_con))
            my_contactos = Contacto.objects.filter(user=request.user)
            context = {'contactos': con}
            return render(request, 'keyapp/contactos.html', context=context)
      return render(request, 'keyapp/contactos.html', context=context)


########################   Reminders

@login_required(login_url='my-login')
def remindersv(request):
      busca_rem=request.GET.get("busca_rem")
                  
      my_reminders = Reminder.objects.filter(user=request.user).order_by('rem_name')
      context = {'reminders': my_reminders}
      if busca_rem:
            con=Reminder.objects.filter(Q(rem_name__icontains=busca_rem) | Q(remarks__icontains=busca_rem))
            my_reminders = Reminder.objects.filter(user=request.user)
            context = {'reminders': con}
            return render(request, 'keyapp/reminders.html', context=context)
      return render(request, 'keyapp/reminders.html', context=context)
# ########################  Claves

@login_required(login_url='my-login')
def claves(request):
      busca_cla=request.GET.get("busca_cla")
      
      my_claves = Clave.objects.filter(user=request.user).order_by('fk_cat__categoria', 'entidad')
      context = {'claves': my_claves}
      if busca_cla:
            cla=Clave.objects.filter(Q(entidad__icontains=busca_cla) | Q(remarks__icontains=busca_cla) | Q(fk_cat__categoria__icontains=busca_cla))
            my_claves = Clave.objects.filter(user=request.user)
            context = {'claves': cla}
            return render(request, 'keyapp/claves.html', context=context)
      return render(request, 'keyapp/claves.html', context=context)


########################  Links

@login_required(login_url='my-login')
def links(request):
      busca_link=request.GET.get("busca_link")
      
      my_links = Link.objects.filter(user=request.user).order_by('fk_cat__categoria', 'entidad')
      context = {'links': my_links}
      if busca_link:
            link=Link.objects.filter(Q(entidad__icontains=busca_link) | Q(remarks__icontains=busca_link) | Q(fk_cat__categoria__icontains=busca_link))
            my_links = Link.objects.filter(user=request.user)
            context = {'links': link}
            return render(request, 'keyapp/links.html', context=context)
      return render(request, 'keyapp/links.html', context=context)



########################   User Logout

def user_logout(request):
      
      auth.logout(request)
      
      return redirect("my-login")
      

########################  Create a link
               
@login_required(login_url='my-login')
def create_link(request):        
      
      form = CreateLinkForm()
      if request.method == "POST":
            form = CreateLinkForm(request.POST)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.user=request.user
                  f.save()
                  return redirect("links")
                  
      context = {'form': form}      
      return render(request, 'keyapp/create-link.html', context=context)      


########################  Create a clave
               
@login_required(login_url='my-login')
def create_clave(request):        
      
      form = CreateClaveForm()
      if request.method == "POST":
            form = CreateClaveForm(request.POST)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.user=request.user
                  f.save()
                  return redirect("claves")
                  
      context = {'form': form}      
      return render(request, 'keyapp/create-clave.html', context=context)  

########################  Create a contacto
               
@login_required(login_url='my-login')
def create_contacto(request):        
      
      form = CreateContactoForm()
      if request.method == "POST":
            form = CreateContactoForm(request.POST)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.user=request.user
                  f.save()
                  return redirect("contactosH")
                  
      context = {'form': form}      
      return render(request, 'keyapp/create-contacto.html', context=context)  

########################  Create a reminder
               
@login_required(login_url='my-login')
def create_reminder(request):        
      
      form = CreateReminderForm()
      if request.method == "POST":
            form = CreateReminderForm(request.POST)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.user=request.user
                  f.save()
                  return redirect("remindersH")
                  
      context = {'form': form}      
      return render(request, 'keyapp/create-reminder.html', context=context)  
                
                
########################  Update a link
               
@login_required(login_url='my-login')   
def update_link(request, pk):
      
      link = Link.objects.get(id=pk)
      form = UpdateLinkForm(instance=link)
      if request.method == "POST":
            form = UpdateLinkForm(request.POST, instance=link)
            if form.is_valid():
                  form.save()
                  return redirect("links")
                   
      context = {'form': form}      
      return render(request, 'keyapp/update-link.html', context=context)    

########################  Update a contacto
               
@login_required(login_url='my-login')   
def update_contacto(request, pk):
      
      contacto = Contacto.objects.get(id=pk)
      form = UpdateContactoForm(instance=contacto)
      if request.method == "POST":
            form = UpdateContactoForm(request.POST, instance=contacto)
            if form.is_valid():
                  form.save()
                  return redirect("contactosH")
                   
      context = {'form': form}      
      return render(request, 'keyapp/update-contacto.html', context=context)    

########################  Update a clave
               
@login_required(login_url='my-login')   
def update_clave(request, pk):
      
      clave = Clave.objects.get(id=pk)
      form = UpdateClaveForm(instance=clave)
      if request.method == "POST":
            form = UpdateClaveForm(request.POST, instance=clave)
            if form.is_valid():
                  form.save()
                  return redirect("claves")
                   
      context = {'form': form}      
      return render(request, 'keyapp/update-clave.html', context=context)    



########################  Read ot View a singular link

@login_required(login_url='my-login')   
def singular_link(request, pk):
      
      all_links = Link.objects.get(id=pk)
      context = {'link':all_links}
      return render(request, 'keyapp/view-link.html', context=context)



########################  Read ot View a singular contacto

@login_required(login_url='my-login')   
def singular_contacto(request, pk):
      
      all_contactos = Contacto.objects.get(id=pk)
      context = {'contacto':all_contactos}
      return render(request, 'keyapp/view-contacto.html', context=context)


########################  Read ot View a singular clave

@login_required(login_url='my-login')   
def singular_clave(request, pk):
      
      all_claves = Clave.objects.get(id=pk)
      context = {'clave':all_claves}
      return render(request, 'keyapp/view-clave.html', context=context)



########################  Delete a link
               
@login_required(login_url='my-login')   
def delete_link(request, pk):
      
      link = Link.objects.get(id=pk)
      
      link.delete()
      
      return redirect("links")


########################  Delete a contacto
               
@login_required(login_url='my-login')   
def delete_contacto(request, pk):
      
      contacto = Contacto.objects.get(id=pk)
      
      contacto.delete()
      
      return redirect("contactosH")


########################  Delete a clave
               
@login_required(login_url='my-login')   
def delete_clave(request, pk):
      
      clave = Clave.objects.get(id=pk)
      
      clave.delete()
      
      return redirect("claves")


########################  Categorias Claves

@login_required(login_url='my-login')
def cat_claves(request):
      
      my_cat = Cat_clave.objects.filter(user=request.user)
      context = {'cat_claves': my_cat}
      return render(request, 'keyapp/cat_claves.html', context=context)


########################  Categorias Contactos

@login_required(login_url='my-login')
def cat_contactos(request):
      
      my_cat = Cat_contacto.objects.filter(user=request.user)
      context = {'cat_contactos': my_cat}
      return render(request, 'keyapp/cat_contactos.html', context=context)


########################  Categorias Links

@login_required(login_url='my-login')
def cat_links(request):
      
      #my_cat = Cat_link.objects.all() 
      my_cat = Cat_link.objects.filter(user=request.user) 
      context = {'cat_links': my_cat}
      return render(request, 'keyapp/cat_links.html', context=context)


########################  Delete Categoria clave
               
@login_required(login_url='my-login')   
def delete_cat_clave(request, pk):
      
      cat_clave = Cat_clave.objects.get(id=pk)
      cat_clave.delete()
      return redirect("cat_claves")


########################  Delete Categoria contacto
               
@login_required(login_url='my-login')   
def delete_cat_contacto(request, pk):
      
      cat_contacto = Cat_contacto.objects.get(id=pk)
      cat_contacto.delete()
      return redirect("cat_contactos")

########################  Delete Categoria link
               
@login_required(login_url='my-login')   
def delete_cat_link(request, pk):
      
      cat_link = Cat_link.objects.get(id=pk)
      cat_link.delete()
      return redirect("cat_links")

########################  Create Categoria clave
               
@login_required(login_url='my-login')
def create_cat_clave(request):        
      
      form = CreateCat_claveForm()
      if request.method == "POST":
            form = CreateCat_claveForm(request.POST)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.user=request.user
                  f.save()
                  return redirect("cat_claves")
                  
      context = {'form': form}      
      return render(request, 'keyapp/create-cat_clave.html', context=context)  


########################  Create Categoria contacto
               
@login_required(login_url='my-login')
def create_cat_contacto(request):        
      
      form = CreateCat_contactoForm()
      if request.method == "POST":
            form = CreateCat_contactoForm(request.POST)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.user=request.user
                  f.save()
                  return redirect("cat_contactos")
                  
      context = {'form': form}      
      return render(request, 'keyapp/create-cat_contacto.html', context=context)  


########################  Create Categoria link
               
@login_required(login_url='my-login')
def create_cat_link(request):        
      
      form = CreateCat_linkForm()
      if request.method == "POST":
            form = CreateCat_linkForm(request.POST)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.user=request.user
                  f.save()
                  return redirect("cat_links")
                  
      context = {'form': form}      
      return render(request, 'keyapp/create-cat_link.html', context=context)  

import sys
from django.http import HttpResponse

def apagar(request):
      if request.user.is_superuser:
            sys.exit()
            
            return HttpResponse("apagando")
      
      
########################   Codigos

@login_required(login_url='my-login')
def codigosv(request):
      busca_cod=request.GET.get("busca_cod")
                  
      my_codigos = Codigo.objects.filter(user=request.user)
      context = {'codigos': my_codigos}
      if busca_cod:
            cod=Codigo.objects.filter(Q(name__icontains=busca_cod) | Q(remarks__icontains=busca_cod))
            my_codigos = Codigo.objects.filter(user=request.user)
            context = {'codigos': cod}
            return render(request, 'keyapp/codigos.html', context=context)
      return render(request, 'keyapp/codigos.html', context=context)      


########################  Create a codigo
               
@login_required(login_url='my-login')
def create_codigo(request):        
      
      form = CreateCodigoForm()
      if request.method == "POST":
            form = CreateCodigoForm(request.POST)
            if form.is_valid():
                  f=form.save(commit=False)
                  f.user=request.user
                  f.save()
                  return redirect("codigosH")
                  
      context = {'form': form}      
      return render(request, 'keyapp/create-codigo.html', context=context)  


########################  Update a codigo
               
@login_required(login_url='my-login')   
def update_codigo(request, pk):
      
      codigo = Codigo.objects.get(id=pk)
      form = UpdateCodigoForm(instance=codigo)
      if request.method == "POST":
            form = UpdateCodigoForm(request.POST, instance=codigo)
            if form.is_valid():
                  form.save()
                  return redirect("codigosH")
                   
      context = {'form': form}      
      return render(request, 'keyapp/update-codigo.html', context=context)    


########################  Read ot View a singular codigo

@login_required(login_url='my-login')   
def singular_codigo(request, pk):
      
      all_codigos = Codigo.objects.get(id=pk)
      context = {'codigo':all_codigos}
      return render(request, 'keyapp/view-codigo.html', context=context)


########################  Delete a codigo
               
@login_required(login_url='my-login')   
def delete_codigo(request, pk):
      
      codigo = Codigo.objects.get(id=pk)
      
      codigo.delete()
      
      return redirect("codigosH")


########################  singular codigo para QR

def singular_qr(request, pk):
      
      all_codigos = Codigo.objects.get(id=pk)
      context = {'codigo':all_codigos}
      return render(request, 'keyapp/view-qr.html', context=context)


      