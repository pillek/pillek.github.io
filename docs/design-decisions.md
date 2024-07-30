---
title: Design Decisions
nav_order: 3
---

{: .label }
[Philipp Kreis/Raslan Ebuheit]

{: .label .label-red }
[work in progress]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Title]

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## [Example, delete this section] 01: How to access the database - SQL or SQLAlchemy 

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-Jun-2024

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

Our web application is written in Python with Flask and connects to an SQLite database. To complete the current project, this setup is sufficient.

We intend to scale up the application later on, since we see substantial business value in it.



Therefore, we will likely:
Therefore, we will likely:
Therefore, we will likely:

+ Change the database schema multiple times along the way, and
+ Switch to a more capable database system at some point.

### Decision

We stick with plain SQL.

Our team still has to come to grips with various technologies new to us, like Python and CSS. Adding another element to our stack will slow us down at the moment.

Also, it is likely we will completely re-write the app after MVP validation. This will create the opportunity to revise tech choices in roughly 4-6 months from now.
*Decision was taken by:* github.com/joe, github.com/jane, github.com/maxi

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ We know how to write SQL | ❌ We must learn ORM concept & SQLAlchemy |
| **Change DB schema** | ❌ SQL scattered across code | ❔ Good: classes, bad: need Alembic on top |
| **Switch DB engine** | ❌ Different SQL dialect | ✔️ Abstracts away DB engine |

---

## 01: Wie soll der User Journey sein, bzw. was bräuchten wir minimal?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 09-07-2024

### Problem statement

Unsere Anwendung soll einen kleinen und funktionalen User Journey bieten, die es den Nutzern ermöglicht, ihre Ziele schnell zu erreichen. Wir müssen entscheiden, wie dieser Journey aussehen soll und welche minimalen Schritte erforderlich sind.

### Decision

-> Homepage
	Button für “Berater ansehen”
->Beraterübersicht (von allem) 
	Mehrere Berater in Reihen mit Bildern
	unter jedem Berater dessen Präferenzen
	unter jedem Berater ein Button mit Kontakt
-> ChatBox evtl. im gleichen Fenster (erstmal ohne Login)
	User gibt Nachricht in die Eingabe ein, welche automatisch an Mail von Consultant versendet wird

### Regarded options

- Längerer User Journey: Eine umfassendere Erfahrung mit zusätzlichen Schritten (z. B. Login).
Pro: Bietet umfassendere Funktionen.
Con: Kann komplex sein und die Entwicklungszeit verlängern.
- Minimaler User Journey: Eine reduzierte Version mit nur den grundlegenden Schritten.
Pro: Einfach und schnell zu ein Produkt zu haben.
Con: Begrenzte Funktionalität und möglicherweise weniger attraktiv für Benutzer.

---

## 02: Welchen Advisor Journey brauchen wir für den geforderten User Journey?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 09-07-2024

### Problem statement

Unsere Aufgabe besteht darin, den passenden Advisor Journey für den geforderten User Journey zu definieren. Dabei müssen wir nun die signifikanten Anforderungen und den Kontext berücksichtigen.

### Decision

-> Registrierung auf Loginseite mit
	E-Mail
	Passwort
	
-> Dashboard von Consultant
Name angeben
Über mich
Meine Stylings (Bilder)
Meine Services
	preferences angeben
	biography angeben
	(Bild angeben)
	(der Consultant sieht seine Aufträge im Dashboard und kann alte dort löschen)

-> Login vom Consultant auf Homepage in NavBar	

### Regarded options

Andere Möglichkeiten sich als Berater in seinem Dashboard zu beschreiben

---

## 03: Braucht der normale Kunde einen Login?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 09-07-2024

### Problem statement

Uns hat sich die Frage gestellt, ob der normale Kunde einen Login benötigt. Hierbei müssen wir die Anforderungen des Kontakts zwischen Kunde und Berater berücksichtigen.

### Decision

Nach etwas Abwägung haben wir uns dafür entschieden, den Login des normalen Kunden wegzulassen und den Messenger nicht über unser System zu entwickeln. Deswegen werden wir ein einfaches Formularfeld implementieren, die die nötige Eingabe enthält und die komplette Kommunikation über E-Mail laufen lässt. JavaScript ermöglicht das Pop-up und das Versenden macht Python möglich.


### Regarded options

