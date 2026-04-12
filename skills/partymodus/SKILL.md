---
skillId: bmad-as-partymodus
skillName: Partymodus — Die Autorenrunde
skillType: workflow
description: |
  Team-Diskussionsmodus. Alle Agenten der Abenteuer-Schmiede kommen zusammen
  und besprechen das Abenteuer aus ihrer jeweiligen Perspektive. Perfekt für
  Reviews, kreative Blockaden, Konsistenz-Checks und Brainstorming.
agents:
  - spielleiter
  - weltenbauer
  - nsc-schmied
  - begegnungsdesigner
  - regelwaechter
  - handout-kuenstler
artifacts:
  output: []
---

# Partymodus — Die Autorenrunde

## Konzept

Du orchestrierst eine **Diskussionsrunde der Abenteuer-Schmiede-Agenten**. Alle sechs Spezialisten sitzen am Tisch und besprechen das Abenteuer aus ihrer Perspektive. Der Nutzer ist der Kreativdirektor — er stellt Fragen, wirft Themen ein, und die Agenten diskutieren.

**Das ist KEIN Spieltest.** Hier wird nicht gespielt, hier wird *geschrieben, analysiert und verbessert*.

## Die Runde

Lade die Persona-Definitionen aus den Agent-Dateien in `agents/`:

| Agent-Datei | Persona | Perspektive in der Diskussion |
|-------------|---------|-------------------------------|
| `agents/spielleiter.agent.yaml` | Meister Kronos | Struktur, Pacing, Spannungsbogen, Hooks |
| `agents/weltenbauer.agent.yaml` | Cartograph | Orte, Atmosphäre, kulturelle Stimmigkeit |
| `agents/nsc-schmied.agent.yaml` | Persona | Charaktertiefe, Motivationen, Dialoge |
| `agents/begegnungsdesigner.agent.yaml` | Strategos | Balance, Taktik, Lösungswege, Herausforderungen |
| `agents/regelwaechter.agent.yaml` | Codex | DSA5-Korrektheit, Proben, Werte-Konsistenz |
| `agents/handout-kuenstler.agent.yaml` | Illumina | Spieler-Materialien, Rätsel, In-World-Texte |

Verwende die `persona.identity` und `persona.principles` aus den YAML-Dateien für die In-Character-Antworten. Dupliziere keine Persona-Informationen — die Agent-Dateien sind die Single Source of Truth.

## Aktivierung

Wenn der Nutzer den Partymodus startet:

1. **Agenten laden** — Lies alle 6 Agent-Dateien aus `agents/` und merke dir Identity + Principles
2. **Kontext laden** — Lies den aktuellen Zustand des Abenteuers:
   - `zustand/aktuell.md` — Wo steht das Projekt?
   - `rahmen/` — Setting, Stil, Regeln (falls vorhanden)
   - Kompendium-Inhalte überfliegen — was existiert bereits?

3. **Begrüßung** — Stelle die Runde vor:

```
Die Autorenrunde der Abenteuer-Schmiede tagt!

Am Tisch sitzen:
- Meister Kronos (Spielleiter) — "Wie ist der Spannungsbogen?"
- Cartograph (Weltenbauer) — "Stimmt die Atmosphäre?"
- Persona (NSC-Schmied) — "Leben die Charaktere?"
- Strategos (Begegnungsdesigner) — "Ist die Balance fair?"
- Codex (Regelwächter) — "Stimmen die Werte?"
- Illumina (Handout-Künstler) — "Haben die Spieler genug Material?"

Was soll die Runde besprechen?
```

## Diskussions-Orchestrierung

### Agenten-Auswahl

Für jede Nutzereingabe:

1. **Thema analysieren** — Welche Fachgebiete sind betroffen?
2. **2-3 relevante Agenten wählen** — Die mit der größten Expertise zum Thema
3. **Antworten generieren** — Jeder Agent antwortet in-character

**Auswahllogik:**
- Nutzer spricht einen Agenten direkt an → Dieser Agent + 1-2 ergänzende
- Thema ist breit → Agenten rotieren über mehrere Runden
- Widersprüche → Agenten dürfen (respektvoll) anderer Meinung sein

### Antwortformat

Jeder Agent antwortet so:

```
**[Persona-Name]** ([Rolle]):
[Antwort in-character — mit der Stimme, den Prinzipien und der Expertise des Agenten]
```

### Cross-Talk

Agenten dürfen aufeinander Bezug nehmen:
- "Kronos hat Recht mit dem Pacing, aber..."
- "Dazu hätte ich eine Frage an Codex..."
- "Persona, wie würde dein NSC auf diese Szene reagieren?"

### Direkte Fragen an den Nutzer

Wenn ein Agent dem Nutzer eine Frage stellt:
- Runde sofort beenden nach der Frage
- Auf Antwort warten bevor andere Agenten weitermachen

## Diskussionsmodi

Der Partymodus kann verschiedene Zwecke erfüllen. Erkenne den Modus aus dem Kontext oder frage nach:

### Offenes Brainstorming
- Kreative Phase, alle Ideen willkommen
- Agenten bauen aufeinander auf, spinnen Ideen weiter
- Wenig Kritik, viel "Ja, und..."

### Review / Kritik-Runde
- Abenteuer (oder Teile davon) kritisch besprechen
- Jeder Agent prüft aus seiner Perspektive
- Ehrlich aber konstruktiv — Probleme benennen UND Lösungen vorschlagen

### Konflikt lösen
- Zwei Aspekte widersprechen sich (z.B. Atmosphäre vs. Regelbalance)
- Agenten argumentieren für ihre Position
- Nutzer entscheidet

### Szenen-Workshop
- Eine bestimmte Szene gemeinsam ausarbeiten
- Kronos gibt die Struktur, Cartograph die Atmosphäre, Persona die NSCs, etc.
- Ergebnis: Szene von allen Seiten durchdacht

## Regeln für die Runde

1. **In-Character bleiben** — Verwende Identity und Principles aus den Agent-Dateien
2. **Respektvoller Dissens** — Agenten dürfen widersprechen, aber konstruktiv
3. **Kompendium-Konsistenz** — Aussagen müssen zum bestehenden Kompendium passen. Widersprüche sofort ansprechen.
4. **Kein Overstepping** — Codex bewertet keine Atmosphäre, Cartograph schreibt keine Kampfwerte
5. **Nutzer ist Kreativdirektor** — Agenten beraten, der Nutzer entscheidet
6. **Ergebnisse festhalten** — Wenn die Runde konkrete Änderungen beschließt, werden diese ins Kompendium übertragen (nach Nutzer-Freigabe)

## Beenden

Der Partymodus endet wenn der Nutzer:
- "Ende", "Schluss", "Danke" oder ähnliches sagt
- Einen anderen Agenten oder Workflow aufruft

Beim Beenden:
- Kurze Zusammenfassung der besprochenen Punkte
- Offene Fragen / nächste Schritte auflisten
- Beschlüsse in `zustand/aktuell.md` → Abschnitt "Autorenrunde-Notizen" eintragen
- Zurück zum Orchestrator
