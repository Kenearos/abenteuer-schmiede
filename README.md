# Abenteuer-Schmiede

**BMAD-Modul für KI-gestützte Pen-&-Paper-Abenteuer im DSA-Stil**

Schreibe DSA-Abenteuer mit einem Team spezialisierter KI-Agenten — vom Hook bis zum fertigen Abenteuerband. Inklusive interaktivem **Partymodus** zum Testen!

## Was ist das?

Abenteuer-Schmiede ist ein BMAD-kompatibles Modul, das den Prozess der Abenteuer-Erstellung in spezialisierte Rollen aufteilt. Statt alles alleine zu machen, arbeiten 7 Agenten zusammen:

| Agent | Rolle | Was er tut |
|-------|-------|-----------|
| **Spielleiter** (Meister Kronos) | Abenteuer-Architekt | Akte, Szenen, Spannungsbögen, Hooks |
| **Weltenbauer** (Cartograph) | Geographin | Schauplätze, Regionen, Atmosphäre |
| **NSC-Schmied** (Persona) | Menschenkennerin | NSCs mit Werten, Motivation, Stimme |
| **Begegnungsdesigner** (Strategos) | Taktiker | Kampf, Sozial, Erkundung — balanciert |
| **Regelwächter** (Codex) | DSA5-Experte | Werte, Proben, Regelkonsistenz |
| **Handout-Künstler** (Illumina) | Kalligraphin | Briefe, Rätsel, In-World-Texte |
| **Partymodus** (Spieltisch) | Virtueller SL | Spiele dein Abenteuer interaktiv durch! |

## Features

- **Kompendium-System**: Single Source of Truth für NSCs, Orte, Szenen, Begegnungen
- **DSA5-Native**: Proben, Qualitätsstufen, Kampfwerte, Zauber, Liturgien
- **Drei-Akt-Struktur** mit flexiblen Fixpunkten und Freiheitsräumen
- **Partymodus**: Teste dein Abenteuer bevor du es am echten Tisch spielst!
- **Balance-Analyse**: Automatische Prüfung von Pacing, Spielertypen-Abdeckung
- **Regelcheck**: Validierung aller Werte und Probenschwierigkeiten
- **Handout-Werkstatt**: Atmosphärische Briefe, Rätsel und Dokumente
- **Export**: Markdown, Druckformat, VTT-kompatibel
- **Wiederverwendbar**: Nutze die Schmiede für jedes neue Abenteuer

## Schnellstart

### Standalone (ohne BMAD)

```bash
git clone https://github.com/Kenearos/abenteuer-schmiede.git
cd abenteuer-schmiede
claude
```

Dann sage: **"Neues Abenteuer"** oder **"Hilfe"**

### Als BMAD-Modul

```bash
# In einem bestehenden BMAD-Projekt:
npx bmad-method install
# → Wähle "Abenteuer-Schmiede" aus der Modulliste
```

## Projektstruktur

```
abenteuer-schmiede/
├── CLAUDE.md                 # Orchestrator (Herzstück)
├── module.yaml               # BMAD-Modul-Definition
├── rahmen/                   # Abenteuer-Rahmen
│   ├── setting.md            # Region, Epoche, Kultur
│   ├── stil.md               # Erzählstil, Atmosphäre
│   └── regeln.md             # DSA5-Basis + Hausregeln
├── kompendium/               # Single Source of Truth
│   ├── nsc/                  # Alle NSCs mit Werten
│   ├── orte/                 # Alle Schauplätze
│   ├── szenen/               # Alle Szenen
│   ├── begegnungen/          # Alle Begegnungen
│   ├── handouts/             # Spieler-Handouts
│   └── figuren/              # Spielercharaktere (Partymodus)
├── zustand/                  # State-Management
│   ├── aktuell.md            # Globaler Fortschritt
│   └── szenen/               # Partymodus-Ergebnisse
├── skills/                   # BMAD-Skills
│   ├── as-setup/             # Projekt-Setup
│   ├── spielleiter/          # Abenteuerstruktur
│   ├── weltenbauer/          # Schauplätze
│   ├── nsc-schmied/          # NSC-Erstellung
│   ├── begegnungsdesigner/   # Begegnungen
│   ├── regelwaechter/        # Regelcheck
│   ├── handout-kuenstler/    # Handouts
│   ├── partymodus/           # Interaktiver Spieltest
│   ├── szenen-balancer/      # Balance-Analyse
│   └── abenteuer-export/     # Export
├── agents/                   # Agent-Definitionen
└── _bmad-output/             # Generierte Dateien
    ├── szenen/
    ├── handouts/
    └── export/
```

## Workflow

```
1. Setup        → Rahmen definieren (Region, Ton, Regeln)
2. Konzept      → Hook, Prämisse, Akt-Struktur
3. Welt         → Schauplätze ausarbeiten
4. NSCs         → Charaktere mit Werten erschaffen
5. Szenen       → Szene für Szene ausarbeiten
6. Begegnungen  → Kämpfe, Rätsel, soziale Konflikte
7. Handouts     → Briefe, Karten, Rätsel
8. Regelcheck   → Werte und Proben validieren
9. Balancing    → Pacing und Spielertypen prüfen
10. Partymodus  → Abenteuer durchspielen und testen!
11. Export      → Fertiges Abenteuer exportieren
```

Jeder Schritt ist ein **Gate** — du entscheidest ob es weitergeht.

## Partymodus

Das Highlight: Spiele dein Abenteuer interaktiv durch!

- Erstelle oder lade Spielercharaktere
- Claude übernimmt den Spielleiter
- Würfle Proben oder lass sie automatisch auflösen
- Entdecke Plotlöcher, Balance-Probleme und Sackgassen
- Erhalte einen detaillierten Testbericht

```
> Partymodus
🎲 Willkommen am Spieltisch! 
   Möchtest du vorgefertigte Helden oder eigene erstellen?
```

## Voraussetzungen

- Claude Code (empfohlen)
- Kein Python oder sonstige Dependencies nötig
- Optional: Foundry VTT / Roll20 für VTT-Export

## DSA-Hinweis

Dieses Modul nutzt die Regeln von **Das Schwarze Auge 5. Edition** als Basis. DSA und Das Schwarze Auge sind eingetragene Marken von Ulisses Spiele. Dieses Projekt ist ein inoffizielles Fan-Werkzeug und steht in keiner Verbindung zu Ulisses Spiele.

## Contributing

Pull Requests willkommen! Besonders gesucht:

- Vorgefertigte Helden-Templates für den Partymodus
- Regionale Setting-Pakete (Mittelreich, Thorwal, etc.)
- Zufallstabellen (NSCs, Begegnungen, Schätze)
- Verbesserungen am Regelwächter
- VTT-Integration (Foundry, Roll20)

## Lizenz

MIT — Mach damit was du willst.

---

Gebaut mit Würfeln und KI von [Kenearos](https://github.com/Kenearos)
