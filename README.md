# Jenseits-Tiger

Ein Arcade-Spiel jenseits von Gut und Böse. Engel wollen dich bekehren, Teufel wollen dich verführen, du willst nur fressen.

- **Laufen:** Maus oder Finger. **Springen:** Klick, Tipp oder Leertaste (zweiter Finger: Sprung geradeaus).
- Nur im Sprung frisst du. Engel fressen ist böse, Teufel fressen ist gut.
- Bleib in der Mitte der Moral-Anzeige. Wer ganz gut oder ganz böse wird, fliegt raus.
- Abwechselnd fressen baut die Kette auf. Ab ×5 beginnt der Rausch, ab ×10 das Delirium.
- Formationen (Buffet, Reigen, Spalier) sind für einen einzigen langen Sprung gebaut.
- Erzengel und Erzteufel brauchen drei Sprünge. Ihre Lichtstrahlen und Feuerringe durchquerst du im Sprung.
- Regelmäßig kommt die Umwertung aller Werte: Engel und Teufel tauschen die Rollen, deine Moral kippt ins Gegenteil.
- Der Schnurrbart macht dich sechs Sekunden zum Übertiger.

## Technik

Eine einzige Datei, keine Abhängigkeiten, kein Build: `index.html` im Browser öffnen.

- Spielfiguren werden auf ein 2D-Canvas gezeichnet und per WebGL nachbearbeitet: Shader-Hintergrund, Bloom, Schockwellen, chromatische Aberration. Ohne WebGL läuft eine einfache 2D-Darstellung.
- Die Musik entsteht live per WebAudio. Ihre Spuren folgen der Kette, die Tonart folgt der Moral-Anzeige.
- `index.html#debug` legt `window.__jt` frei, unter anderem `sim(sekunden, geschick)` für Bot-Durchläufe.
