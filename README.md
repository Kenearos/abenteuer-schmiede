# Abenteuer-Schmiede

**BMAD-Modul für KI-gestützte Pen-&-Paper-Abenteuer**

Schreibe Pen-&-Paper-Abenteuer mit einem Team spezialisierter KI-Agenten — vom Hook bis zum fertigen Abenteuerband. Systemunabhängig: DSA5, D&D 5e, Pathfinder, Shadowrun und mehr. Mit **Autorenrunde** für Team-Reviews!

## Was ist das?

Abenteuer-Schmiede ist ein [BMAD](https://github.com/bmadcode/BMAD-METHOD)-Modul, das den Prozess der Abenteuer-Erstellung in spezialisierte Rollen aufteilt. Statt alles alleine zu machen, arbeiten 6 Agenten zusammen:

| Agent | Rolle | Was er tut |
|-------|-------|-----------|
| **Spielleiter** (Meister Kronos) | Abenteuer-Architekt | Akte, Szenen, Spannungsbögen, Hooks |
| **Weltenbauer** (Cartograph) | Geographin | Schauplätze, Regionen, Atmosphäre |
| **NSC-Schmied** (Persona) | Menschenkennerin | NSCs mit Werten, Motivation, Stimme |
| **Begegnungsdesigner** (Strategos) | Taktiker | Kampf, Sozial, Erkundung — balanciert |
| **Regelwächter** (Codex) | Regelwerk-Experte | Werte, Proben, Regelkonsistenz |
| **Handout-Künstler** (Illumina) | Kalligraphin | Briefe, Rätsel, In-World-Texte |

Im **Partymodus** kommen alle Agenten als Autorenrunde zusammen und besprechen das Abenteuer gemeinsam.

## Features

- **Kompendium-System**: Single Source of Truth für NSCs, Orte, Szenen, Begegnungen
- **Systemunabhängig**: Unterstützt DSA5, D&D 5e, Pathfinder, Shadowrun und weitere Systeme
- **Drei-Akt-Struktur** mit flexiblen Fixpunkten und Freiheitsräumen
- **Partymodus**: Autorenrunde — alle Agenten reviewen und diskutieren dein Abenteuer
- **Balance-Analyse**: Automatische Prüfung von Pacing, Spielertypen-Abdeckung
- **Regelcheck**: Validierung aller Werte und Probenschwierigkeiten
- **Handout-Werkstatt**: Atmosphärische Briefe, Rätsel und Dokumente
- **Export**: Markdown, Druckformat, VTT-kompatibel
- **Wiederverwendbar**: Nutze die Schmiede für jedes neue Abenteuer

> **Spieltest gesucht?** Der [PnP-Simulator](https://github.com/Kenearos/pnp-simulator) simuliert dein Abenteuer mit KI-Spielern — exportiere aus der Schmiede, importiere in den Simulator.

## Installation

Voraussetzung: Ein Projekt mit [BMAD-METHOD](https://github.com/bmadcode/BMAD-METHOD) Setup.

```bash
# In einem bestehenden BMAD-Projekt:
npx bmad-method install
# → Wähle "Abenteuer-Schmiede" aus der Modulliste
```

Nach der Installation stehen alle Agenten und Workflows über die BMAD-Kommandos zur Verfügung.

## Modulstruktur

```
abenteuer-schmiede/
├── module.yaml               # BMAD-Modul-Definition
├── agents/                   # Agent-Personas (YAML)
│   ├── spielleiter.agent.yaml
│   ├── weltenbauer.agent.yaml
│   ├── nsc-schmied.agent.yaml
│   ├── begegnungsdesigner.agent.yaml
│   ├── regelwaechter.agent.yaml
│   └── handout-kuenstler.agent.yaml
├── skills/                   # BMAD-Skills
│   ├── as-setup/             # Projekt-Setup
│   ├── spielleiter/          # Abenteuerstruktur
│   ├── weltenbauer/          # Schauplätze
│   ├── nsc-schmied/          # NSC-Erstellung
│   ├── begegnungsdesigner/   # Begegnungen
│   ├── regelwaechter/        # Regelcheck
│   ├── handout-kuenstler/    # Handouts
│   ├── partymodus/           # Autorenrunde (Team-Diskussion)
│   ├── szenen-balancer/      # Balance-Analyse
│   └── abenteuer-export/     # Export
├── rahmen/                   # Abenteuer-Rahmen (pro Projekt befüllt)
│   ├── system.md             # Spielsystem-Definition (Attribute, Würfel, Mechaniken)
│   ├── setting.md            # Spielwelt, Region, Epoche, Kultur
│   ├── stil.md               # Erzählstil, Atmosphäre
│   └── regeln.md             # Hausregeln + Einstellungen
├── kompendium/               # Single Source of Truth (pro Projekt befüllt)
│   ├── nsc/                  # Alle NSCs mit Werten
│   ├── orte/                 # Alle Schauplätze
│   ├── szenen/               # Alle Szenen
│   ├── begegnungen/          # Alle Begegnungen
│   └── handouts/             # Spieler-Handouts
├── zustand/                  # State-Management
│   └── aktuell.md            # Globaler Fortschritt
└── _bmad-output/             # Generierte Dateien
```

## Workflow

```
1. Setup       → Spielsystem wählen, Rahmen definieren
2. Konzept     → Hook, Prämisse, Akt-Struktur
3. Welt        → Schauplätze ausarbeiten
4. NSCs        → Alle wichtigen NSCs mit Werten erstellen
5. Szenen      → Szene für Szene ausarbeiten (inkl. Begegnungen)
6. Handouts    → Briefe, Rätsel, Dokumente erstellen
7. Regelcheck  → Alle Werte, Proben, Schwierigkeiten prüfen
8. Balancing   → Pacing und Balance analysieren
9. Team-Review → Autorenrunde — alle Agenten reviewen gemeinsam
10. Export     → Fertiges Abenteuer exportieren
```

Jeder Schritt ist ein **Gate** — du entscheidest ob es weitergeht.

## Partymodus (Autorenrunde)

Alle Agenten kommen als Team zusammen und besprechen dein Abenteuer:

- **Brainstorming** — Ideen gemeinsam spinnen
- **Review** — Jeder Agent prüft aus seiner Perspektive
- **Szenen-Workshop** — Eine Szene von allen Seiten durchdenken
- **Konflikte lösen** — Wenn Atmosphäre und Regelbalance kollidieren

## Spielsystem-Hinweis

Die Abenteuer-Schmiede ist systemunabhängig und unterstützt beliebige Pen-&-Paper-Regelwerke. Das System wird beim Setup in `rahmen/system.md` definiert. Erwähnte Spielsysteme (DSA, D&D, Pathfinder, Shadowrun, etc.) sind Marken ihrer jeweiligen Rechteinhaber. Dieses Projekt steht in keiner Verbindung zu diesen Unternehmen.

## Contributing

Pull Requests willkommen! Besonders gesucht:

- System-Vorlagen für `rahmen/system.md` (DSA5, D&D 5e, Pathfinder, etc.)
- Setting-Pakete für verschiedene Spielwelten
- Zufallstabellen (NSCs, Begegnungen, Schätze)
- Verbesserungen am Regelwächter
- VTT-Integration (Foundry, Roll20)

## Lizenz

MIT — Mach damit was du willst.

---

Gebaut mit Würfeln und KI von [Kenearos](https://github.com/Kenearos)
