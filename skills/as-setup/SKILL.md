---
skillId: bmad-as-setup
skillName: Abenteuer-Schmiede Setup
skillType: workflow
description: |
  Setup-Workflow für ein neues Abenteuer-Projekt. Erstellt die Projektstruktur,
  definiert Spielsystem und Rahmen, bereitet alles für die Entwicklung vor.
---

# Abenteuer-Schmiede Setup

Dieser Workflow richtet ein neues Abenteuer-Projekt ein.

## Ablauf

### Schritt 1: Spielsystem und Grundeinstellungen

Frage den Nutzer nach:
1. **Spielsystem**: Welches Regelwerk? (z.B. DSA5, D&D 5e, Pathfinder 2e, Shadowrun 6, Savage Worlds, eigenes System)
2. **Abenteuer-Name**: Wie soll das Abenteuer heißen?
3. **Spielwelt/Region**: Wo spielt das Abenteuer? (z.B. Aventurien/Mittelreich, Forgotten Realms/Sword Coast, Sixth World/Seattle)
4. **Epoche/Zeitraum**: Wann spielt es? (z.B. 1040 BF, DR 1492, 2080)
5. **Abenteuer-Typ**: Ermittlung, Intrige, Reise, Dungeon, etc.
6. **Spieleranzahl**: Für wie viele Helden/Charaktere?
7. **Erfahrungsstufe**: Wie erfahren sind die Charaktere? (Anfänger bis Meisterlich — Details gemäß System)
8. **Geschätzte Dauer**: One-Shot bis Kampagne?
9. **Sprache**: Deutsch oder English?

### Schritt 2: Rahmen erstellen

Erstelle die Rahmen-Dateien in dieser Reihenfolge:

#### `rahmen/system.md`

Befülle die Systemdefinition basierend auf dem gewählten Spielsystem. Nutze dein Wissen über das System um alle Sektionen auszufüllen:
- Kernattribute mit Abkürzungen
- Würfelsystem und Probenmechanik
- Schwierigkeitsskala
- Kampfsystem-Überblick
- Verfügbare Spezies/Herkünfte
- Charakterfortschritt
- Magie/Übernatürliches (falls vorhanden)
- Erfahrungsstufen-Referenz
- Wichtige Begriffe und Abkürzungen

#### `rahmen/setting.md`
```markdown
# Setting: [Region/Spielwelt]

## Geographie
<!-- Landschaft, Klima, wichtige Orte -->

## Kultur
<!-- Vorherrschende Kulturen, Sitten, Religion/Überzeugungen -->

## Politik
<!-- Herrschaftsstrukturen, Konflikte, Allianzen -->

## Aktuelles Zeitgeschehen
<!-- Was passiert gerade in dieser Region? (Epoche beachten) -->

## Stimmung
<!-- Grundstimmung: düster, abenteuerlich, politisch, mystisch -->

## Reisehinweise
<!-- Typische Gefahren, Entfernungen, Transportmittel -->
```

#### `rahmen/stil.md`
```markdown
# Erzählstil

## Grundeinstellungen
- **Perspektive**: Zweite Person Plural ("Ihr seht...")
- **Sprache**: [Deutsch/English]
- **Ton**: [Episch/Gritty/Humorvoll/Düster/etc.]

## Atmosphäre
<!-- Wie soll sich das Abenteuer anfühlen? Referenz-Werke? -->

## Vorlesetext-Regeln
- Maximal 5-7 Sätze
- Mindestens 3 Sinne ansprechen
- Immer ein interaktives Detail
- Nie die Reaktion der Charaktere vorwegnehmen

## Verbotene Klischees
<!-- Was wollen wir NICHT? -->
```

#### `rahmen/regeln.md`
```markdown
# Regelwerk-Einstellungen

## Basis
- **Spielsystem**: Siehe `rahmen/system.md`
- **Erfahrungsstufe**: [Stufe gemäß System]
- **Optionalregeln**: [Welche systemspezifischen Optionen verwenden?]

## Hausregeln
<!-- Abweichungen vom Standardregelwerk -->

## Proben-Philosophie
- Kritische Proben (Story-relevant): Eher leicht
- Bonus-Proben (Extra-Info): Normal bis schwer
- Heldentaten: Schwer bis meisterlich

## Kampf-Einstellungen
- **Kritische Treffer**: [Ja/Nein]
- **Vereinfachter Kampf**: [Für Nebenbegegnungen?]
- **Sonstige Optionen**: [Systemspezifische Kampfoptionen]

## Übernatürliches
- **Verbreitung**: [Wie häufig ist Magie/Übernatürliches in der Spielwelt?]
- **Einschränkungen**: [Gibt es besondere Regeln oder Verbote?]

## Belohnungen
- **Erfahrungspunkte pro Abend**: [Empfehlung gemäß System]
- **Beute-Richtlinie**: [Großzügig/Normal/Karg]
```

### Schritt 3: Zustand initialisieren

Erstelle `zustand/aktuell.md` mit den Projektdaten.

### Schritt 4: Bestätigung

Zeige dem Nutzer die erstellte Struktur und frage:
"Alles korrekt? Sollen wir mit dem Abenteuer-Konzept beim Spielleiter starten?"

<HALT>
Warte auf Nutzereingabe.
</HALT>
