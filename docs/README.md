Das Projekt von Mustache beschreibt eine Fashion Webseite, die es ermöglicht Kunden und Beratern je nach ausgewählten Fashion - Präferenzen, in über die Plattform in Kontakt zu treten. Hierbei sind 2 unterschiedliche Customer - Journeys und Advisor - Journeys zu beachten. Die Schnittstelle zwischen den beiden Journeys bildet die ChatBox mit der Funktionalität Kundenanfragen direkt in das Postfach des Beraters zu senden.

--> Advisor - Journey wird wie folgt abgebildet:

Registrierung und Anmeldung:
* Berater müssen sich registrieren und anmelden, um auf ihr Dashboard zugreifen zu können.
* Die Registrierung umfasst die Angabe persönlicher Daten, die Einrichtung eines Profils 
* Die Berater können sich mit ihren Anmeldedaten anmelden, um auf ihr Konto zuzugreifen.

Verwaltung des Dashboards:
* Nach der Anmeldung werden die Berater zu ihrem Dashboard weitergeleitet, wo sie ihr Profil und ihre Dienste verwalten können.
* Das Dashboard enthält Optionen zum Aktualisieren persönlicher Informationen, zum Ändern von Profilbildern und zum Ändern von Serviceangeboten.
* Berater können auch Kundenanfragen, die über die hinterlegte E-Mail-Adresse in ihrem externen Postfach einsehen. 

Profilanpassung:
* Berater können ihre Profile anpassen, um ihr Fachwissen zu präsentieren und potenzielle Kunden anzusprechen.
* Sie können detaillierte Beschreibungen hinzufügen, Bilder ihrer Arbeit hochladen und die von ihnen angebotenen Dienstleistungen angeben (z. B. Online, Vor Ort).
* Berater können auch ihre Verfügbarkeit und ihren Standort aktualisieren, um eine genaue Filterung auf der Seite advisors.html zu gewährleisten.
* Wichtig ist anzumerken: Die Filteroption ist derzeit statisch und bildet die auszuwählenden Attribute für alle Berater gleich ab. 
* Future Doing: Die Filteroption kann nur dynamisch angepasst werden, wenn das Dashboard für die Advisor ebenfalls individuell pro AdvisorID abgebildet werden kann, was zum Zeitpunkt der Entwicklung fehlt.

--> Die Schnittstelle ChatBox wird wie folgt abgebildet: 

* Wir haben für das Projekt dazu eine extra E-Mail-Adresse erstellt, die zugänglich ist. 
* User: tippitopp034@gmail.com
* Passwort: EuropeFootball2024
* Sollte das Passwort nicht funktionieren, bitte raslan.ebuheit@hotmail.de kontaktieren
* Wichtig ist anzumerken, dass zum derzeitigen Stand der Entwicklung alle Chatbox - Optionen, unabhängig vom Berater, die Nachrichten zu der gleichen E-Mail-Adresse senden
* Future Doing: Es fehlt an einem dynamischen Advisor Dashboard, die individuelle Profiländerungen speichern kann. Wir haben nur ein Advisor Dashboard, welches für die Frontend Ansicht verwendet wird. Aber es fehlt zum jetzigen Zeitpunkt ein Advisor Dashboard im Backend. 


--> Die User Journey wird wie folgt abgebildet:

Fehlendes Login
* Der Kunde braucht sich auf der Webseite nicht zu registrieren und braucht daher auch kein Kundenprofil zu hinterlegen
* Unter advidor.html hat der Kunde die Möglichkeit seine Auswahl an Beratern zu treffen.

Kunden - Kommunikation
* Sobald der Kunde einen Berater ausgesucht hat, kann er über den Kontakt - Button seine Anfrage versenden
* Es öffnet sich ein neues Popup - Fenster auf der gleichen Seite und der Kunde kann in einem Textfeld seine Nachrichten verfassen und über die Schnittstelle der ChatBox Funktionalität die Anfrage auf die E-Mail-Adresse des Beraters senden

Vertragsabwicklung:
* Wenn ein Kunde beschließt, eine Dienstleistung in Anspruch zu nehmen, leitet der Berater ihn zur Seite payment.html weiter.
* Das Dashboard kann einen Bereich zur Verfolgung abgeschlossener Verträge und zur Verwaltung laufender Aufträge enthalten.