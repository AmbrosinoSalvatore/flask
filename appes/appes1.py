#realizzare un server web che permetta di effettuare il login
#l'utente inserisce l'username e la password
#se l'username è admin e la password è xxx123# 
#il sito ci saluta con messaggio di benvenuto
#altrimenti ci da un messaggio di errore 
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('eslogin.html')

@app.route('/data', methods=['GET'])
def data():
    username = request.args["username"]
    password = request.args["password"]
    if username == 'admin' and password == 'xxx123#':
        return render_template('welcome.html',nome=username)
    else:
        return render_template('errore.html')


    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)