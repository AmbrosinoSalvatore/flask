from flask import Flask, render_template, request
app = Flask(__name__)
capoluoghi_Regione = {"Abruzzo" :"L'Aquila", "Basilicata" : "Potenza", "Calabria" : "Catanzaro", "Campania" : "Napoli", "Emilia-Romagna" :"Bologna", "Friuli-Venezia" : "Trieste", "Lazio" :	"Roma", "Liguria" :	"Genova", "Lombardia" :	"Milano", "Marche" : "Ancona", "Molise" :	"Campobasso", "Piemonte"	: "Torino", "Puglia" :	"Bari", "Sardegna" :	"Cagliari", "Sicilia" :	"Palermo", "Toscana"	: "Firenze", "Trentino-Alto Adige" :	"Trento", "Umbria" :	"Perugia", "Valle d'Aosta" :	"Aosta", "Veneto" :	"Venezia" }


@app.route('/', methods=['GET'])
def home_page():
    return render_template("Scegli.html")

@app.route('/data', methods=['GET'])
def data():
    scelta = request.args["Scegli"]
    if scelta == "Regione":
        return render_template("cap.html")
    else:
        return render_template("reg.html")
    

@app.route("/dataReg", methods=["GET"])
def dataReg():
    regione = request.args["Regione"]
    for key, value in capoluoghi_Regione.items():
        if regione == key:
            capoluogo = value
            return render_template("risposta.html", risultato = capoluogo)
    return render_template("erroree.html")

@app.route("/dataCap", methods=["GET"])
def dataCap():
    capoluogo = request.args["Capoluogo"]
    for key, value in capoluoghi_Regione.items():
        if capoluogo == value:
             regione = key
             return render_template("risposta.html", risultato = regione)
    return render_template("error.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)