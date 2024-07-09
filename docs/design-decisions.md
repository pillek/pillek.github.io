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

## 01: [Kein User Login nötig - Raslan]

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: 09-07-2024

### Problem statement

Unsere Applikation soll bei der User Journey keine Login Funktionalität für den User zur Verfügung stellen. Damit wollen wir 2 Effekte erzielen: A. Wir sparen uns die Zeit und können die vorhandenenen Ressourcen in die Entwicklung anderer Funktionalitäten stecken B. Wir geben unserem Produkt ein cooles Feature, aber auch dem User die Möglichkeit das Produkt ohne großen Aufwand auszuprobieren.  

### Decision

Daher haben wir uns in gemeinsamer Ansprache dazu entschieden eine ChatBox Funktionalität hinter jedem Berater - Profil zu hinterlegen, womit der User ganz einfach interagieren soll. Nach dem wir gemeinsam die Chatbox Funktionalität grob umfasst haben, ging es für mich in die eigentliche Entwicklung. 

Ich wollte, dass der User, nachdem er auf den Kontakt - Button im Advisor Profil geklickt hat, ein neues Popup Fenster sieht, wo der User folgende Felder ausfüllen kann: Betreff, Email und das Nachrichtenfeld mit dem jeweiligen Inhalt. Sobald der User auf "Senden" klickt, soll die Nachricht auf die jeweilige Email - Adresse des Beraters gesendet werden.

### Regarded options

Um die ChatBox Funktionalität abzubilden gab es dazu 2 Optionen:

A. JavaScript: Mit JS war es mir möglich gewesen die gewünschte Popup Funktionalität erfolgreich umzusetzen. Dazu musste zuerst eine Fetch - API von Flask im index.html eimgefügt werden, damti eine HTTP - Anfrage an einen Server gesendet werden kann. Nachdem diese dann stand, musste die Popup Funktionalität des Öffnens und des Schließens integriert werden.

B. Python: Wird ein Standard Code verwendet um eine POST Anfrage an die hinterlegte Email Adresse zu senden.

Zum jetzigen Stand der Entwicklung ist nur eine Email - Adresse für alle Berater verwendet. Das nächste Schritte wäre eventuell für jeden Berater eine individuelle POST - Anfrage zu machen. Je nach Stand der Entwicklung wird es versucht umzusetzen. 

---
