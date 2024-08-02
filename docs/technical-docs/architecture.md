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



<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Overview

Die app.py Datei erstellt die Flask-App und sorgt dafür, dass wenn ein Benutzer eine Anfrage an die App stellt, die Anfrage über die Routen weiterverarbeitet wird.
Die database.py Datei stellt die Verbindung zur Datenbank her und sorgt dafür, dass die App auf die Daten zugreifen kann. Diese Datei wird in app.py importiert, um die Datenbankverbindung zu initialisieren.

Die SQL-Skripte im Ordner sql werden verwendet, um die Datenbanktabellen zu erstellen und zu verwalten. Diese Skripte werden normalerweise einmalig ausgeführt, um die Datenbankstruktur zu definieren.

Die forms.py Datei definiert die Formulare, die in der App verwendet werden. Wenn ein Benutzer ein Formular ausfüllt und absendet, wird die Anfrage an eine View-Funktion weitergeleitet, die das entsprechende Formular aus forms.py importiert und verarbeitet.

Die Modelle im Ordner models repräsentieren die Datenbanktabellen. Wenn eine View-Funktion Daten aus der Datenbank abfragen oder speichern muss, verwendet sie diese Modelle, um die entsprechenden Datenbankoperationen durchzuführen.

Die View-Funktionen im Ordner views verarbeiten die Anfragen der Benutzer, interagieren mit den Modellen und rendern die entsprechenden Templates. Diese Templates befinden sich im Ordner templates und enthalten die HTML-Dateien, die als Vorlagen für die Darstellung der Benutzeroberfläche dienen. Jinja2 wird oft verwendet, um dynamische Inhalte in den HTML-Dateien zu rendern.

Zusammengefasst: Wenn ein Benutzer eine Anfrage stellt, wird diese von app.py an die entsprechende View-Funktion weitergeleitet. Die View-Funktion verarbeitet die Anfrage, interagiert mit den Modellen, um Daten aus der Datenbank abzurufen oder zu speichern, und rendert schließlich ein Template, das dem Benutzer angezeigt wird. Die Formulare aus forms.py werden verwendet, um Benutzereingaben zu validieren und zu verarbeiten, während database.py die Verbindung zur Datenbank sicherstellt.


## User Flow
![User Flow](..\assets\images\userflow.jpg)




[Data Model](https://pillek.github.io/technical-docs/data-model.html){: .btn .btn-purple }

