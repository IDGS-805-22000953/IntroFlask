from flask import Flask,render_template, request
from datetime import datetime
from flask import g
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms



app=Flask(__name__)
app.secret_key='negros'
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404
    
@app.before_request
def before_request():
    g.nombre="Mario"
    print('before 1')
    
@app.after_request
def after_request(response):
    print('after 1')
    return response
    
    

@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():
    #print("alumno {}".format(g.nombre))
    mat=""
    nom=""
    ape=""
    email=""
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST" and alumno_clase.validate():
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data
        # print('Nombre: {}'.format(nom))
        mensaje='bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("Alumnos.html", form=alumno_clase,mat=mat,nom=nom,ape=ape,email=email)

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    nom = ""
    apePa = ""
    apeMa = ""
    genero = ""
    edad = 0
    signo = ""
    
   
    zodiaco_clase = forms.ZodiacoForm(request.form)

    if request.method == "POST" and zodiaco_clase.validate():
       
        nom = zodiaco_clase.nombre.data
        apePa = zodiaco_clase.apellidoPa.data
        apeMa = zodiaco_clase.apellidoMa.data
        genero = zodiaco_clase.genero.data
        dia = zodiaco_clase.dia.data  
        mes = zodiaco_clase.mes.data  
        anio = zodiaco_clase.anio.data  

        try:

            fecha_nac = datetime(anio, mes, dia)

            hoy = datetime.now()
            edad = hoy.year - fecha_nac.year
            if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
                edad -= 1

            
            animales = [
                "Rata", "Buey", "Tigre", "Conejo", "Dragón", 
                "Serpiente", "Caballo", "Cabra", "Mono", 
                "Gallo", "Perro", "Cerdo"
            ]
            indice = (fecha_nac.year - 1900) % 12
            signo = animales[indice]

        except ValueError:
            
            pass

    return render_template("zodiacoChino.html",form=zodiaco_clase,nom=nom,apePa=apePa,apeMa=apeMa,genero=genero,edad=edad,signo=signo
    )

@app.route("/")
def index():
    titulo="IDGS805"
    lista=["Pedro,juan,Mario"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/Hola")
def hola():
    return "<h1>Hola mundooo</h1>"


@app.route("/user/<string:user>")
def user(user):
    return f"hola,{user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numeri es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}"

@app.route("/form1")
def form1():
    return '''
            <form>
            <label for="nombre">Nombre:</label>
            </form>
    
           '''
           
           
           
@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado" ,methods=["POST"])
def result():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operacion = request.form.get("operacion")
        
        if operacion == "multiplicacion":
            return f"La multiplicacion de {num1} x {num2} = {str(int(num1)*int(num2))}"
        
        elif operacion == "division":
            return f"La division de {num1} / {num2} = {str(int(num1)/int(num2))}"
        
        elif operacion == "resta":
            return f"La resta de {num1} - {num2} = {str(int(num1)-int(num2))}"
        
        elif operacion == "suma":
            return f"La suma de {num1} + {num2} = {str(int(num1)+int(num2))}"
        



@app.route("/Cine")
def cine():
    return render_template("cine.html")

@app.route("/entradas", methods=["GET", "POST"])
def entrada():
    if request.method == "POST":
        try:
            compradoresC = int(request.form.get("compradoresC", 0))
            boletos = int(request.form.get("boletos", 0))
            metodo_pago = request.form.get("tarjeta")  
            proceso = request.form.get("proceso")

            if proceso == "procesar":
                max_boletos_permitidos = 7 * compradoresC

                if boletos > max_boletos_permitidos:
                    return render_template("cine.html", valorPago="Error: Excede el límite de boletos permitidos.")

                precio_unitario = 12
                total_global = boletos * precio_unitario

                if 3 <= boletos <= 5:
                    total_global -= total_global * 0.10  
                elif boletos >= 6:
                    total_global -= total_global * 0.15  

                if metodo_pago == "si":
                    total_global -= total_global * 0.10 

                total_global = round(total_global, 2)

                return render_template("cine.html", valorPago=total_global)

        except ValueError:
            return render_template("cine.html", valorPago="Error: Ingrese valores numéricos válidos para compradores y boletos.")

    return render_template("cine.html", valorPago=0)


            
            

        
        



if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)


