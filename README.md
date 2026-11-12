# Jenseits-Tiger

Ein Arcade-Spiel jenseits von Gut und Böse. Engel wollen dich bekehren, Teufel wollen dich verführen, du willst nur fressen.

## Spielen

`index.html` im Browser öffnen (zusammen mit `voice.js` im selben Ordner). Kein Build, keine Abhängigkeiten.

- **Laufen:** Maus, Finger oder WASD/Pfeiltasten. **Springen:** Klick, Tipp oder Leertaste (zweiter Finger: Sprung geradeaus). **Pause:** P oder Esc.
- Nur im Sprung frisst du. Engel fressen ist böse, Teufel fressen ist gut.
- Bleib in der Mitte der Moral-Anzeige. Wer ganz gut oder ganz böse wird, fliegt raus.
- Abwechselnd fressen baut die Kette auf. Ab ×5 beginnt der Rausch, ab ×10 das Delirium.
- Im Sprung bist du unantastbar, auch für Lichtstrahlen, Feuerringe und Lanzen.
- Regelmäßig kommt die Umwertung aller Werte: Engel und Teufel tauschen die Rollen, deine Moral kippt ins Gegenteil.

## Kapitel

| Kapitel | Neu | Endgegner |
| --- | --- | --- |
| I Morgenröte | Engel, Teufel, Formationen (Buffet, Reigen, Spalier) | Erzengel |
| II Menschliches, Allzumenschliches | Menschen (fressen kostet die Kette), Schwärme | Erzteufel |
| III Die fröhliche Wissenschaft | Doppelmoral (Joker), der Hammer | Erzengel und Erzteufel |
| IV Götzen-Dämmerung | Eiferer mit Lanze | Der Götze |
| V Also sprach der Tiger | alles zusammen | Götze, Erzengel und Erzteufel |

Danach beginnt die ewige Wiederkunft: dieselben Kapitel, schneller und härter.

Fundstücke: der **Schnurrbart** (sechs Sekunden Übertiger), der **Hammer** (frisst alles in Reichweite, streng abwechselnd), der **Ring** (ein Extraleben).

## Technik

- Spielfiguren werden auf ein 2D-Canvas gezeichnet und per WebGL nachbearbeitet: Shader-Hintergrund, Bloom, Schockwellen, chromatische Aberration. Ohne WebGL läuft eine einfache 2D-Darstellung.
- Die Musik entsteht live per WebAudio. Ihre Spuren folgen der Kette, Tonart und Tempo folgen Moral-Anzeige und Kapitel.
- Die Ansagen liegen als MP3 in `voice/` (erzeugt mit ElevenLabs, Stimme „Haunting-Hector“). `python3 tools/build_voice.py` packt sie in `voice.js`.
- `python3 tools/build_single.py out.html` schreibt das ganze Spiel in eine einzige Datei.
- `index.html#debug` legt `window.__jt` frei, unter anderem `sim(sekunden, geschick)` für Bot-Durchläufe.
