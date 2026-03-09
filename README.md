#Second Brain – Personal Knowledge Manager

Second Brain ist ein persönliches Wissensmanagement-Tool, das komplett über die Command Line (Terminal) gesteuert wird. Es ermöglicht dir, Gedanken, Notizen und Ideen effizient zu speichern, zu verknüpfen und zu durchsuchen. Ideal für Lernen, Projektideen, Journaling oder philosophische Notizen.

Features:

Notizenverwaltung: Speichere Ideen, Gedanken oder Konzepte mit Tags.

Automatische Verknüpfungen: Das System schlägt verwandte Notizen vor (AI-basiert).

Graphische Visualisierung: Sieh dein persönliches Wissensnetzwerk als Graph.

Schnelle Suche: Suche nach Titel, Inhalt oder Tags.

Daily Use: Perfekt für kontinuierliches Lernen und Journaling.

Tech Stack:

Python 3.10+

NetworkX + Matplotlib – Graph-Visualisierung

scikit-learn – AI-basiertes Verknüpfen von Notizen

JSON für lokale Speicherung

Installation:

Repo klonen:

git clone https://github.com/weafxy/SecodBrain.git
cd SecondBrain

Virtuelle Umgebung erstellen (optional, empfohlen):

python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Mac/Linux

Abhängigkeiten installieren:

pip install networkx matplotlib scikit-learn

Noch exestiert keine requirements datei, die kommt noch.


Nutzung:

Starten:

python main.py

Du siehst dann den Prompt:

brain>

Befehle:

help – Zeigt alle verfügbaren Befehle

add – Neue Notiz hinzufügen

list – Alle Notizen auflisten

search <Suchbegriff> – Notizen nach Titel oder Inhalt durchsuchen

suggest <Notiz-ID> – Semantisch ähnliche Notizen vorschlagen

graph – Zeigt dein Wissensnetzwerk grafisch

exit – CLI verlassen

Beispiele:

Notiz hinzufügen:

brain> add (enter)
Title: Python Tricks (enter)
Content: List Comprehensions, Dictionaries, kleine Projekte (enter)
Add tags? (y/n) y (enter)
Tags (comma separated): Programmierung, Python (enter)
Note added! ID: 123e4567-e89b-12d3-a456-426614174000

Alle Notizen auflisten:

brain> list (enter)
123e4567-e89b-12d3-a456-426614174000 - Python Tricks [Programmierung, Python] Links: 0

Notizen durchsuchen:

brain> search Python (enter)
123e4567-e89b-12d3-a456-426614174000 - Python Tricks [Programmierung, Python]

AI-Vorschläge für Verknüpfungen:

brain> suggest 123e4567-e89b-12d3-a456-426614174000 (enter)
Suggested links for 'Python Tricks':
- Lernmethoden (456e7890-12ab-34cd-5678-123456789abc)

Graph anzeigen:

brain> graph (enter)

Ein Fenster zeigt alle Notizen als Knoten und Verknüpfungen als Linien.

Hinweise:

notes.json enthält deine Notizen. Lege ein leeres Array [] an, wenn die Datei leer ist.

Alle Dateien (main.py, notes.py, storage.py, ai.py, graph.py) müssen im gleichen Ordner liegen.

Ordnernamen mit Leerzeichen vermeiden (z. B. SecondBrain statt Second Brain).

Lizenz:

MIT License – siehe LICENSE
