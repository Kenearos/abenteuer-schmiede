---
skillId: bmad-as-szenen-balancer
skillName: Szenen-Balancer
skillType: workflow
description: |
  Analysiert Pacing, Begegnungsverteilung und Spielertypen-Abdeckung
  des Abenteuers. Prüft ob verschiedene Heldentypen genug Spotlights
  bekommen und ob der Spannungsbogen funktioniert.
---

# Szenen-Balancer

Dieser Workflow analysiert das gesamte Abenteuer auf Balance und Pacing.

## Ablauf

### Schritt 1: Daten sammeln

Lade alle Dateien:
- Alle Szenen aus `kompendium/szenen/`
- Alle Begegnungen aus `kompendium/begegnungen/`
- `zustand/aktuell.md`

### Schritt 2: Begegnungstyp-Verteilung

Zähle und visualisiere die Begegnungstypen:

```
Typ-Verteilung:
Kampf       ████████░░░░░░░░  35%
Sozial      ██████░░░░░░░░░░  25%
Erkundung   ████░░░░░░░░░░░░  20%
Ermittlung  ███░░░░░░░░░░░░░  15%
Dramatisch  █░░░░░░░░░░░░░░░   5%
```

**Ideal-Verteilung** (empfohlen):
- Kampf: 20-30%
- Sozial: 25-35%
- Erkundung: 15-25%
- Ermittlung: 10-20%
- Dramatisch/Atmosphärisch: 5-15%

### Schritt 3: Spielertypen-Analyse

Prüfe ob verschiedene Heldentypen glänzen können:

| Heldentyp | Spotlight-Szenen | Anteil | Bewertung |
|-----------|-----------------|--------|-----------|
| Kämpfer | [Szenen-Nummern] | X% | ✅/⚠️/❌ |
| Magier | [Szenen-Nummern] | X% | ✅/⚠️/❌ |
| Geweihter | [Szenen-Nummern] | X% | ✅/⚠️/❌ |
| Gesellschaftler | [Szenen-Nummern] | X% | ✅/⚠️/❌ |
| Streuner | [Szenen-Nummern] | X% | ✅/⚠️/❌ |
| Waldläufer | [Szenen-Nummern] | X% | ✅/⚠️/❌ |
| Gelehrter | [Szenen-Nummern] | X% | ✅/⚠️/❌ |

### Schritt 4: Spannungsbogen-Check

Analysiere den Spannungsverlauf über alle Szenen:

```
Spannung  ▲
Hoch      █         ██       ████
Mittel    ██       █  ██    █    █
Niedrig   █ ██   ██    ██ ██     ██
Ruhig     █   ███        █         ██
          ▼──────────────────────────▶
          Akt I    | Akt II  | Akt III
```

Prüfe:
- Steigt die Spannung insgesamt?
- Gibt es Durchhänger (>2 ruhige Szenen hintereinander)?
- Gibt es einen klaren Midpoint und Klimax?
- Gibt es Verschnaufpausen nach intensiven Szenen?

### Schritt 5: Schwierigkeits-Kurve

Prüfe ob die Schwierigkeit angemessen steigt:

| Akt | Durchschnittliche Probenschwierigkeit | Kampf-Schwierigkeit |
|-----|--------------------------------------|---------------------|
| I | [Modifikator-Schnitt] | [Leicht/Mittel] |
| II | [Modifikator-Schnitt] | [Mittel/Schwer] |
| III | [Modifikator-Schnitt] | [Schwer/Boss] |

### Schritt 6: Wahlfreiheits-Check

Prüfe ob Spieler echte Entscheidungen treffen:

| Szene | Lösungswege | Verzweigungen | Bewertung |
|-------|-------------|---------------|-----------|
| ... | [Anzahl] | [Ja/Nein] | ✅/⚠️/❌ |

**Warnung bei**: Szenen mit nur einem Lösungsweg, fehlende Misserfolgs-Pfade

### Schritt 7: Report erstellen

Erstelle den vollständigen Balance-Report mit:
1. Zusammenfassung (1-3 Sätze)
2. Stärken des Abenteuers
3. Probleme (sortiert nach Schwere)
4. Konkrete Verbesserungsvorschläge
5. Gesamtbewertung

<HALT>
Zeige dem Nutzer den Report und warte auf Entscheidung: "Soll ich die vorgeschlagenen Verbesserungen umsetzen?"
</HALT>
