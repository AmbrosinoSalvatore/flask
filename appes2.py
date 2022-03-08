#realizzare un sitoweb che permetta la registrazione degliu utenti
#l'utente inserisce il nome,username,password
#connferma password e il sesso.
#se le informazioni sono corrette il sito salva le informazioni in una struttura dati opportuna(lista dizionari)
#prevedere la possibilità di fare il login inserendo 
#username e password 
#se sono corrette fornire un messaggio di benvenuto diverso a secondo del sesso 
from flask import Flask,render_template,request
app = Flask(__name__)
lista = []

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('es2.html')

@app.route('/data', methods=['GET'])
def data():
    username = request.args["username"]
    password = request.args["password"]
    name = request.args['Name']
    conferma_password = request.args['conferma_password']
    sex = request.args['Sex']
    if password == conferma_password:
        lista.append({'name':name,'username':username,'password':password,'sex':sex})
        return render_template('login.html')
    else:
        return render_template('errore.html')

@app.route('/login', methods=['GET'])
def login():
    username_log = request.args["username"]
    password_log = request.args["password"]
    for i in lista:
        if i == 'password':
            p = i
    else:
        p = 's'


    if password_log == p:
        return render_template('welcome.html',nome_user=username_log)
    else:
        return render_template('errore.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)