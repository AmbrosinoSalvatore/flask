#realizzare un serverweb che visualizzi l'ora attuale e colori lo sfondo in base all'orario:colore per la mattina uno per il pome uno per la sera e uno per la notte
from flask import Flask,render_template
app = Flask(__name__)

from datetime import date

today = date.today()
@app.route('/', methods=['GET'])
def ora():
    if today > 7 and < 12
    return render_template('ora.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)