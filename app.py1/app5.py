#si vuole realizzare un sito che memoriiza le squadre di caalcio.
#l'utente deve poter inserire il nome della squadra e la data di fondazione  e la città 
#deve inoltre poter effetuare delle ricerche inserendo 1 dei valori delle colonne e ottenere i dati presenti.
from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template('')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)