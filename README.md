# Asiste — Sistema de control de asistencia

## 1. Descripción del proyecto

Asiste es una aplicación web desarrollada para registrar y consultar la asistencia de estudiantes. Permite visualizar la lista del curso, seleccionar una fecha, marcar la asistencia, buscar estudiantes, filtrar resultados y agregar nuevos estudiantes. También identifica a los estudiantes pertenecientes a JUNAEB.

## 2. Tecnologías utilizadas

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Jinja2
- Git y GitHub

## 3. Instalación y ejecución

### Requisitos

- Python instalado.
- Visual Studio Code.
- Conexión a Internet para instalar las dependencias.

### Descargar el proyecto

```bash
git clone -b version-flask https://github.com/aadrianamorillo-web/registro_junaeb_actualizado.git
cd registro_junaeb_actualizado
```

### Crear el entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual en Windows

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En Git Bash:

```bash
source .venv/Scripts/activate
```

### Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### Iniciar la aplicación

```bash
python app.py
```

Abrir en el navegador la dirección local que aparece en la terminal, normalmente:

http://127.0.0.1:5000

## 4. Rutas y funcionalidades

| Ruta | Método | Descripción |
|---|---|---|
| `/` | GET | Muestra la lista de estudiantes y permite buscar, filtrar y consultar la asistencia por fecha. |
| `/marcar` | POST | Registra o actualiza la asistencia de un estudiante. |
| `/estudiantes/agregar` | POST | Permite agregar un estudiante nuevo. |

## 5. Estructura del proyecto

```text
registro_junaeb_actualizado/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── plantillas/
│   └── index.html
├── estaticos/
│   ├── css/
│   │   └── estilos.css
│   └── js/
│       └── asistencia.js
└── instancia/
    └── asistencia.db
```

- `app.py`: contiene la aplicación Flask y sus rutas.
- `requirements.txt`: contiene las dependencias de Python.
- `README.md`: documentación del proyecto.
- `plantillas/index.html`: estructura HTML de la página.
- `estaticos/css/estilos.css`: estilos visuales.
- `estaticos/js/asistencia.js`: interactividad de la página.
- `instancia/asistencia.db`: archivo de base de datos SQLite, creado por la aplicación cuando corresponde.
- `.gitignore`: indica qué archivos se excluyen del control de versiones.

## 6. Base de datos

El proyecto utiliza SQLite para almacenar información localmente.

La base de datos gestiona dos tipos principales de información:

### Estudiantes

Contiene el identificador del estudiante, su nombre completo y un campo que indica si pertenece a JUNAEB.

### Asistencias

Almacena el estudiante asociado, la fecha y el estado de asistencia.

Los estados de asistencia que utiliza la interfaz son Presente, Ausente, Atrasado y Pendiente.

## 7. Funcionalidades principales

- Mostrar la lista de estudiantes.
- Identificar a los estudiantes de JUNAEB.
- Seleccionar la fecha de asistencia.
- Marcar estudiantes como presentes, ausentes o atrasados.
- Consultar estudiantes pendientes de registro.
- Buscar estudiantes por nombre.
- Filtrar por estado de asistencia.
- Mostrar contadores de asistencia.
- Agregar nuevos estudiantes.
- Guardar registros en SQLite.

## 8. Integrantes

- Adriana Morillo
- Miley Casanova
- Keysi Flores
- Emilia Beltran

## 9. Captura de pantalla

Agregar una captura real de la página principal de la aplicación en funcionamiento.

Guardar la imagen en `docs/captura-pagina-principal.png` y mostrarla aquí:

![Página principal de Asiste](docs/captura-pagina-principal.png)

## 10. Repositorio

Repositorio de GitHub:

https://github.com/aadrianamorillo-web/registro_junaeb_actualizado

Rama de trabajo: `version-flask`
