---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
[Philipp Kreis/Raslan Ebuheit]

{: .label .label-red }
[work in progress]

{: .no_toc }
# Architecture


## Overview

Die app.py Datei erstellt die Flask-App und sorgt dafür, dass wenn ein Benutzer eine Anfrage an die App stellt, die Anfrage über die Routen weiterverarbeitet wird.

Die database.py Datei stellt die Verbindung zur Datenbank her und sorgt dafür, dass die App auf die Daten zugreifen kann. Diese Datei wird in app.py importiert, um die Datenbankverbindung zu initialisieren.

Die forms.py Datei definiert die Formulare, die in der App verwendet werden. Wenn ein Benutzer ein Formular ausfüllt und absendet, wird die Anfrage weitergeleitet.

Die Modelle im Ordner models repräsentieren die Datenbanktabellen. Wenn eine Funktion Daten aus der Datenbank abfragen oder speichern muss, verwendet sie diese Modelle.

Die Templates im Ordner templates enthalten die HTML-Dateien, die als Vorlagen für das Darstellen der Benutzeroberfläche dienen. 



## User Flow
![User Flow](..\assets\images\userflow.jpg)




[Data Model](https://pillek.github.io/technical-docs/data-model.html){: .btn .btn-purple }

