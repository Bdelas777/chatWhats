# chatWhats
Proyecto de ejemplo para recibir y responder mensajes de WhatsApp (Webhook).

Requisitos:
- Python 3.8+
- Paquetes: `flask`, `requests`, `python-dotenv`

Instalación rápida:

1. Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Instalar dependencias:

```powershell
pip install -r requeriments.txt
```

Variables de entorno (archivo `.env`):

- `VERIFY_TOKEN`: token para verificar el webhook (GET)
- `VERIFY_TOKEN_APP`: token de acceso para la API de mensajes (Bearer)

Ejecución:

```powershell
python app.py
```

Uso rápido:
- Envía `hola` para recibir un saludo y sugerencia de opciones.
- Pulsa los botones para ver `Ver productos` o `Ver servicios`.
- En `Ver productos` se mostrará un listado interactivo con productos, al seleccionar uno recibirás detalles.

Archivos importantes:
- `app.py`: servidor Flask y lógica principal.
- `util.py`: construye los payloads para la API de WhatsApp.
- `whatsappservice.py`: envía mensajes a la API de Facebook/WhatsApp.
- `TextModel.json`, `ButtonModel.json`, `ListModel.json`: ejemplos de webhooks entrantes.

Notas:
- Este proyecto envía peticiones POST a la API de Graph de Facebook; asegúrate de tener un token válido en `.env`.
- Para pruebas locales, usa herramientas como `ngrok` para exponer el puerto.