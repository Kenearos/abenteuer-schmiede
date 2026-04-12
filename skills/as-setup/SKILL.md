---
skillId: bmad-as-setup
skillName: Abenteuer-Schmiede Setup
skillType: workflow
description: |
  Setup-Workflow für ein neues Abenteuer-Projekt. Erstellt die Projektstruktur,
  definiert den Rahmen und bereitet alles für die Entwicklung vor.
---

# Abenteuer-Schmiede Setup

Dieser Workflow richtet ein neues Abenteuer-Projekt ein.

## Ablauf

### Schritt 1: Projektname und Grundeinstellungen

Frage den Nutzer nach:
1. **Abenteuer-Name**: Wie soll das Abenteuer heißen?
2. **Region**: Wo in Aventurien spielt es?
3. **Epoche**: Wann spielt es? (z.B. 1040 BF)
4. **Abenteuer-Typ**: Ermittlung, Intrige, Reise, Dungeon, etc.
5. **Spieleranzahl**: Für wie viele Helden?
6. **Erfahrungsstufe**: Wie erfahren sind die Helden?
7. **Geschätzte Dauer**: One-Shot bis Kampagne?
8. **Sprache**: Deutsch oder English?

### Schritt 2: Rahmen erstellen

Erstelle die Rahmen-Dateien:

#### `rahmen/setting.md`
```markdown
# Setting: [Region]

## Geographie
<!-- Landschaft, Klima, wichtige Orte -->

## Kultur
<!-- Vorherrschende Kulturen, Sitten, Götterverehrung -->

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
- Nie die Reaktion der Helden vorwegnehmen

## Verbotene Klischees
<!-- Was wollen wir NICHT? Generisches Fantasy? Tolkien-Kopien? -->
```

#### `rahmen/regeln.md`
```markdown
# Regelwerk-Einstellungen

## Basis
- **Regelwerk**: DSA5
- **Erfahrungsstufe**: [AP-Bereich]
- **Optionalregeln**: [Welche verwenden?]

## Hausregeln
<!-- Abweichungen vom Standardregelwerk -->

## Proben-Philosophie
- Kritische Proben (Story-relevant): Eher leichter (0 bis +2)
- Bonus-Proben (Extra-Info): Normal bis schwer (0 bis -3)
- Heldentaten: Schwer bis meisterlich (-3 bis -7)

## Kampf-Einstellungen
- **Trefferzonen**: [Ja/Nein]
- **Wundschwellen**: [Ja/Nein]
- **Vereinfachter Kampf**: [Für Nebenbegegnungen?]

## Magie-Einstellungen
- **Verbreitung**: [Wie häufig ist Magie in der Region?]
- **Antimagie**: [Gibt es Antimagie-Elemente?]
```

### Schritt 3: Zustand initialisieren

Erstelle `zustand/aktuell.md` mit den Projektdaten.

### Schritt 4: Bestätigung

Zeige dem Nutzer die erstellte Struktur und frage:
"Alles korrekt? Sollen wir mit dem Abenteuer-Konzept beim Spielleiter starten?"

<HALT>
Warte auf Nutzereingabe.
</HALT>
