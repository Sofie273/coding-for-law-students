#
# Projekt III - Facebook: Anwendung zur Überprüfung der Betroffenheit einer Datenpanne, Generierung eines Dokuments
#
#

### Hier importieren wir die benötigten Bibliotheken
import Brief as Brief
import datetime
import pandas as pd


### Hier definieren wir unsere globalen Variablem, also Variablen, die für den gesamten Programmablauf zur Verfügung stehen sollen
texts = {
    "account": "Haben Sie einen Facebook-Account?",
    "mobil": "Bitte geben Sie ihre Telefonnummer ein:",
    "name": "Bitte geben Sie Ihren vollständigen Namen an.",
    "email_vorhanden": ["Wir haben zu Ihrem Facebook Account folgende E- Mailadresse gefunden:","Dürfen wir Sie auf der gleichen E-Mail Adresse kontaktieren?"],
    "email_nicht_vorhanden": "Wir haben zu Ihrem Facebook Account keine E- Mailadresse gefunden.",
    "email_input": "Bitte geben Sie Ihre E-Mail Adresse ein, über die wir sie kontaktieren dürfen:",
    "anschrift": "Bitte geben Sie Ihre vollständige Anschrift an:"
}

daten = pd.read_csv("export.csv")

answers = {}

### Mit dieser Funktion können wir die Fragen an unsere User stellen
def get_user_input(question):
    answer = input(question)
    return answer

def find_mobile_number(mobile):
    return mobile in daten.Mobil.values

def find_email(mobile):
    return daten[daten.Mobil == mobile]["EMail"].values


### Hier definieren wir unsere Logik
def main():

    answers["account"] = get_user_input(texts["account"])

    if answers == "nein":
        print("Sie sind ziemlich sicher nicht vom Datenleck betroffen.")
        return

    answers["mobil"] = get_user_input(texts["mobil"])

    if find_mobile_number(answers["mobil"]) == False:   
        print("Die Mobilnummer wurde nicht im Datensatz gefunden.\nVermutlich sind Sie nicht vom Datenleck betroffen.")
        return
    
    answers["name"] = get_user_input(texts["name"])

    email = find_email(answers["mobil"])

    if email != None:
        answers["mail_vorhanden"] = get_user_input(texts["email_vorhanden"][0]+email+texts["email_vorhanden"][1])

        if answers["mail_vorhanden"] == "nein":
            answers["email"] = get_user_input(texts["email_input"])
        else:
            answers["email"] = email
    else:
        print(texts["email_nicht_vorhanden"])
        answers["email"] = get_user_input(texts["email_input"])

    answers["anschrift"] = get_user_input(texts["anschrift"])

    Brief.generiere_schreiben(answers, answers["mobil"][-5:])
    

### Dieser Aufruf führt dazu, dass diie Funktion "main" bei Ausführen des Python Programms ausgeführt wird
if __name__ == '__main__':
    main()