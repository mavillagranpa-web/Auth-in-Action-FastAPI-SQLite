paso 1
# API de Autenticación - Guía Paso a Paso

## 📋 PRERREQUISITOS
- Tener Python 3.10+ instalado
- Tener pip (gestor de paquetes de Python)

## 🚀 INSTALACIÓN Y EJECUCIÓN - PASO A PASO

### PASO 1: Instalar dependencias
```bash
pip install -r requirements.txt

paso 2
python -m uvicorn main:app --reload
paso 3
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
paso 4
http://127.0.0.1:8000/docs
paso 5
En la página de Swagger (http://127.0.0.1:8000/docs)

Haz clic en el endpoint POST /login

Haz clic en "Try it out"

En el campo de texto, pega exactamente:

{
  "username": "naruto",
  "password": "rasengan123"
}
PASO 6
Si es exitoso: Verás código 200 y mensaje de bienvenida

Si hay error: Verás código 401 con mensaje de error
