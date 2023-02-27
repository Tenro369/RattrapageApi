import json
import requests

def requestApi(theme): # Requete pour récupperer les infos dans l'API celon un theme entrer en parametre

    myAPIKEY = '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'

    haiku = requests.post(url="https://api.openai.com/v1/completions",
        headers=
        {'Content-Type': 'application/json','Authorization': 'Bearer '+myAPIKEY}
        ,
        data= json.dumps({
            "model": "text-davinci-003", 
            "prompt": "generates a poem about ".join(theme), # Genere le haiku celon le theme choisi
            "temperature": 0,
            "max_tokens": 64
        })
    )

    file1 = open("Haikus.txt", "a")
    file1.write(theme + ": " + haiku.json()["choices"][0]["text"] + "\n@")
    file1.close()

    returnValue = {
        'about' : theme,
        'text' : haiku.json()["choices"][0]["text"]
    }

    print(returnValue)
    return returnValue

if __name__ == "__main__":
    requestApi(input("Theme: "))
    
