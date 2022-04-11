"""1. Avere l’elenco delle linee tranviarie e di bus che hanno un percorso la cui lunghezza è compresa tra due valori
inseriti dall’utente. Ordinare le linee in ordine crescente sul numero della linea.
2. Avere un elenco di tutte le linee (tram e bus) che passano in un certo quartiere. L’utente inserisce il nome del
quartiere (anche solo una parte del nome) e il sito risponde con l’elenco ordinato in ordine crescente delle linee
che passano in quel quartiere
3. Avere la mappa della città con il percorso di una linea scelta dall’utente. L’utente sceglie il numero della linea da
un menù a tendina (le linee devono essere ordinati in ordine crescente), clicca su un bottone e ottiene la mappa
di Milano con il percorso della linea prescelta"""
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


linee = pd.read_csv('/workspace/flask/tpl_percorsi_shp (1).zip',sep=';')
quartieri = gpd.read_file('/workspace/flask/verificaA/ds964_nil_wm.zip')
@app.route('/', methods=['GET'])
def home():
    return render_template('homec.html')

@app.route("/selezione", methods=["GET"])
def selezione():
  scelta = request.args['scelta']
  #in base alla scelta del radio button ti porta a diverse rotte
  if scelta == 'es1':
    return redirect(url_for('distanza'))
  elif scelta == 'es2':
    return redirect(url_for('input'))
  else:
    return redirect(url_for('dropdown'))

@app.route("/distanza", methods=["GET"])
def distanza():
  return render_template("distanza.html")

@app.route("/elenco", methods=["GET"])
def elenco():
  min = request.args['valoreI']
  max = request.args['valoreF']
  l_linee = linne[(linne["lung_km"]>min) & linee["lung_km"]< max].sort_values("linea")
  return render_template("elenco.html",tabella = l_linee.to_html())





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)