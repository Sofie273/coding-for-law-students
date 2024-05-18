#
# Projekt - VW: Modul zum Generieren von PDFs
#
#

import pdfkit, datetime

def generiere_schreiben():### Definiere hier in der Funktion welche Paramter du mitgeben möchtest

        ### Hier wird der Briefkopf definiert, dieser ist mit HTML formatiert
        html = """
                <p style = "float:right;">
                Kanzlei Spa&szlig;v&ouml;gel und Partner <br/>
                Im Spa&szlig;weg 3<br/>
                12345 Spa&szlig;stadt
                </p><br/><br/><br/><br/>
                <p style = "align:left;">
                <b>An die <br/>
                Volkswagen AG<br/>
                Berliner Ring 2<br/>
                38440 Wolfsburg</b>
                </p><br/>"""

        html += """
                <p style = "float:right;">
                Frankfurt, den""" 

        html += ### füge hier das aktuelle Datum ein

        html +=   "<br/> Aktenzeichen 22/"

        html += ### füge hier das Aktenzeichen ein
        
        html += " </p><br/><br/>"

        html += """
                <h1>Geltendmachung von Schadensersatzanspr&uuml;chen</h1><br/>

                <p>Sehr geehrte Damen und Herren,</p>
                <p>in der vorgenannten Angelegenheit zeige ich mit beiliegender Vollmacht an, dass mich 
                """ 
        html += ### füge hier den Namen ein
        html += ", " 
        html += ### füge hier die Anschrift ein
        
        html += "mit der Wahrnehmung seiner/ihrer Interessen beauftragt hat.</p>"

        #FALLS Motortyp = EA189 dann:
        motortyp_EA189 = """<h2>Anspruch auf Schadensersatz aus &sect; 852 BGB <h2><br/>
                Sie haben unseren Mandanten durch den Einbau einer unzul&auml;ssigen Abschalteinrichtung sittenwidrig gesch&auml;digt. 
                Daraus ist unserem Mandanten ein Schaden i.H.v. """
        motortyp_EA189 += ### füge hier den Preis ein
        motortyp_EA189 += """ &euro; wegen des Abschluss des Kaufvertrages enstanden (BGH, Urteil vom 25. Mai 2020 - VI ZR 252/19). 
                Jedoch ist die Nutzung des Autos mit """
        motortyp_EA189 += ### Berechne: Kaufpreis *0.4 * Tachostand heute - Tachostand bei Kauf)/1000)
        motortyp_EA189 += """ &euro; anzurechnen (vgl. Damit besteht ein Anspruch unseres Mandanten gegen Sie i.H.v. aus § 852 BGB Zug-um-Zug gegen &Uuml;bergabe und &Uuml;bereignung des Autos. 
                Die Verj&auml;hrungsfrist beträgt 10 Jahre und ist demnach noch nicht eingetreten (vgl. BGH, Urteile vom 21. Februar 2022 – VIa ZR 8/21 und VIa ZR 57/21).
                <p>
                Beweis:<br/>
                AdHoc-Meldung Volkswagen AG <br/>
                Diverse Zeitungsberichte
                </p>"""

        #FALLS Motortyp = EA288 dann:
        
        motortyp_EA288 = """<h2>Anspruch auf Schadensersatz aus &sect; 826 BGB </h2><br/>
                Sie haben unseren Mandanten durch den Einbau einer unzul&auml;ssigen Abschalteinrichtung sittenwidrig gesch&auml;digt. 
                Daraus ist unserem Mandanten ein Schaden i.H.v. """ 
        motortyp_EA288 += ### füge hier den Preis ein
        motortyp_EA288 +="""&euro; wegen des Abschluss des Kaufvertrages enstanden (BGH, Urteil vom 25. Mai 2020 - VI ZR 252/19). 
                Jedoch ist die Nutzung des Autos mit """ 
        motortyp_EA288 += ### Berechne: Kaufpreis *0.4 * Tachostand heute - Tachostand bei Kauf)/1000)
        motortyp_EA288 +="""&euro; anzurechnen (vgl. Damit besteht ein Anspruch unseres Mandanten gegen Sie i.H.v. aus &sect; 852 BGB Zug-um-Zug gegen &Uuml;bergabe und &Uumlbereignung des Autos. 
                <p>
                Beweis:<br/>
                AdHoc-Meldung Volkswagen AG<br/>
                Diverse Zeitungsberichte
                </p>"""


        ### füge hier die Unterscheidung nach Motortyp an
    

        html += """ Mit freundlichen Gr&uuml;&szlig;en<br/>
                Dr. Scherz<br/>
                Scherzanwalt
                """

        # Diese Funktion macht aus unserem HTML ein PDF Dokument
        pdfkit.from_string(html,('Anschreiben_','.pdf')) ### füge das Aktenzeichen mit in den Dateinamen ein

