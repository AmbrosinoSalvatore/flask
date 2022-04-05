from flask import Flask,render_template,request, Response,redirect,url_for
app = Flask(__name__)
# pip install flask pandas contextily geopandas matplotlib
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import geopandas as gpd
import io
import pandas as pd
stazioni = pd.read_csv('/workspace/flask/templates/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv',sep=';')
stazionigeo = gpd.read_file('/workspace/flask/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson',sep=';')
quartieri = gpd.read_file('/workspace/flask/ds964_nil_wm.zip')
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/selezione', methods=['GET'])
def selezione():
    #capire quale radiobutton è stato selezionato
    scelta=request.args['scelta']
    if scelta == 'es1':
        return redirect(url_for('numero'))
    elif scelta == 'es2':
        return redirect(url_for('input'))
    else:
        return redirect(url_for('dropdown'))

@app.route('/numero', methods=['GET'])
def numero():
    global risultato
    #numero stazioni per ogni municipio
    risultato=stazioni.groupby('MUNICIPIO')['OPERATORE'].count().reset_index()
    return render_template('elenco.html',risultato=risultato.to_html())

@app.route('/grafico', methods=['GET'])
def grfico():
    #costruzione del grafico
    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.OPERATORE

    ax.bar(x, y, color = "#304C89")
    #visualizzazione del grafico
    output = io.BytesIO()#STABILIRE IL CANALE DI COMUNICAZIONE
    FigureCanvas(fig).print_png(output)#stampare l'immagiine sull'output
    return Response(output.getvalue(), mimetype='image/png')#mandare in risposta quello che c'e nell'output e gli diciamo che è un immagine

@app.route('/ricerca', methods=['GET'])
def ricerca():
  quartiere = request.args['quartieri']
  quartiereUtente = quartieri[quartieri['NIL'].str.contains(quartiere)]
  stazioniQuartieri = stazionigeo[stazionigeo.within(quartiereUtente.geometry.squeeze())]
  return render_template('elenco1.html', risultato = stazioniQuartieri.to_html())

@app.route('/input', methods=['GET'])
def input():
    return render_template('input.html')

@app.route('/dropdown', methods=['GET'])
def dropdown():
    nomistazioni = stazioni.OPERATORE.to_list()
    nomistazioni = list(set(nomistazioni))
    nomistazioni.sort()
    return render_template('dropdown.html', stazioni = nomistazioni)

@app.route('/sceltastazioni', methods=['GET'])
def sceltastazioni():
    stazione = request.args['stazione']
    stazione_utente = stazionigeo[stazionigeo.OPERATORE == stazione]
    quartiere = quartieri[quartieri.contains(stazione_utente.geometry.squeeze())]
    return render_template(lista_stazione.html,quartiere=quartiere)

@app.route('/mappaquarieri', methods=['GET'])
def mappaquart():
  fig, ax = plt.subplots(figsize = (12,8))
  quartiere1.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor='k')
  stazioni_utente.to_crs(epsg=3857).plot(ax=ax, color='r', edgecolor='k')
  ctx.add_basemap(ax=ax)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)