#1. Avere un elenco di tutte le stazioni radio che si trovano in un certo quartiere. L’utente sceglie il nome del quartiere da un elenco di radiobutton (ordinato in ordine alfabetico) e clicca su un bottone. Il sito risponde con
#l’elenco ordinato in ordine alfabetico delle stazioni radio presenti in quel quartiere
#2. Avere le stazioni radio presenti in un quartiere. L’utente inserisce il nome del quartiere (anche solo una parte di
#esso), clicca su un bottone e ottiene la mappa del quartiere con un pallino nero sulla posizione delle stazioni radio
#3. Avere il numero di stazioni per ogni municipio (in ordine crescente sul numero del municipio) e il grafico corrispondente
from flask import Flask, render_template, send_file, make_response, url_for, Response,request,redirect
app = Flask(__name__)
# pip install flask pandas contextily geopandas matplotlib
import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

stazioni = pd.read_csv('/workspace/flask/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv',sep=';')
stazionigeo = gpd.read_file('/workspace/flask/verificaA/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson',sep=';')
quartieri = gpd.read_file('/workspace/flask/verificaA/ds964_nil_wm.zip')

@app.route('/', methods=['GET'])
def home():
    return render_template('homeb.html')
#1
@app.route('/es1', methods=['GET'])
def es1():
    nomi_quartieri = quartieri.NIL.to_list()
    return render_template('home_es1.html',quartieri=nomi_quartieri)

@app.route('/elenco', methods=['GET'])
def elenco():
    quartiere = request.args['quartiere']
    quartiere_utente = quartieri[quartieri.NIL == quartiere] 
    stazioni_q = stazionigeo[stazionigeo.within(quartiere_utente.geometry.squeeze())]
    return render_template('elencob.html',risultato=stazioni_q.to_html())
#2v
@app.route('/es2', methods=['GET'])
def es2():
    return render_template('home_es2.html')

@app.route('/ricerca_stazioni', methods=['GET'])
def staz():
    global quartiere_utente,stazioni_quar
    quartiere = request.args['quartiere']
    quartiere_utente = quartieri[quartieri.NIL.str.contains(quartiere)]
    stazioni_quar = stazionigeo[stazionigeo.intersects(quartiere_utente.geometry.squeeze())]
    return render_template('mappa.html')

@app.route('/mappa', methods=['GET'])
def mappa():
    fig, ax = plt.subplots(figsize = (12,8))
    quartiere_utente.to_crs(3857).plot(ax=ax,alpha=0.3,edgecolor='k')
    stazioni_quar.to_crs(3857).plot(ax=ax,color='k')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    
    return Response(output.getvalue(), mimetype='image/png')
#3
@app.route('/es3', methods=['GET'])
def es3():
    global risultato
    risultato = stazioni.groupby('MUNICIPIO')['OPERATORE'].count().reset_index()
    return render_template("tabella.html",risultato=risultato.to_html())

@app.route('/grafico', methods=['GET'])
def graf():
    fig, ax = plt.subplots(figsize = (12,8))
    x = risultato.MUNICIPIO
    y = risultato.OPERATORE
    ax.bar(x,y)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)  
    return Response(output.getvalue(), mimetype='image/png')

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)