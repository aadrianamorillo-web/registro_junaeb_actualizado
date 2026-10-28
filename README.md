# Asiste · Lista de asistencia (Flask)

Versión Flask/Python de la aplicación de asistencia.

## Requisitos
- Python 3.10 o superior

## Ejecutar en Windows
```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

## Ejecutar en Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Abre la dirección que muestre la terminal, normalmente http://127.0.0.1:5000.

La base de datos SQLite se crea automáticamente en `instancia/asistencia.db`.
La lista inicial contiene los 35 estudiantes proporcionados para esta versión. Los números 19 y 23 no aparecen en la lista recibida, por lo que no se inventaron estudiantes para esos espacios. Comprueba los nombres y las marcas JUNAEB antes de usarla en clases.
