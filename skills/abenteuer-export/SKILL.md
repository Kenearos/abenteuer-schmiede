---
skillId: bmad-as-abenteuer-export
skillName: Abenteuer-Export
skillType: workflow
description: |
  Exportiert das fertige Abenteuer als zusammenhängendes Markdown-Dokument,
  druckfertiges Format oder VTT-kompatibles Format.
artifacts:
  output:
    - type: document
      path: _bmad-output/export/
---

# Abenteuer-Export

Dieser Workflow exportiert das Abenteuer in verschiedene Formate.

## Ablauf

### Schritt 1: Vollständigkeitsprüfung

Prüfe ob alle Elemente vorhanden sind:

- [ ] `rahmen/setting.md` — Setting definiert
- [ ] `rahmen/stil.md` — Stil definiert
- [ ] `kompendium/szenen/uebersicht.md` — Szenen-Übersicht vorhanden
- [ ] Mindestens 3 Szenen ausgearbeitet
- [ ] Alle referenzierten NSCs existieren in `kompendium/nsc/`
- [ ] Alle referenzierten Orte existieren in `kompendium/orte/`
- [ ] Mindestens 1 Begegnung pro Akt
- [ ] Einleitung/Hook vorhanden

Falls unvollständig: Zeige was fehlt und frage ob trotzdem exportiert werden soll.

### Schritt 2: Export-Format wählen

Frage den Nutzer:
- **Markdown** — Komplettes Abenteuer als eine .md Datei
- **Druckformat** — Strukturiert wie ein offizielles Abenteuer im Stil des gewählten Systems
- **VTT-Format** — Szenen-basiert für Foundry VTT / Roll20

### Schritt 3: Zusammenstellen

**Markdown-Export** (`_bmad-output/export/[abenteuer-name].md`):

```markdown
# [Abenteuer-Name]

> [Kurzbeschreibung in 2-3 Sätzen]

## Metadaten
- **Autor**: [Name]
- **Setting**: [Region, Epoche]
- **Spieleranzahl**: [X-Y]
- **Erfahrungsstufe**: [Stufe]
- **Geschätzte Spieldauer**: [Dauer]

---

## Einleitung
[Hook, Prämisse, Übersicht für den SL]

## Hintergrund
[Was ist wirklich passiert? Was wissen nur die SL-Leser?]

## Dramatis Personae
[Alle NSCs mit Kurzprofil und Seitenverweis]

## Schauplätze
[Alle Orte mit Kurzprofil und Seitenverweis]

---

## Akt I: [Titel]
### Szene 1: [Titel]
[Komplette Szene mit Vorlesetext, Ablauf, Proben, Übergängen]

### Szene 2: [Titel]
...

## Akt II: [Titel]
...

## Akt III: [Titel]
...

---

## Anhang

### NSC-Werte
[Vollständige Werteblöcke aller kampfrelevanten NSCs]

### Begegnungstabellen
[Zufallsbegegnungen und Encountertabellen]

### Handouts
[Alle Spieler-Handouts zum Ausdrucken]

### Karten
[Kartenbeschreibungen und ASCII-Karten]

### Belohnungen
[AP-Vergabe und Beutevorschläge]
```

**Druckformat** — Wie ein offizielles Abenteuer im Stil des gewählten Systems:

Selbe Struktur, aber:
- Vorlesetexte in Blockquotes
- SL-Informationen klar getrennt
- Seitenverweise als Anker
- Inhaltsverzeichnis am Anfang
- Druckfreundliche Formatierung

**VTT-Format** — Für Virtual Tabletop:

- Jede Szene als einzelne Datei
- NSC-Werte als importierbare Blöcke
- Handouts als separate Dateien
- Encounter-Maps als ASCII-Beschreibungen

### Schritt 4: Speichern

Speichere den Export in `_bmad-output/export/`:
- `[name].md` — Hauptdokument
- `[name]-handouts/` — Separate Handout-Dateien
- `[name]-nsc/` — Separate NSC-Werte

### Schritt 5: Zusammenfassung

Zeige dem Nutzer:
- Exportierte Dateien
- Seitenumfang
- Vollständigkeits-Status

<HALT>
Warte auf Nutzereingabe. Frage: "In welchem Format soll ich das Abenteuer exportieren? Markdown, Druckformat oder VTT?"
</HALT>
