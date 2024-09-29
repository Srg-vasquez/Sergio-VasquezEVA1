from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)  # Por ejemplo, 'electronica', 'ropa', etc.
    imagen = models.ImageField(upload_to='productos/')  # Asegúrate de tener Pillow instalado para trabajar con imágenes

    def __str__(self):
        return self.nombre
