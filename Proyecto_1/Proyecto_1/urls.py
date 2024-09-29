from django.contrib import admin
from django.urls import path
from Proyecto_1APP import views
from django.conf import settings  # Importar settings para acceder a las configuraciones del proyecto
from django.conf.urls.static import static  # Importar static para servir archivos estáticos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página principal
    path('datospersona/', views.datospersona, name='datospersona'),  # Datos de la persona
    path('productos/', views.productos_view, name='productos'),  # Lista de productos
    path('productos/<str:categoria>/', views.productos_por_categoria, name='productos_por_categoria'),  # Nueva ruta para productos por categoría
    path('producto/<int:producto_id>/', views.producto_detalle, name='producto_detalle'),  # Detalle del producto
]

# Agregar rutas para archivos estáticos y media en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
