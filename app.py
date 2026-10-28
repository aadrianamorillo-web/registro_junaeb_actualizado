from flask import Flask, render_template, request, redirect, url_for, flash
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instancia"
INSTANCE_DIR.mkdir(exist_ok=True)
DB_PATH = INSTANCE_DIR / "asistencia.db"

app = Flask(__name__)
app.secret_key = "cambia-esta-clave-local"
app.template_folder = "plantillas"
app.static_folder = "estaticos"

ESTUDIANTES_INICIALES = [
    ("Diego León Alarcón Sáez", 1),
    ("Sofía Elizabeth Altamirano Serón", 0),
    ("Emilia Pascale Beltran Muñoz", 0),
    ("Félix Ignacio Blanco Salazar", 0),
    ("Sebastián Matías Bustos Parra", 0),
    ("Benjamín Andrés Hernán Calderón Cereceda", 1),
    ("Miley Pascale Casanova Flores", 0),
    ("Elder Manuel Cruzado Rodríguez", 0),
    ("Sebastián Emilio Delgado Carrasco", 0),
    ("Pascal Francisca Díaz Godoy", 0),
    ("Pablo César Espinoza Gómez", 0),
    ("Mariana Francisca Espinoza Salas", 0),
    ("Fernanda Antonella Fernández Fernández", 0),
    ("Keysi Sharon Flores Solis", 0),
    ("Adonys Amador Gómez Miño", 0),
    ("Magdalena Paz González González", 0),
    ("Fernando Andrés Ibarra Sáez", 1),
    ("Noelia Amaranta Jeria Jiménez", 0),
    ("Franchesca Danae Lizana Herrera", 0),
    ("Kevin Dylan Morales Nuñez", 0),
    ("Nicolás Ignacio Morales Soto", 0),
    ("Adriana Valeria Morillo Pizan", 1),
    ("Mariana Millaray Núñez Ancamil", 0),
    ("Vicente Matías Quiroz Vilches", 0),
    ("César Alejandro Ramirez Aquino", 0),
    ("Antonella Belén Rivera Zúñiga", 0),
    ("Germán Enrique Riveros Albornoz", 0),
    ("Martina Belén Robles Campillay", 0),
    ("Tomás Ariel Rodríguez Meneses", 0),
    ("Josefa Ignacia Rojas Vásquez", 0),
    ("Naaray Mijael Seguel Claverie", 0),
    ("Antonia Margarita Torres Palacios", 0),
    ("Cristhian Reinier Urdaneta Cuello", 1),
    ("Vicente Ignacio Vallejos Pérez", 0),
    ("Gabriel Isaias Vásquez Cornejo", 1),
]

def conectar_db():
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion

def preparar_db():
    with conectar_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                junaeb INTEGER NOT NULL DEFAULT 0
            )
        """)
        db.execute("""
            CREATE TABLE IF NOT EXISTS asistencias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                estudiante_id INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                estado TEXT NOT NULL DEFAULT 'Pendiente',
                UNIQUE(estudiante_id, fecha),
                FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id)
            )
        """)
        cantidad = db.execute("SELECT COUNT(*) FROM estudiantes").fetchone()[0]
        if cantidad == 0:
            db.executemany(
                "INSERT INTO estudiantes (nombre, junaeb) VALUES (?, ?)",
                ESTUDIANTES_INICIALES
            )

@app.route("/")
def inicio():
    from datetime import date
    fecha = request.args.get("fecha", date.today().isoformat())
    buscar = request.args.get("buscar", "").strip()
    filtro = request.args.get("filtro", "Todos")
    with conectar_db() as db:
        consulta = """
            SELECT e.id, e.nombre, e.junaeb,
                   COALESCE(a.estado, 'Pendiente') AS estado
            FROM estudiantes e
            LEFT JOIN asistencias a
              ON a.estudiante_id = e.id AND a.fecha = ?
            WHERE e.nombre LIKE ?
        """
        filas = db.execute(consulta, (fecha, f"%{buscar}%")).fetchall()
        estudiantes = [dict(f) for f in filas]
    if filtro != "Todos":
        estudiantes = [e for e in estudiantes if e["estado"] == filtro]
    conteo = {
        "Presentes": sum(e["estado"] == "Presente" for e in estudiantes),
        "Ausentes": sum(e["estado"] == "Ausente" for e in estudiantes),
        "Atrasados": sum(e["estado"] == "Atrasado" for e in estudiantes),
        "Pendientes": sum(e["estado"] == "Pendiente" for e in estudiantes),
    }
    return render_template("index.html", estudiantes=estudiantes, fecha=fecha,
                           buscar=buscar, filtro=filtro, conteo=conteo)

@app.post("/marcar")
def marcar():
    estudiante_id = request.form.get("estudiante_id", type=int)
    fecha = request.form.get("fecha", "")
    estado = request.form.get("estado", "")
    estados_validos = {"Presente", "Ausente", "Atrasado", "Pendiente"}
    if not estudiante_id or not fecha or estado not in estados_validos:
        flash("No se pudo guardar. Revisa los datos e inténtalo de nuevo.", "error")
        return redirect(url_for("inicio"))
    with conectar_db() as db:
        if estado == "Pendiente":
            db.execute("DELETE FROM asistencias WHERE estudiante_id = ? AND fecha = ?",
                       (estudiante_id, fecha))
        else:
            db.execute("""
                INSERT INTO asistencias (estudiante_id, fecha, estado)
                VALUES (?, ?, ?)
                ON CONFLICT(estudiante_id, fecha)
                DO UPDATE SET estado = excluded.estado
            """, (estudiante_id, fecha, estado))
    flash("Asistencia guardada correctamente.", "ok")
    return redirect(url_for("inicio", fecha=fecha, buscar=request.form.get("buscar", "")))

@app.post("/estudiantes/agregar")
def agregar_estudiante():
    nombre = request.form.get("nombre", "").strip()
    junaeb = 1 if request.form.get("junaeb") == "on" else 0
    if not nombre:
        flash("Escribe el nombre del estudiante.", "error")
    else:
        try:
            with conectar_db() as db:
                db.execute("INSERT INTO estudiantes (nombre, junaeb) VALUES (?, ?)",
                           (nombre, junaeb))
            flash("Estudiante agregado correctamente.", "ok")
        except sqlite3.IntegrityError:
            flash("Ese estudiante ya está registrado.", "error")
    return redirect(url_for("inicio"))

preparar_db()

if __name__ == "__main__":
    app.run(debug=True)
