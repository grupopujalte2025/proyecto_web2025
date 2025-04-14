from django.db import models


# Create your models here.
class ContactForm(models.Model):
    nombre = models.CharField(max_length=50,verbose_name = 'nombre', blank=False)
    correo = models.EmailField(max_length=254, blank=False,verbose_name = 'correo')
    telefono = models.CharField(max_length=15, blank=False,verbose_name = 'teléfono')
    asunto = models.CharField(max_length=50, blank=False,verbose_name = 'asunto')
    mensaje = models.CharField(max_length=350, blank=False,verbose_name = 'mensaje')

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.name

