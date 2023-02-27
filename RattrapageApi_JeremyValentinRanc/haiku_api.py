from re import T
from flask import Flask, jsonify
import take_api

app = Flask(__name__)

file1 = open("Haikus.txt", "r")
tabHaikus = file1.read().split("@") # Sépare chacun des haikus dans du fichier
file1.close()

tab = []

for i in tabHaikus: # Sépare les infos du fichier pour chaque haiku
    if len(i) == 0:continue
    k = i.split(':')
    tab.append({
        'about' : k[0],
        'text' : k[1]
    })

def saveHaikus(): # Sauvegarde les haikus permettant la suppression et le changement d'un haiku
    file1 = open("Haikus.txt", "w")
    for i in tab:
        file1.write(i["about"] + ": " + i["text"] + "\n@")
    file1.close()


@app.route("/") # Lien permettant d'accéder à tous les haikus
def all():
    return jsonify(tab)


@app.route('/api/haiku/<theme>') # Lien permettant de voir un haiku celon son theme
def haiku(theme):
    for i in tab:
        if(i["about"]==theme):
            return jsonify(i)
            
    return jsonify(take_api.requestApi(theme))
    

@app.route('/api/haiku/<theme>/<modif>') # Lien permettant de changer le texte d'un haiku celon son theme
def haiku_modif(theme, modif):
    for i in tab:
        if(i["about"]==theme):
            i["text"] = modif
            saveHaikus()
            return jsonify(i)

@app.route('/api/haiku/<theme>/delete') # Lien permettant de supprimer un haiku celon son theme
def haiku_delete(theme):
    for i in range(len(tab)):
        if(tab[i]["about"]==theme):
            tab.pop(i)
            saveHaikus()
            return jsonify(i)

if __name__ == "__main__":
    app.run(debug=True)
