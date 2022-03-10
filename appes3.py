#realizzare un server web che permetta di conoscere capoluoghi di regione.
#utente inserisce il nome della regione e il programma restituisce il nome del capoluogo de regione
#caricare i capoluoghi di regione in una lista di dizionari
#modificare l'es precedente per permettere all'utente di inserire un capoluogo e avere la regione in cui si trova
#l'utente sceglie se avere il capologo o la regione
from flask import Flask,render_template,request
app = Flask(__name__)
capoluoghiRegione = {'Abruzzo' : 'Aquila', 'Basilicata' : 'Potenza', 'Calabria' : 'Catanzaro', 'Campania' : 'Napoli ', 'Emilia-Romagna' : 'Bologna', 'Friuli Venezia Giulia' : 'Trieste','Lazio' : 'Roma','Liguria' : 'Genova', 'Lombardia' : 'Milano', 'Marche' : 'Ancona','Molise' : 'Campobasso','Piemonte' : 'Torino','Puglia' : 'Bari','Sardegna' : 'Cagliari','Sicilia' : 'Palermo','Toscana' : 'Firenze','Trentino-Alto Adige' : 'Trento','Umbria' : 'Perugia','Valle Aosta' : 'Aosta','Veneto' : 'Venezia'}

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('capo.html')

@app.route('/data', methods=['GET'])
def data():
    # prende la regione scritta dall'utente
    regione = request.args["reg_cap"]
    # crea la variabile capoluogo e vi inserisce il capoluogo di quella regione
    # se la regione non ce restituisce il messaggio 'regione non esistente'
    capoluogo=capoluoghiRegione.get(regione,'regione non esistente' )
    
    return render_template('reg.html',reg=capoluogo)

        








if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)