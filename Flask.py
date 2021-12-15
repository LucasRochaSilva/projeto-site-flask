from flask import Flask, render_template

app = Flask(__name__)


# route > "seu site aqui : http://127.0.0.1:5000/"
@app.route('/')
# função > oque voce quer exibir naquela pagina
def homepage():
    return render_template("homepage.html")


@app.route("/virtus")
def virtus():
    return render_template("virtus.html")


@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")


# colocar o site no ar
app.run()
