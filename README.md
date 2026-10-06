# M365 Access Review Analyzer

Ein CSV-basierter Python-Prototyp zur Erkennung potenzieller Identitäts- und Berechtigungsrisiken in einer simulierten Microsoft-365-Umgebung.

Die Anwendung lädt synthetische Benutzer-, Ressourcen- und Berechtigungsdaten, wendet definierte IAM-Prüfregeln an und exportiert die Ergebnisse in einen strukturierten Excel-Bericht.

## Funktionen

Der Analyzer erkennt aktuell:

- ausstehende Gasteinladungen, die älter als 30 Tage sind,
- Ressourcen mit unterbrochener Berechtigungsvererbung ohne dokumentierte Begründung,
- direkte Berechtigungen deaktivierter Benutzerkonten.

Der Grenzwert für ausstehende Einladungen kann über die Analysefunktion angepasst werden. Bei der Berichtserstellung wird das aktuelle Datum verwendet.

## Verwendete Technologien

- Python
- Pandas
- OpenPyXL
- Git und GitHub

## Projektstruktur

```text
m365-access-review-analyzer/
├── data/
│   ├── users.csv
│   ├── resources.csv
│   └── permissions.csv
├── output/
│   └── .gitkeep
├── src/
│   ├── analyzer.py
│   ├── data_loader.py
│   └── report_generator.py
├── .gitignore
├── README.md
└── requirements.txt
```

- `data_loader.py` lädt die CSV-Dateien und prüft, ob alle erforderlichen Spalten vorhanden sind.
- `analyzer.py` enthält die fachlichen IAM-Prüfregeln und steuert die Analyse.
- `report_generator.py` erstellt und formatiert den Excel-Bericht.
- `data/` enthält die synthetischen Eingabedaten.
- `output/` enthält lokal erzeugte Berichte, die nicht versioniert werden.

## Installation

Repository klonen:

```bash
git clone https://github.com/zufarRey/m365-access-review-analyzer.git
cd m365-access-review-analyzer
```

Virtuelle Python-Umgebung erstellen und aktivieren:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Unter Windows:

```powershell
.\.venv\Scripts\activate
```

Benötigte Pakete installieren:

```bash
python -m pip install -r requirements.txt
```

## Ausführung

Den Analyzer aus dem Projekt-Hauptordner starten:

```bash
python -m src.analyzer
```

Der erzeugte Bericht wird hier gespeichert:

```text
output/access_review_report.xlsx
```

## Excel-Bericht

Der Bericht enthält drei Tabellenblätter:

- `Stale Guest Invitations`
- `Broken Inheritance`
- `Disabled User Access`

Jedes Tabellenblatt verfügt über Filter, eine fixierte Kopfzeile und automatisch angepasste Spaltenbreiten.

## Synthetische Daten

Alle in diesem Repository enthaltenen Benutzer, Ressourcen, Berechtigungen, Namen und Kennungen sind fiktiv und wurden ausschließlich zu Demonstrationszwecken erstellt.

Das Projekt enthält keine Daten aus einem realen Microsoft-365-Tenant oder Unternehmen.

## Einschränkungen

Die aktuelle Version verarbeitet lokale CSV-Dateien und besitzt keine direkte Anbindung an Microsoft Entra ID, Microsoft Graph oder SharePoint Online.

Das Projekt dient als Lern- und Referenzprojekt zur Demonstration von Python-basierter Datenverarbeitung und IAM-bezogener Analyselogik.

## Geplante Erweiterungen

- automatisierte Tests mit Pytest,
- konfigurierbare Prüfregeln und Grenzwerte,
- Unterstützung von Microsoft Graph oder exportierten Entra-ID-Daten,
- weitere Prüfungen für Identitäten und Berechtigungen,
- Risikostufen und zusammengefasste Kennzahlen im Bericht.