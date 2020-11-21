from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from utils.util import AlchemyEncoder
import json


# Server - Flask
# ORM - SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/tienda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#########################################################################################

# CRUD Pagos 
class Pagos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idDuenio = db.Column(db.Integer)
    idCursos = db.Column(db.Integer)

# Rutas Pagos
@app.route('/Pagos/consulta',methods=['POST'])
def consultarPagos():
    cursosData = json.dumps(Pagos.query.all(), cls=AlchemyEncoder)
    data={}
    data['body'] = json.loads(cursosData)
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/Pagos/crear',methods=['POST'])
def crearPagos():
    crear = Pagos(idDuenio=request.form['idDuenio'],idCursos=request.form['idCursos'])
    db.session.add(crear)
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/Pagos/actualizar',methods=['POST'])
def actualizarPagos():
    consultar =  Pagos.query.filter_by(id=request.form['id']).all()
    for cursos in consultar:
        cursos.nombre = request.form['nombre']
        cursos.idProfesor = request.form['idProfesor']
        cursos.activo = request.form['activo']
        db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/Pagos/eliminar',methods=['POST'])
def eliminarPagos():
    Pagos.query.filter_by(id=request.form['id']).delete()
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

#########################################################################################

# CRUD CURSOSCOMPRADOS 
class CursosComprados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idDuenio = db.Column(db.Integer)
    idCursos = db.Column(db.Integer)

# Rutas CURSOSCOMPRADOS
@app.route('/cursoscomprados/consulta',methods=['POST'])
def consultarCursosComprados():
    cursosData = json.dumps(CursosComprados.query.all(), cls=AlchemyEncoder)
    data={}
    data['body'] = json.loads(cursosData)
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/cursoscomprados/detalle',methods=['POST'])
def detallarCursosComprados():
    cursosData = json.dumps(CursosComprados.query.filter_by(id=request.form['id']).all(), cls=AlchemyEncoder)
    data={}
    data['body'] = json.loads(cursosData)
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/cursoscomprados/crear',methods=['POST'])
def crearCursosComprados():
    crear = CursosComprados(idDuenio=request.form['inputIdDuenio'],idCursos=request.form['inputIdCurso'])
    db.session.add(crear)
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data , 200

@app.route('/cursoscomprados/actualizar',methods=['POST'])
def actualizarCursosComprados():
    consultar =  CursosComprados.query.filter_by(id=request.form['id']).all()
    for cursos in consultar:
        cursos.nombre = request.form['nombre']
        cursos.idProfesor = request.form['idProfesor']
        cursos.activo = request.form['activo']
        db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/cursoscomprados/eliminar',methods=['POST'])
def eliminarCursosComprados():
    CursosComprados.query.filter_by(id=request.form['id']).delete()
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

#########################################################################################

# CRUD Cursos 
class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    #descripcion = db.Column(db.String(200))
    #costo = db.Column(db.Integer)
    #categorias = db.Column(db.String(200))
    idProfesor = db.Column(db.Integer)
    activo = db.Column(db.Integer)

# Rutas Cursos
@app.route('/cursos/consulta',methods=['POST'])
def consultarCursos():
    cursosData = json.dumps(Cursos.query.all(), cls=AlchemyEncoder)
    data={}
    data['body'] = json.loads(cursosData)
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/cursos/detalle',methods=['POST'])
def detalleCurso():
    data = request.json
    query = Cursos.query.filter_by(id=data['id']).all()
    consultar =  json.dumps(query, cls=AlchemyEncoder)
    data={}
    http = 200
    if len(query) > 0:
        data['body'] = json.loads(consultar)
        data['status'] = {}
        data['status']['code'] = 'OK'
    else:
        data['status'] = {}
        data['status']['code'] = 'Not OK'
        http = 500
    return data, http

@app.route('/cursos/crear',methods=['POST'])
def crearCursos():
    crear = Cursos(nombre=request.form['inputNombre'],idProfesor=request.form['inputIdProfesor'],activo=1)
    db.session.add(crear)
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/cursos/actualizar',methods=['POST'])
def actualizarCursos():
    consultar =  Cursos.query.filter_by(id=request.form['id']).all()
    for cursos in consultar:
        cursos.nombre = request.form['nombre']
        cursos.idProfesor = request.form['idProfesor']
        cursos.activo = request.form['activo']
        db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/cursos/eliminar',methods=['POST'])
def eliminarCursos():
    Cursos.query.filter_by(id=request.form['id']).delete()
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

#########################################################################################

#CRUD Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    apellido = db.Column(db.String(200))
    correo = db.Column(db.String(200))
    contrasenia = db.Column(db.String(200))
    role = db.Column(db.Integer)


