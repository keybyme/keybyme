from django.db import models
from django.contrib.auth.models import User 
from encrypted_model_fields.fields import EncryptedCharField


######################## --- Claves

class Cat_clave(models.Model):
    categoria = models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table="cat_clave"
    def __str__(self):
        return f"{self.categoria}"
    
class Clave(models.Model):
    entidad = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    username = models.CharField(max_length=50, blank=True)
    password = EncryptedCharField(max_length=500, blank=True)
    remarks = models.CharField(max_length=100, blank=True)
    fk_cat = models.ForeignKey(Cat_clave, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table="clave"
    def __str__(self):
        return f"{self.entidad} | {self.url} | {self.username} | {self.password} | {self.remarks}"
    
    
######################## --- Contactos

class Cat_contacto(models.Model):
    categoria = models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table="cat_contacto"
    def __str__(self):
        return f"{self.categoria}"
    
    

class Contacto(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=250, blank=True)
    remarks = models.CharField(max_length=100, blank=True)
    fk_cat = models.ForeignKey(Cat_contacto, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table="contacto"
    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.remarks}"
    
    
 ######################## --- Links
 
class Cat_link(models.Model):
    categoria = models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table="cat_link"
    def __str__(self):
        return f"{self.categoria}"
    
    
class Link(models.Model):
    entidad = models.CharField(max_length=100)
    url = models.CharField(max_length=250)
    remarks = models.CharField(max_length=100, blank=True)
    fk_cat = models.ForeignKey(Cat_link, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table="link"
    def __str__(self):
        return f"{self.entidad} | {self.url} | {self.remarks}"
    
    
######################## --- QRcode
 
class Qrcode(models.Model):
    link=models.ImageField(upload_to='images/', null=True, blank=True)        
 
    class Meta:
        db_table="qrcode"
    def __str__(self):
        return f"{self.link}"
######################## --- Reminder    
class Reminder(models.Model):
    rem_name = models.CharField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    remarks = models.CharField(blank=True, null=True)
    freq = models.IntegerField(blank=True, null=True) # 1= daily, 2= weekly, 3= annually
    freq_m_d = models.DateField(blank=True, null=True) # month, day
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)    
    comentarios = models.CharField(blank=True, null=True, unique=False)
    testf = models.CharField(blank=True, null=True)
 
    class Meta:
        db_table="reminder"
    def __str__(self):
        return f"{self.rem_name} | {self.date} | {self.time} | {self.remarks} | {self.freq} | {self.freq_m_d} | {self.comentarios}"      

######################## --- Codigos 

class Codigo(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=15, blank=True)
    height = models.CharField(max_length=15, blank=True)
    weight = models.CharField(max_length=15, blank=True)
    allergic = models.CharField(max_length=200, blank=True)
    emergency = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    certification = models.CharField(max_length=250, blank=True)
    remarks = models.CharField(max_length=250, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table="codigo"
    def __str__(self):
        return f"{self.name} | {self.dob} | {self.height} | {self.weight} | {self.allergic} | {self.emergency} | {self.phone} | {self.certification} | {self.remarks}"
    
    