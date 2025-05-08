# Clasificador de Enfermedades de Hojas con Flask y TensorFlow Lite

Este proyecto es una aplicación web hecha con Flask que utiliza modelos de Deep Learning para clasificar en tiempo real imágenes de hojas de plantas, detectando enfermedades específicas según su especie.

El modelo fue entrenado sobre el dataset Plant Village y convertido a formato TensorFlow Lite (.tflite) para despliegue eficiente.

## Características
- Acceso a la cámara del dispositivo directamente desde el navegador (compatible con móviles y escritorio).

- Predicciones en tiempo real a partir de imágenes capturadas.

- Identificación de múltiples categorías, incluyendo enfermedades específicas por especie y estado saludable.

- Backend optimizado usando modelos en formato TensorFlow Lite.

- Interfaz sencilla construida con Bootstrap.

---

## Estructura del proyecto

```
plant_village_app/
├── app.py                               # Servidor Flask principal
├── requirements.txt                     # Dependencias necesarias
├── models/
│   └── plant_leaves_classifier_expert.tflite  # Modelo entrenado y convertido
├── static/
│   ├── main.js                          # Lógica JavaScript para captura y envío de imágenes
│   └── logo.png                         # Logo mostrado en la interfaz (opcional)
├── templates/
│   └── index.html                       # Interfaz principal de la aplicación
└── README.md                            # Este archivo
```

---

## Requisitos

- Python 3.8+
- TensorFlow 2.x
- Flask
- gunicorn (para despliegue)

Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## Ejecución local

```bash
python app.py
```

Luego abre tu navegador en:
```
http://127.0.0.1:5000
```

---

## Despliegue en Render

1. Sube este proyecto a un repositorio en GitHub.
2. Crea una cuenta en [https://render.com](https://render.com)
3. En Render:
   - Selecciona "New Web Service"
   - Conecta tu repositorio
   - Configura:
     - **Build command**: `pip install -r requirements.txt`
     - **Start command**: `gunicorn app:app`
4. Asegúrate de tener `plant_leaves_classifier_expert.tflite` dentro de `model/`, y que pesen <100MB.

---

## Licencia
Este proyecto es de uso libre con fines educativos y experimentales.

---

## Autor
**Angel Barraza Real**  
[GitHub](https://github.com/AngelBReal)  
[LinkedIn](https://www.linkedin.com/in/angelbarrazareal/)  

---

¡Listo para usar! Si necesitas ayuda para desplegarlo o extenderlo, contáctame.

