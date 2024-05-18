#
# Projekt II - VW: Anwendung zur Überprüfung der Betroffenheit vom Abgasskandal, Generierung eines Anwaltsschreibens
#
#

### Hier importieren wir die benötigten Bibliotheken
import Brief as Brief
import datetime


### Hier definieren wir unsere globalen Variablem, also Variablen, die für den gesamten Programmablauf zur Verfügung stehen sollen


texts = {
    "marke": "Welche Automarke haben Sie gekauft? Geben Sie VW, Audi, Seat, Skoda, BMW oder Mercedes an.",
    "motor": "Welchen Motortyp haben Sie? Geben sie EA189 oder EA288 an.",
    "kauf-datum": "Wann haben Sie das Auto gekauft?",
    "kauf-ort": "Wo haben sie das Auto gekauft?",
    "kauf-preis": "Wie viel haben Sie gezahlt?",
    "kilometer-kauf": "Wie war der anfängliche Kilometerstand bei Kauf des Autos?",
    "kilometer-aktuell": "Wie ist der aktuelle Tachostand des Autos?",
    "name": "Bitte geben Sie Ihren vollständigen Namen ein:",
    "anschrift": "Bitte geben Sie Ihre vollständige Anschrift an"
}

aktenzeichen = "1"
answers = {}

### Mit dieser Funktion können wir die Fragen an unsere User stellen
def get_user_input(question):
    answer = input(question)
    return answer

### Hier definieren wir unsere Logik
def main():

    answers["marke"] = get_user_input(texts["marke"])

    if answers["marke"] not in ("VW","Audi","Seat","Skoda","BMW","Mercedes"):
        print("Ungültige Eingabe. Programm wird abgebrochen.")
        return ## damit brechen wir die Funktion ab
    elif answers["marke"] in ("BMW","Mercedes"):
        print("Diese Marken sind nicht betroffen. Programm wird abgebrochen.")
        return
    
    answers["motor"] = get_user_input(texts["motor"])

    if answers["motor"] not in ("EA189","EA288"):
        print("Ungültige Eingabe. Programm wird abgebrochen.")
        return
    
    answers["kauf-datum"] = get_user_input(texts["kauf-datum"])

    purchase_date = datetime.datetime.strptime(answers["kauf-datum"]) 

    if answers["motor"] == "EA189" and purchase_date < datetime.datetime.strptime("01.01.2012"):
        print("Ihr Anliegen ist leider bereits verjährt.")
        return
    if answers["motor"] == "EA189" and purchase_date > datetime.datetime.strptime("22.09.2015"):
        print("Ihr Motor ist nicht betroffen.")
        return
    if answers["motor"] == "EA288" and purchase_date < datetime.datetime.strptime("01.01.2012"):
        print("Ihr Anliegen ist leider bereits verjährt.")
        return
    if answers["motor"] == "EA288" and purchase_date > datetime.datetime.strptime("12.09.2019"):
        print("Ihr Motor ist nicht betroffen.")
        return

    answers["kauf-ort"] = get_user_input(texts["kauf-ort"])
    answers["kauf-ort"] = int(get_user_input(texts["kauf-preis"]))
    answers["kilometer-kauf"] = int(get_user_input(texts["kilometer-kauf"]))
    answers["kilometer-aktuell"] = int(get_user_input(texts["kilometer-aktuell"]))
    answers["name"] = get_user_input(texts["name"])
    answers["anschrift"] = get_user_input(texts["anschrift"])

    Brief.generiere_schreiben(answers, aktenzeichen)

    aktenzeichen = str(int(aktenzeichen)+1)


### Dieser Aufruf führt dazu, dass diie Funktion "main" bei Ausführen des Python Programms ausgeführt wird
if __name__ == '__main__':
    main()