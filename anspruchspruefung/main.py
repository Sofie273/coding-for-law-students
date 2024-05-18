#
# Projekt I: Chatbot zu einer einfachen Anspruchsprüfung
#
#

### Dieser Befehl importiert die Fragen aus der Datei "texte"
import texte
texte = texte.Texte()

### Zu Anfang definieren wir unsere globalen Variablen, also die Variablen, die für das gesamte Programm verfügbar sein sollen
answers = {
    "schuldverhältnis":[],
    "pflichtverletzung": [],
    "verschulden": [],
    "fristsetzung": [],
    "mahnung": [],
    "schaden": [],
    "ergebnis": []
}

### Mit dieser Funktion können wir die Fragen an unsere User stellen
def get_user_input(question):
    answer = input("\n"+question+"\n")
    return answer

### Hier implementieren wir die Logik der Anspruchsprüfung
### Wir gehen einfach davon aus, dass immer "ja" oder "nein" geantwortet wird
def main():

    for frage in texte.schuldverhältnis:
        answers["schuldverhältnis"].append(get_user_input(texte.schuldverhältnis[frage]))

    if not("ja" in answers["schuldverhältnis"]):
        print(texte.abbruch["8.1"])
        return
    
    for frage in texte.pflichtverletzung:
        answers["pflichtverletzung"].append(get_user_input(texte.pflichtverletzung[frage]))

    if not("ja" in answers["pflichtverletzung"]):
        print(texte.abbruch["8.1"])
        return
    
    answers["verschulden"] = get_user_input(texte.verschulden["3.1"])

    if answers["verschulden"] == "nein":
        print(texte.abbruch["8.1"])
        return
    
    ### Fristsetzung 
    if answers["pflichtverletzung"][2] == "ja": #es geht um Frage 2.3, da index bei 0 anfängt müssen wir eins niedriger anfangen
        for frage in texte.fristsetzung:
            answers["fristsetzung"].append(get_user_input(texte.fristsetzung[frage]))
        
        if "nein" in answers["fristsetzung"]:
            print(texte.abbruch["8.1"])
            return
        
    ### Mahnung
    if answers["pflichtverletzung"][3] == "ja":
        for frage in texte.mahnung:
            answers["mahnung"].append(get_user_input(texte.fristsetzung[frage]))
        
        if "nein" in answers["mahnung"]:
            print(texte.abbruch["8.1"])
            return
        
    ### Schaden
    if answers["pflichtverletzung"][0] == "ja":
        answers["schaden"][0] = get_user_input(texte.schaden["6.1"])

        if answers["schaden"][0] == "ja":
            answers["schaden"][1] = get_user_input(texte.schaden["6.2"])

    if answers["pflichtverletzung"][1] == "ja":
        answers["schaden"][2] = get_user_input(texte.schaden["6.3"])
        answers["schaden"][3] = get_user_input(texte.schaden["6.4"])

        if answers["schaden"][2] == "ja" or answers["schaden"][3] == "ja":
            answers["schaden"][4] = get_user_input(texte.schaden["6.5"])

    if answers["pflichtverletzung"][2] == "ja":
        answers["schaden"][5] = get_user_input(texte.schaden["6.6"])

        if answers["schaden"][5] == "ja":
            answers["schaden"][6] = get_user_input(texte.schaden["6.7"])

    if answers["pflichtverletzung"][3] == "ja":
        answers["schaden"][7] = get_user_input(texte.schaden["6.8"])

        if answers["schaden"][7] == "ja":
            answers["schaden"][8] = get_user_input(texte.schaden["6.9"])

    ### Ergebnis
    if answers["schaden"][0] == "ja":
        print(texte.ergebnis["7.1"][0]+answers["schaden"][1]+texte.ergebnis["7.1"][1])

    if answers["schaden"][2] == "ja" or answers["schaden"][3] == "ja":
        print(texte.ergebnis["7.2"][0]+answers["schaden"][4]+texte.ergebnis["7.2"][1])
    
    if answers["schaden"][5] == "ja":
        print(texte.ergebnis["7.3"][0]+answers["schaden"][6]+texte.ergebnis["7.3"][1])

    if answers["schaden"][7] == "ja":
        print(texte.ergebnis["7.4"][0]+answers["schaden"][8]+texte.ergebnis["7.4"][1])

    print("Sollten Sie keine Rückmeldung bekommen haben, liegt kein Anspruch auf Schadensersatz gem. §§ 280 ff. BGB vor.")

    
### Dieser Aufruf führt dazu, dass diie Funktion "main" bei Ausführen des Python Programms ausgeführt wird
if __name__ == '__main__':
    main()