# Rutas Usuarios
@app.route('/usuario/consulta',methods=['POST'])
def consultarUsuario():
    query = Usuario.query.all()
    userData = json.dumps(query, cls=AlchemyEncoder)
    data={}
    http = 200
    if len(query) > 0:
        data['body'] = json.loads(userData)
        data['status'] = {}
        data['status']['code'] = 'OK'
    else:
        data['status'] = {}
        data['status']['code'] = 'Not OK'
        http = 500
    return data, http

@app.route('/usuario/detalle',methods=['POST'])
def detalleUsuario():
    query = Usuario.query.filter_by(correo=request.form['inputEmail'],contrasenia=request.form['inputPassword']).all()
    consultar =  json.dumps(query, cls=AlchemyEncoder)
    data={}
    http = 200
    if len(query) > 0:
        data['body'] = json.loads(consultar)
        data['status'] = {}
        data['status']['code'] = 'OK'
    else:
        data['status'] = {}
        data['status']['code'] = 'Not OK'
        http = 500
    return data, http

@app.route('/usuario/crear',methods=['POST'])
def crearUsuario():
    crear = Usuario(nombre=request.form['inputNombre'],apellido=request.form['inputApellido'],correo=request.form['inputEmail'],contrasenia=request.form['inputPassword'],role=request.form['inputRole'])
    db.session.add(crear)
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/usuario/actualizar',methods=['POST'])
def actualizarUsuario():
    consultar =  Usuario.query.filter_by(id=request.form['id']).all()
    for usuario in consultar:
        usuario.nombre = request.form['nombre']
        usuario.apellido = request.form['apellido']
        usuario.role = request.form['role']
        db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/usuario/eliminar',methods=['POST'])
def eliminarUsuario():
    Usuario.query.filter_by(id=request.form['id']).delete()
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

#########################################################################################

# CRUD Inscripciones
class Inscripciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idEstudiante = db.Column(db.Integer)
    activo = db.Column(db.Integer)

# Rutas Inscripciones
@app.route('/inscripciones/consulta',methods=['POST'])
def consultarInscripciones():
    inscripcionesData = json.dumps(Inscripciones.query.all(), cls=AlchemyEncoder)
    data={}
    data['body'] = json.loads(inscripcionesData)
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/inscripciones/crear',methods=['POST'])
def crearInscripciones():
    crear = Inscripciones(idEstudiante=request.form['idEstudiante'], activo=request.form['activo'])
    db.session.add(crear)
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/inscripciones/actualizar',methods=['POST'])
def actualizarInscripciones():
    consultar =  Inscripciones.query.filter_by(id=request.form['id']).all()
    for inscripciones in consultar:
        inscripciones.idEstudiante = request.form['idEstudiante']
        inscripciones.activo = request.form['activo']
        db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

@app.route('/inscripciones/eliminar',methods=['POST'])
def eliminarInscripciones():
    Inscripciones.query.filter_by(id=request.form['id']).delete()
    db.session.commit()
    data={}
    data['status'] = {}
    data['status']['code'] = 'OK'
    return data

#########################################################################################

# Paginas
@app.route('/',methods=['GET'])
def home():
    cursosData = Cursos.query.all()
    return render_template('index.html',cursos = cursosData)

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/adminProfesor/<id>',methods=['GET'])
def adminProfesor(id):
    idProfesor = id
    usuarioQuery = Usuario.query.filter_by(id=idProfesor).all()
    cursosQuery = Cursos.query.filter_by(idProfesor=idProfesor).all()
    return render_template('adminProfesor.html',usuario=usuarioQuery,cursos=cursosQuery)

@app.route('/adminEstudiantes/<id>',methods=['GET'])
def adminEstudiantes(id):
    listaCursos = []
    idEstudiante = id
    usuarioQuery = Usuario.query.filter_by(id=idEstudiante).all()
    cursosQuery = Cursos.query.all()
    cursosCompradosQuery = CursosComprados.query.filter_by(idDuenio=idEstudiante).all()
    for cr in cursosCompradosQuery:
        cur = Cursos.query.filter_by(id=cr.idCursos).all()
        crComprado = {}
        crComprado['id'] = cur[0].id
        crComprado['nombre'] = cur[0].nombre
        listaCursos.append(crComprado)
    return render_template('adminEstudiantes.html',usuario=usuarioQuery, cursos=cursosQuery, cursosComprados=listaCursos)

# Pagina no encontrada
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title = 'No encontrado'), 404

#########################################################################################

# Init Server
if __name__=="__main__":
    app.run(debug=True)