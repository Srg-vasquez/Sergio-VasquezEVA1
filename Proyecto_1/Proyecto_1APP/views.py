from django.shortcuts import render
from django.http import Http404

# Datos de productos con descripciones y categorías
productos = [
    {"id": 1, "nombre": "Televisor", "descripcion": "Televisor 4K Ultra HD con pantalla de 65 pulgadas, resolución increíble y conectividad Wi-Fi integrada para acceso a streaming de contenido. Ideal para salas de estar grandes y reuniones familiares.", "precio": "$500.000", "categoria": "electronica", "imagen": "televisor40k.jpg"},
    {"id": 2, "nombre": "Muñeca", "descripcion": "Muñeca de peluche suave con ropa tejida a mano y cabello trenzado, perfecta para acompañar a los niños en sus juegos y a la hora de dormir. Producto seguro y duradero.", "precio": "$20.000", "categoria": "juguetes", "imagen": "muñeca.jpg"},
    {"id": 3, "nombre": "Camiseta", "descripcion": "Camiseta de algodón 100% orgánico, disponible en diferentes colores y tallas. Ideal para combinar con jeans o shorts en cualquier temporada del año.", "precio": "$15.000", "categoria": "ropa", "imagen": "camiseta-negra.jpg"},
    {"id": 4, "nombre": "Laptop", "descripcion": "Laptop con procesador Intel i5 de última generación, 8GB de RAM y 256GB de almacenamiento SSD. Perfecta para tareas de oficina, videollamadas y entretenimiento multimedia.", "precio": "$800.000", "categoria": "electronica", "imagen": "Laptop.jpg"},
    {"id": 5, "nombre": "Auto de Juguete", "descripcion": "Auto de juguete a control remoto con luces LED y sonido, diseñado para proporcionar horas de diversión a niños y adultos. Ruedas robustas que garantizan estabilidad y durabilidad.", "precio": "$25.000", "categoria": "juguetes", "imagen": "auto-juguete.jpg"},
    {"id": 6, "nombre": "Pantalones", "descripcion": "Pantalones vaqueros de corte clásico con acabado desgastado, disponibles en tallas para hombre y mujer. Hechos con tela resistente y de alta calidad para un uso prolongado.", "precio": "$30.000", "categoria": "ropa", "imagen": "pants.jpg"},
    # Nuevos productos para Electrónica
    {"id": 7, "nombre": "Audífonos Inalámbricos", "descripcion": "Audífonos inalámbricos con cancelación de ruido, batería de larga duración y conexión Bluetooth. Ideales para trabajar desde casa o relajarse escuchando música.", "precio": "$150.000", "categoria": "electronica", "imagen": "audifonos-inalambricos.jpg"},
    {"id": 8, "nombre": "Smartwatch", "descripcion": "Smartwatch con monitor de ritmo cardíaco, contador de pasos y notificaciones. Compatible con iOS y Android.", "precio": "$200.000", "categoria": "electronica", "imagen": "smartwatch.jpg"},
    {"id": 9, "nombre": "Tablet", "descripcion": "Tablet de 10 pulgadas con pantalla Full HD, 64GB de almacenamiento y sistema operativo Android. Perfecta para leer, jugar y ver videos.", "precio": "$250.000", "categoria": "electronica", "imagen": "tablet.jpg"},
    # Nuevos productos para Juguetes
    {"id": 10, "nombre": "Set de Bloques de Construcción", "descripcion": "Set de bloques de construcción con piezas interconectables. Estimula la creatividad y el pensamiento lógico en los niños.", "precio": "$35.000", "categoria": "juguetes", "imagen": "bloque-construccion.jpg"},
    {"id": 11, "nombre": "Pelota de Fútbol", "descripcion": "Pelota de fútbol tamaño oficial, ideal para niños y adultos. Hecha de materiales duraderos para un rendimiento superior en cualquier campo.", "precio": "$10.000", "categoria": "juguetes", "imagen": "pelota-football.jpg"},
    {"id": 12, "nombre": "Rompecabezas 3D", "descripcion": "Rompecabezas 3D con más de 500 piezas. Fomenta la concentración y habilidades motoras finas. Incluye instrucciones detalladas.", "precio": "$50.000", "categoria": "juguetes", "imagen": "rompecabeza-3d.jpg"},
    # Nuevos productos para Ropa
    {"id": 13, "nombre": "Chaqueta de Cuero", "descripcion": "Chaqueta de cuero genuino, ideal para usar en climas fríos. Diseño clásico que nunca pasa de moda, disponible en varias tallas.", "precio": "$120.000", "categoria": "ropa", "imagen": "chaqueta-cuero.jpg"},
    {"id": 14, "nombre": "Vestido de Verano", "descripcion": "Vestido de verano hecho de lino, ideal para eventos casuales. Disponible en colores vibrantes y diseño suelto para máxima comodidad.", "precio": "$60.000", "categoria": "ropa", "imagen": "ropa-verano.jpg"},
    {"id": 15, "nombre": "Zapatos Deportivos", "descripcion": "Zapatos deportivos con suela antideslizante y plantilla acolchada. Perfectos para correr o caminar largas distancias.", "precio": "$70.000", "categoria": "ropa", "imagen": "zapatos-deportivos.jpg"},
]

def index(request):
    # Separa productos por categoría para enviar a la plantilla
    productos_electronica = [p for p in productos if p["categoria"] == "electronica"]
    productos_juguetes = [p for p in productos if p["categoria"] == "juguetes"]
    productos_ropa = [p for p in productos if p["categoria"] == "ropa"]

    # Pasar los productos separados a la plantilla index.html
    return render(request, 'templateApp/index.html', {
        'productos_electronica': productos_electronica,
        'productos_juguetes': productos_juguetes,
        'productos_ropa': productos_ropa,
    })

def productos_por_categoria(request, categoria):
    # Filtrar productos según la categoría recibida
    productos_filtrados = [p for p in productos if p["categoria"] == categoria]
    
    if not productos_filtrados:
        raise Http404("No se encontraron productos para la categoría especificada.")
    
    return render(request, 'templateApp/producto.html', {"productos": productos_filtrados})

def datospersona(request):
    # Datos simulados de una persona
    data = {"id": "123456", "nombre": "Pedro Gaete", "email": "pedro.gaete@inacapmail.cl"}
    return render(request, 'templateApp/primeraweb.html', data)

def productos_view(request):
    # Muestra todos los productos en una página de lista
    return render(request, 'templateApp/producto.html', {"productos": productos})

def producto_detalle(request, producto_id):
    # Encuentra un producto por su ID para mostrar los detalles
    producto = next((item for item in productos if item["id"] == producto_id), None)
    if producto is None:
        raise Http404("Producto no encontrado")
    return render(request, 'templateApp/producto_detalle.html', {"producto": producto})
