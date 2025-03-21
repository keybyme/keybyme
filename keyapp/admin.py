from django.contrib import admin
from .models import Cat_clave, Cat_link, Contacto, Clave, Link, Cat_contacto, Qrcode, Reminder, Codigo


# Register your models here.

admin.site.register(Cat_clave)
admin.site.register(Cat_contacto)
admin.site.register(Cat_link)
admin.site.register(Clave)
admin.site.register(Contacto)
admin.site.register(Link)
admin.site.register(Qrcode)
admin.site.register(Reminder)
admin.site.register(Codigo)