Gastzugang ohne Login:
Pro: Einfache und schnelle Bestellabwicklung.
Pro: Ermöglicht ein schnelleres minimales Softwareprodukt.
Con: Begrenzter Komfort im Erlebnis des Kunden.

Login erforderlich:
Pro: Bietet ein besseres Erlebnis und ermöglicht die Speicherung von Kundendaten.
Con: Kann Benutzer abschrecken, die keine zusätzlichen Konten erstellen möchten.
Con: Erhöht den Aufwand für die Entwicklung.

--- 

## 04: Nehmen wir CSS oder nehmen wir Bootstrap?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 09-07-2024

### Problem statement

Bei der Wahl der Formatierung für unser Webprojekt müssen wir die Vor- und Nachteile von CSS und Bootstrap abwägen. Hierbei geht es darum, die beste Lösung für unsere spezifischen Anforderungen zu finden.

### Decision

Wir haben uns erst einmal für CSS entschieden, wir dort von vornherein Wissen haben.

### Regarded options

CSS (Cascading Style Sheets):
Pro: Schon vorhandenes Wissen.
Con: Erfordert mehr Aufwand.
Con: Keine vorgefertigten Komponenten.
Bootstrap:
Pro: Vorgefertigte Komponenten und Stile für schnellere Entwicklung.
Pro: Responsives Design und gute Unterstützung für verschiedene Geräte.
Con: Weniger Vorwissen.

---

## 05: Welche Anforderungen haben wir an die Datenbank und welche Datenbank passt dazu?

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: 09-07-2024

### Problem statement

Wir müssen alles vom Advisor (Login Daten, Profildaten, Bilder, Payment) von mehreren Advisorn speichern.

### Decision

Wir bauen eine SQLAlchemy Datenbank mit den Tabellen: User, Login,...

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## 06: [Kein User Login nötig - Raslan]

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: 09-07-2024

### Problem statement

Unsere Applikation soll bei der User Journey keine Login Funktionalität für den User zur Verfügung stellen. Damit wollen wir 2 Effekte erzielen: A. Wir sparen uns die Zeit und können die vorhandenenen Ressourcen in die Entwicklung anderer Funktionalitäten stecken B. Wir geben unserem Produkt ein cooles Feature, aber auch dem User die Möglichkeit das Produkt ohne großen Aufwand auszuprobieren.  

### Decision

Daher haben wir uns in gemeinsamer Absprache dazu entschieden, eine ChatBox Funktionalität hinter jedem Berater - Profil zu hinterlegen, womit der User ganz einfach interagieren soll. Nach dem wir gemeinsam die Chatbox Funktionalität grob umfasst haben, ging es für mich in die eigentliche Entwicklung. 

Ich wollte, dass der User, nachdem er auf den Kontakt - Button im Advisor Profil geklickt hat, ein neues Popup Fenster sieht, wo der User folgende Felder ausfüllen kann: Betreff, Email und das Nachrichtenfeld mit dem jeweiligen Inhalt. Sobald der User auf "Senden" klickt, soll die Nachricht auf die jeweilige Email - Adresse des Beraters gesendet werden.

### Regarded options

Um die ChatBox Funktionalität abzubilden gab es dazu 2 Optionen:

A. JavaScript: Mit JS war es mir möglich gewesen die gewünschte Popup Funktionalität erfolgreich umzusetzen. Dazu musste zuerst eine Fetch - API von Flask im index.html eimgefügt werden, damti eine HTTP - Anfrage an einen Server gesendet werden kann. Nachdem diese dann stand, musste die Popup Funktionalität des Öffnens und des Schließens integriert werden.

B. Python: Wird ein Standard Code verwendet um eine POST Anfrage an die hinterlegte Email Adresse zu senden.

Zum jetzigen Stand der Entwicklung ist nur eine Email - Adresse für alle Berater verwendet. Das nächste Schritte wäre eventuell für jeden Berater eine individuelle POST - Anfrage zu machen. Je nach Stand der Entwicklung wird es versucht umzusetzen. 

---
## 02: [Mail - API]

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 22-07-2024

### Problem Statement

Wir haben zwar eine Chatbox Funktionalität für alle Advisor Profile erstellt, aber das Problem war, dass die Mails nicht, wie gewünscht, in der hinterlegten Mail - Adresse ankamen. Ich hab dann versucht die Vertrauenswürdigkeit der Website - Mails in den Google Einstellungen anzupassen und hatte dabei keinen Erfolg gehabt.

