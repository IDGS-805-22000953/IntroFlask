from flask import Flask,render_template, request

app=Flask(__name__)

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
                precio_unitario = 12
                total_global = boletos * precio_unitario

                
                if boletos <= 7 * compradoresC:
                    if 3 <= boletos <= 5:
                        total_global -= total_global * 0.10  
                    elif boletos >= 6:
                        total_global -= total_global * 0.15  

                
                if metodo_pago == "si":
                    total_global -= total_global * 0.10 

              
                total_global = round(total_global, 2)

                return render_template("cine.html", valorPago=total_global)

        except ValueError:
            return "Error: Ingrese valores numéricos válidos para compradores y boletos."

    return render_template("cine.html", valorPago=0)

            
            
            
            
        
        



if __name__=="__main__":
    app.run(debug=True,port=3000)


