#
# Projekt III - Facebook: Modul zum Generieren von PDFs
#

import pdfkit, datetime

def generiere_schreiben(antwort_dict):
        ### Hier wird der Briefkopf definiert
        html = """
                <p style = "float:right;">
                Kanzlei Spa&szlig;v&ouml;gel und Partner <br/>
                Im Spa&szlig;weg 3<br/>
                12345 Spa&szlig;stadt
                </p><br/><br/><br/><br/>
                <p style = "align:left;">
                <b>An die <br/>
                Meta Platforms Ireland<br/>
                4 Grand Canal Square<br/>
                Grand Canal Harbour<br/>
                Dublin 2<br/>
                Ireland
                </b></p><br/>"""

        html += """
                <p style = "float:right;">
                Frankfurt, den """
        html += ### füge hier das aktuelle Datum ein
        html += "<br/>Aktenzeichen 22/"
        html += ### füge hier das Aktenzeichen ein
        html += " </p><br/><br/><br/><br/>"

        # Beginn Inhalt Schreiben
        html += """
                <h1>Geltendmachung von Schadensersatzanspr&uuml;chen und Vergleichsangebot</h1><br/>

                <p>Sehr geehrte Damen und Herren,</p>
                <p>in der vorgenannten Angelegenheit zeige ich mit beiliegender Vollmacht an, dass mich 
                """  
        html += ### füge hier den Namen ein
        html += ", "
        html += ### füge hier die Anschrift ein
        html += "mit der Wahrnehmung seiner/ihrer Interessen beauftragt hat.</p>"

        html += """
                <h2>1.	Anspruch auf Schadensersatz i.H.v. 5000&euro;</h2><br/>
                <p>
                Die Daten unseres Mandanten wurden in einer Datenpanne, die sie verschuldet haben, ver&ouml;ffentlicht. 
                Daraus ist unserem Mandanten ein immaterieller Schaden i.H.v. 5000&euro; wegen der Ver&ouml;ffentlichung seiner Daten enststanden. 
                Der Anspruch folgt aus Art. 82 Abs. 1 DSGVO. <br/>

                Beweis: <br/>
                Hamburger Datenschutzbeauftragter<br/>
                (<a href="https://datenschutz-hamburg.de/pages/fb-leak/">https://datenschutz-hamburg.de/pages/fb-leak/</a> ) <br/>
 		Diverse Zeitungsberichte
                </p>

                <h2>2.	Vergleichsangebot</h2><br/>     
                Meinem Mandanten ist es dennoch bewusst, dass zur Geltendmachung des Schadens ein l&auml;ngeres Gerichtsverfahren n&ouml;tig sein k&ouml;nnte.<br/>
                Um die Angelegenheit daher g&uuml;tlich beizulegen, unterbreitet mein Mandant folgenden Vergleich:
                <ol>
                        <li>Mein Mandant verzichtet auf die Geltendmachung von jeglichen Schadensersatzanspr&uuml;chen, die aus der Datenpanne entstanden sind.</li>
                        <li>Ihre Partei zahlt an meinen Mandanten, f&uuml;r die Verletzung seiner Daten einen Betrag in H&ouml;he von &euro;1000,00. Die Zahlung ist innerhalb von 14 Tagen nach Vertragsschluss f&auml;llig.</li>
                        <li>Wechselseitige Anspr&uuml;che aus dem Mietverh&auml;ltnis sind im &Uuml;brigen hiermit abgegolten.</li>
                        <li>Ihre Partei verpflichtet sich, meine anliegende Geb&uuml;hrenrechnung i.H.v. 800&euro; auszugleichen und meinen Mandanten von einer dahingehenden Zahlung freizustellen.</li>
                </ol> """

        #Fußzeile
        html += """ Mit freundlichen Gr&uuml;&szlig;en<br/>
                Dr. Scherz<br/>
                Scherzanwalt
                """

        pdfkit.from_string(html,('Anschreiben_','.pdf')) ### füge das Aktenzeichen mit in den Dateinamen ein