### Decision

Die hinterlegte Email -Adresse von tippitopp034@gmail.com ist ein Google Provider und die gesendeten Mails von der Webseite haben das Problem, dass sie nicht als vertrauenswürdig eingestuft werden. Daher musste ich mir überlegen, wie einen anderen Provider als Zwischenbrücke nutzen könnte, der die richtige Reputation besitzt, damit die Nachrichten von der Webseite ankommen. Dazu wurde die API von Mailjet in die Webseite integriert, um die Vertrauenswürdigkeit der Mails zu erhöhen.  

Wichtig war dabei, dass die verwendete API primär funktioniert und sekundär keine zusätzlichen Kosten verursacht. Da das Basisprodukt von Mailjet 6000 Mails pro Monat kostenlos verarbeiten kann, fiel die entsprechende Entscheidung auf den besagten Provider.

--

## 02: Transaktionsabwicklung

### Meta

Status
: Done

Updated
: 22-07-2024

### Problem Statement

Das Ziel ist es, einen 3-stufigen Zahlungsprozess für eine Mode-Website zu erstellen. Die Schritte sind: Bestelldetails,
Zahlungsinformationen und Zahlungsbestätigung. Die Seite verarbeitet auch eine Anfrage, die den Payload zurück
an das Flask-Backend sendet.

### Decision

Die Design-Entscheidung war, einen 3-stufigen Zahlungsprozess mit klarer Navigation und Validierung bei jedem Schritt zu implementieren.Die Idee ist, den Prozess einfach, aber dennoch „code-komplex“ genug zu gestalten, um eine echte Zahlungsanforderung zu demonstrieren.
 
### Regarded options


Option 1: Modal-basiertes Zahlungsformular
Beschreibung: Ein modales Fenster, das über der aktuellen Seite erscheint und das Zahlungsformular enthält.

Vorteile:
Hält die Benutzer auf derselben Seite und reduziert die Komplexität der Navigation. Kann visuell ansprechend und modern sein.

Nachteile:
Begrenzter Platz für die Anzeige von Informationen, was möglicherweise prägnantere Formulare erfordert.
Potenzielle Probleme mit der Reaktionsfähigkeit und Zugänglichkeit von Mobilgeräten.
Komplexe Handhabung der Formularübermittlung und -validierung innerhalb eines Modals.

Option 2: Einseitiges Zahlungsformular
Beschreibung: Eine einzige Seite, die alle Felder für Bestelldetails, Zahlungsinformationen und Bestätigung enthält.

Vorteile:
Einfachheit in Design und Implementierung.
Alle Informationen sind auf einen Blick sichtbar.

Nachteile:
Kann aufgrund der Menge an Informationen auf einer Seite für die Benutzer überwältigend sein.
Höheres Risiko, dass Nutzer Felder übersehen oder falsch ausfüllen.
Weniger geführte Erfahrung, was zu höheren Abbruchraten führen kann.

---


## 01: Änderung Aufgabenverteilung eine Woche vor Ende

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 27.07.2024

### Problem statement

Eine Woche vor dem Abgabetermin des Projekts kam Philipp wegen eines Fehlercodes in der Datenbank und der allgemeinen Logik des Projekts, die er bis dahin entwickelt hatte, nicht weiter. Deswegen entschied er sich vollständige Neugestaltung der Datenbank in einem separaten Testprojekt, was zu einer erheblichen Verzögerung eine Woche vor Abgabe führte.
### Decision

Wir haben uns dann entschieden, die primäre Verantwortung für die Datenbank und die Logik des Projekts von Philipp auf Raslan zu übertragen. Während Philipp Raslan dabei hilft die Datenbank zu programmieren, kümmert sich Philipp eher  um die Dokumentation. Wir hoffen dadurch das Projekt trotz der unerwarteten Herausforderungen rechtzeitig abzuschließen.

### Regarded options

1. Philipp behebt den Fehler selbst: Dies hätte zu weiteren Verzögerungen führen können, da Philipp bereits Zeit mit der Fehlerbehebung verbracht hatte. Philipp steckt aber bereits tief im Thema.
2. Übertragung der Aufgabe: Raslan hat evtl. mehr Motivation und die Fähigkeiten, die Aufgabe zu übernehmen, während Philipp sich auf die Dokumentation konzentriert. Eine neue Person muss sich aber erst in die Materie einfinden.

---