#si vuole realizzare un sito web che permetta di visualizzare alcune informazioni sull'andamento dell'epidemia di covid nel nostro paese a partiredai dati presenti nel file
#l'utente sceglie la regione da un elenco(menu a tendina),clicca su un bottone e il sito visualizza una tabella contenente le informazioni relative alla regione
#i dati da inserire nel menu a tendine devono essere caricati automaticamente da una pagina
from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv')

@app.route('/', methods=['GET'])
def home():
    return render_template('tendina.html')

@app.route('/data', methods=['GET'])
def data():
    #prende la regione scelta dall'utente
    regione = request.args['City']
    #df_result prende tutti i dati della regione inserita dall'utente
    df_result = df[df['nome_area'] == regione]
    #restituisce l'html ris  e converte il dataframe nell'html
    return render_template('ris.html', tables=[df_result.to_html()], titles=[''])



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)