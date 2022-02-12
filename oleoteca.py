from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao_oleo import*
from flask_mysqldb import MySQL
from modelo import*


app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "cimento1"
app.config['MYSQL_DB'] = "oleoteca"
app.config['MYSQL_PORT'] = 3306
app.secret_key = 'cimento1'
db = MySQL(app)
oleo_dao = DAO(db)

@app.route('/')
def index():
    lista = oleo_dao.listar()
    return render_template('lista_oleos.html', oleos=lista)

@app.route('/criar', methods=['POST',])
def criar():
    corrente = request.form['corrente']
    api = request.form['api']
    nafta = request.form['nafta']
    diesel = request.form['diesel']
    gasoleo = request.form['gasoleo']
    enxofre = request.form['enxofre']
    nitrogenio = request.form['nitrogenio']
    tan = request.form['tan']
    oleo = Oleo(corrente,api,nafta,diesel,gasoleo,enxofre,nitrogenio,tan)
    oleo_dao.salvar(oleo)
    return redirect(url_for('index'))

@app.route('/novo')
def novo():
    return render_template('adicionar_oleos.html')

@app.route('/deletar/<int:ide>')
def deletar(ide):
    oleo_dao.deletando(ide)
    flash("O jogo foi removido com sucesso")
    return redirect(url_for('index'))

@app.route('/editar/<int:ide>')
def editar(ide):
    oleo = oleo_dao.busca_por_id(ide)
    return render_template('edita_oleos.html', oleo=oleo)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    corrente = request.form['corrente']
    api = request.form['api']
    nafta = request.form['nafta']
    diesel = request.form['diesel']
    gasoleo = request.form['gasoleo']
    enxofre = request.form['enxofre']
    nitrogenio = request.form['nitrogenio']
    tan = request.form['tan']
    oleo = Oleo(corrente,api,nafta,diesel,gasoleo,enxofre,nitrogenio,tan,ide=request.form['ide'])
    oleo_dao.salvar(oleo)
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
