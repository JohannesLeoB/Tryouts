# Johannes-Wortlaut ALFA_OS, kondensiert
Quelle: johannes-wortlaut.md (2004 Zeilen, 2026-10-10T16:43 bis 2026-10-13T18:44, UTC). Format: Regel/Entscheidung → Datum. Zitate `„…“` wörtlich. Gestrichen: Doppelungen, Tool-Ausgaben, Dateilisten, Fremdtexte, Smalltalk.

## 0. Sitzungen (Rollen teils erschlossen)
| ID | Rolle |
|---|---|
| 7cc894d9 | Chef/Bauer, „ALFA · 01 · MAX“ (Code, Repo-Maschinerie) |
| a9bb817c | Boss „Fable“ (ab 10-11 21:00 „BossEntwickler“), Design↔Code-Übergabe |
| 79d12623 | Sonnet, Wahr/Falsch-Gegenspieler (10-12) |
| c2a04c8a | neue Boss-Sitzung, Sonnet 5.5 (ab 10-13 15:48) |
| Design | Claude Design im Chrome-Browser, „ALFA · 02 · MAX · Design“, Projekt `f0294bfd…`, schreibt nur in eigenes Projekt, liest GitHub nur nach manuellem Sync |

## 1. Dauerregeln (gelten ab Nennung; Quelle in Klammern)

### Richtung Design → Code
- Johannes entscheidet Design. Der Entwurf in Claude Design ist entschieden; Code zieht nach, exakt inkl. Bewegung. (10-10 19:21; 10-13 12:35, 12:36 „Wie oft habe ich das bereits gesagt???“)
- Code gestaltet nie. Fehlt ein Wert/Icon/Vorlage: nicht erfinden, als Forderung an Design melden. Platzierung/Shell/Aufbau darf Code verantworten. Keine Maße/Token geliefert → keine App bauen. (10-12 21:05, 21:07 „reine Funktion. Ader, aber keine Haut“)
- Eigenmächtig Deklariertes zurückbauen und an zentrale Vorgaben hängen. (10-12 21:09)
- Übergabe nur als Daten (Werte, Token, Maße, Funktionen), nie Bilder/Screenshots/Pixel. Gleiche Sprache bei Design und Code; Wörterbuch muss bei beiden identisch sein. (10-11 13:19, 13:51; 10-12 23:23; 10-13 16:17, 18:24 „mindestens 12 mal klar gesagt“)
- Kein Screenshot-Abpausen; Messen aus Daten/Rendern. Rendern 1:1 Design gegen Code, keine Bilder. (10-12 23:37, 23:40; 10-13 16:35 „Nicht nach html!“)
- Ein Schritt ändert Logik ODER Aussehen, nie beides. (10-11 20:04 „code Umbau und refreshed Ui gehen nicht“)
- Johannes sieht vorab 1:1, was eingebaut wird, nicht erst im Bau nachjustieren. (10-11 15:59)
- Benennung: macOS-/Swift-Best-Practice, englische Bezeichnungen; Wörterbuch darf ins Repo/Code, wenn beide es einhalten; im Lastenheft nur als Abschnitt. (10-13 16:12–16:20)
- Design-Bögen zuerst separat extern „tumblen“/prüfen (Maß, Baubarkeit, Deckung), dann erst Bau. (10-12 19:01)
- Design-Session kennt Uhrzeit nicht → Uhrzeit mitliefern. (10-13 12:50)

### Verhalten der Sitzungen
- Nichts weitergeben, was nicht selbst vollständig gelesen/geprüft wurde. Prüfen heißt vollständig: jeder Wert, Name, Platzierung, Bewegung; „NICHTS darf an COde gehen, was nciht absolut bombenfest ist“. (10-13 12:08–12:10)
- Keine Abkürzungen ohne Rückfrage; Nachrichtenzeilen rechnen, nicht schätzen. Eigene Annahmen als solche kennzeichnen. (10-13 17:35, 17:41)
- Keine Fragen ohne Grund; vor Fragen die eigene Historie/Johannes' Nachrichten durchsuchen. Übersetzungsprobleme zwischen Claudes sind nicht seine Entscheidung. (10-11 13:51; 10-11 19:17; 10-13 18:15)
- Wenn Johannes etwas gesagt hat, nicht erneut fragen: Spalten sind beweglich, es gibt keine festen 616/560, nie 3 auf Minimum. (10-13 17:49–18:15)
- Keine Mikroverwaltung durch Boss; Chef entscheidet im Planrahmen selbst; Chef delegiert, hält Fäden, codet nur als „Bossmove“. (10-10 23:55; 10-12 17:11, 18:17)
- Keine Sammlung/Notizen/Regeln/Prüfer/Pakete auf Vorrat; in Repo „Festgehaltenes“ ist für ihn Schall und Rauch; wichtig ist, dass die Sitzung selbst weiß, was Sache ist. (10-11 19:40; Compact 10-12 16:05)
- Ehrlich arbeiten statt schnell; Fehler offen benennen, bei Überforderung melden. (10-13 17:35, 12:08)
- Johannes in klaren Worten ansprechen: was, warum, Bedeutung für die App; keine Nummern/Kürzel/Ticketnamen. (10-11 19:44)
- Prüfung/Test braucht Erklärung und Legitimation: wer, warum, wann, welches Limit („Man muss wissen warum man geblitzt wurde“); befristete Duldungen möglich („Ampel“). (10-11 00:53, 00:55)
- Tests: nur gegen Attrappen, nie gegen Schlüsselbund/Realdaten. Jeder Test muss bei seinem Auslöser anschlagen (Mutationsprobe); Tests zusammenlegen/entfernen, doppelblind sweepen. (10-11 21:23; 10-13 01:59, 02:05)
- Pro Bug zuerst nachbauen/simulieren, dann fixen (5 Sonnet-Worker). (10-12 19:41)
- Vor commit/push/merge: vorab festgelegte 20er Wahr/Falsch-Liste, von anderem Agent geschrieben; nicht beantwortbar → Session ist selbst schuld. (10-12 18:31)
- Pro Commit: Tests exit 0; jede Behauptung mit Quellzeile; Diff nur Dateien aus dem Plan. (10-12 16:37)
- Bauzeitenplan: „written for agents“, wenig Text, bei jedem Commit geprüft, angepasst statt ergänzt, belegt, mit Datum+Session gezeichnet. (10-12 16:37)
- Rücklieferungen (Design-Fläche, Antworten anderer Sitzungen) kommen immer nach GitHub (geschlossene Kette). (10-10 21:21; 10-12 16:05)
- Artefakte/Dokumente mit Datum im Namen; Master datiert; jede Änderung mit Name+Session gezeichnet. (10-10 23:23–23:25)
- Subagenten: je Schwarm begrenzt und im Blick; 2 Haiku frei, 5 nach Bestätigung, 10–20 nach Zielangabe. (10-10 16:43)

### Code-Hygiene
- Nichts hardcoden: Rechte, Sperren, Schreibsperren, Vier-Augen, Konten, Höchstzahlen = App-Einstellungen je Integration/User/Firma/Team. Keine Rechte im Code; Admin-Layer erst, wenn alles Sperrbare existiert. (10-10 22:12, 22:14; 10-12 17:49)
- Kundennummer-Beispiele u. ä. sind App-Entscheidungen, keine Code-/Sicherheitsfragen; nicht im Code festschreiben. (10-10 18:24)
- UI-Texte/Behauptungen im Code, die „AI-Slop“ sind (Erklärsätze, Schloss-Hinweise, „Entwurf liegt sicher“ obwohl nie gespeichert) → raus. Alte Code-Basis ist voll davon; nichts wegen scheinbarer Wichtigkeit stehen lassen. (10-12 17:46, 17:49, 23:27)
- Keine Eigenbauten ohne Registrierung, keine hardcodierten Werte/Annahmen. (10-12 19:41)
- Fehler/Zustände tragen das vollständige Anbieter-Original (Anbieter, Status, Code/Grund, Servertext, Request-ID); UI zeigt 3 Zustände (Fehler/Eingeschränkt/online) mit Detail-Button für Vollbericht. Anbieter-Knotenpunkte/Handles immer übernehmen, nie Status erfinden. (10-12 20:19–20:23)
- Arbeiten am Root-Code statt endlos sammeln/vergleichen. (10-10 22:33)
- Existierendes (ALFA/ALPHA/Fundus, ~800 Swift-Dateien) ist Fundament; „muss nur richtig ALFA werden“. Altes wegwerfen, was stört. Fundstücke sind Goldgrube, aber nicht alles ist Gold; Headlines von heute werden widerlegt. (10-10 19:32–19:38; 10-11 00:41)

### Repo/Dokumente (Stand 10-13)
- Docs radikal reduzieren (89–95 %), writing for agents, altes weg, Falsches strikt berichtigen; Gelöschtes auch aus Kontext und Git-Historie. (10-13 16:22, 16:23)
- Max 10 Docs im ganzen Repo; jedes bei Lektüre mit Lese-Zeitstempel; >24 h ungelesen → zur Löschung vorlegen. `ausgang/` vollständig bereinigen. (10-13 18:44)
- `CLAUDE.md`: max 5 Bulletpoints à max 3 Zeilen. (10-13 18:44)
- Wichtiges klipp und klar an der Wurzel des Repos, nicht im Anhang. (10-13 18:28)
- Alle Issues samt Kommentaren löschen; Issues dienten nur dem Zuschreiben. Zuvor alle Kommentare lesen. (10-13 18:34, 18:40)
- `ausgang/quellen/johannes-wortlaut.md` war 0 kB → Ursache klären. (10-13 18:44)
- „Briefe ohne Absender/Empfänger“ entfernen, sobald Übergabepaket sitzt (erinnern). (10-10 21:21; 10-12 16:05)

## 2. Produktentscheidungen
- Ziel: App sieht und fühlt sich im Code exakt wie im Design an; sauber, lebhaft, schön, schnell. Prüfstein ist sein Auge. (10-11 00:41)
- Struktur: 3 Spalten (Bahnen), Blob, UI-Blöcke, Integrationen, SaaS-Anbindungen. Blob öffnet Assistent (Doppelklick), Assistent später eigener Vollbereich. (10-10 20:34; 10-11 00:46, 15:06)
- Hülle = Passepartout/Grundriss: globale Funktionen, Mechanik, Grundlayout. Bahntitel/Inhalte gehören nicht in die Hülle, sondern in die abgeleiteten Ansichten (Mail/Einstellungen sind bewusste Variationen der Standardhülle). Keine Mail-Fragmente („Postfach“) in der Hülle. (10-13 16:30, 17:35)
- Bahnen: beweglich (ziehen/falten/auf-ziehen); Mitte ohne festes Mindestmaß; keine festen Zielbreiten außer wo Design Festwerte gibt, Rest skaliert; Höhe analog. Seitenbahn max 380. (10-11 15:06; 10-13 16:28, 17:49–18:15)
- Maßsystem: 4er-Leiter, 56er-Raster (56, 2×56, 5×56 …); Ruhebreite 280; 1 und 2 erlaubte Minima; Kapsel 999 korrekt; Schriftgrößen außerhalb der 4er-Leiter. Offen: space.punkt 6, space.blobRand 6, Schrift 9/11,5/13/18 → an Design zurückspielen und klären. (10-13 00:01, 16:05–16:11)
- Fenster: Apple-Ampel oben links über dem bestehenden Fenster, ohne Innenbild zu ändern. (10-12 16:51–16:52)
- Konten-Hub in Einstellungen (nicht in Mailansicht): bis zu 3 Mailkonten (Gmail/Outlook/GMX/web.de/IMAP gemischt, Max-Zahl einstellbar), je Konto Signatur; Konto entfernen = Hinweis + zweiter Klick (Text liefert Design). Echte Accounts, kein Beispielpostfach. Mailclient abnabeln, neue „Naht“ (Sync, Push, Rückwege). Integrationen leicht einwählbar (Muster integrations.sh / UsefulSoftwareCo/integrations). (10-12 14:43–14:54, 18:48, 20:14, 20:15)
- Schlüsselbund: neue App liest vorerst ALPHA-Einträge (nur lesend), kein Neu-Anmelden. (10-12 14:43)
- Integrationsumfang offen/zu klären: Airtable, ClickUp, Slack, Drive, sevDesk, DHL, Kalender, Kataloge/DBs, Shopify/Lexware/Tradeplace-XML, KI-APIs (Claude/ChatGPT/Gemini), Fireflies, Adobe, Vectorworks, Dropbox/Supabase/eigener Server/Ionos. „Wahrheit je Datenart“ ist Einstellung. (10-12 17:56–18:03)
- Distribution: App geht über Studio hinaus (App Store, später iOS/iPadOS/Web, SaaS/Abo); Struktur muss das vorsehen; Mobil abgespeckt, nicht Mac-1:1. Kein Marktplatz-Denken, aber nicht „zu klein“ denken. (10-12 18:06–18:11)
- Hub/Einstellungen als „Webstuhl“ (Kette/Schuss), erweiterbar um neue Integrationen mit read/write. (10-12 19:01)
- Design-Stand 0,1: Einstellungen + Mail als B/W, wenig Detail. (10-12 19:01)
- Design-Freiheit: Design arbeitet kreativ mit Johannes; alte Arbeitswelt-Artefakte nicht nachäffen. „ALFA Interface“ ist nicht der Gral, ist als Seed kommentiert. (10-11 16:47, 17:44)
- Begriff: „Integrationen“, nicht „Angebote“. (10-13 13:11)
- Entscheidung Wortlaut-Klarstellung: bei „Konto entfernen“ gab Johannes Hinweis + 2. Klick frei, nicht den Text. (10-12 20:15)
- Keine Speicherung von Entwürfen behaupten, solange Code sie nicht speichert. (10-12 23:27)

## 3. Chronik (Entscheidungen/Ereignisse)
### 10-10
- 16:43 Onboarding Boss/Chef; Q/A-Format für Fragen.
- 18:24–19:44 Hardcoding ist Einstellungssache; Zielverständnis statt Tabellieren; Design-Artefakt aus Screenshot = führende erste Linie; Code und Design haben unterschiedliche Wahrheiten, brauchen Ticker/Korrespondenz; Parallelsitzungen brauchen gemeinsame Sicht (auch die 2 Nebenkonten).
- 20:16 Text ins Team-CLAUDE.md in Repo/GitHub ergänzen und straffen.
- 20:28–20:52 Mail-Abgleich mit ≤10 Haiku; Repos: JohannesLeoB/ALPHA, mykilOS-V2 („Ur-Uropa“); ALLES der letzten Wochen aus 3 Konten = Exploration/Studien.
- 22:12–22:14 Wächter nicht aufgerufen / Clockodo-Sperre immer `true` / Vier-Augen nur in Doku → alles Einstellungen, nicht Code.
- 23:08–23:17 „bau die eine Fassung“; to-spec über Produktions-Setup, 5 Sonnet + 15 Haiku.
- 23:21–23:29 Eine Arbeitswelt MASTER, datiert, mit Stand-Vermerk und Ticker je Änderung; Design liest GitHub nur nach manuellem Sync; Cloud-Sitzungen als Außenstelle.
- 23:55–00:04 Aufgabenteilung 2+2; Konto johannes@mykilos.com zuerst; Nebenkonten für Nebenaufgaben.

### 10-11
- 00:11–00:59 Prüfsystem darf nicht „zu Tode testen“; Ein Brief an Design, aktuell gehalten (Stand, Lücken, Rückfragen, Entscheidungen); GitHub muss brandaktuell sein; deep-research zu Schablonen/Artefakten.
- 01:25 Research: welche Artefakte bilden die App ab (Drift, Doppelungen).
- 02:03–02:46 Weiter mit Bau; Fable als „Chef-Kumpel“ befragen, Stand festhalten, Ballast weg.
- 13:15–13:55 Versätze/Abstände/halbtransparente Schnipsel: nicht abpausen, Maßwerte-Grundlage; „blind auf dich verlassen können“.
- 14:09–14:57 Design-Session noch nie gestartet; Seeds = Master 1010 + Werkbank + Schablonen; Design kann Links nicht lesen → Export/Zip.
- 15:05–15:18 Design-Probe: Projekt falsch; Wert `component-lane-leading-max-width` 420→380px geschrieben (v1791731861-d49d).
- 15:27–16:25 Entwurfsbogen/Blob-Position („Blob soll oben links schweben“); Pingpong mit falschen Werten abgelehnt; Frage, warum nicht Claude Design in Chrome als Rendering-Quelle.
- 16:44–17:44 Design-zu-Swift prüfen; Fable-Abstimmung; Fable-Vorschlag umsetzen.
- 18:22–19:47 ZIP gebaut; Chef soll Mail/Einstellungen im Altcode erfassen; Aufwand-Check; Assumptions hinterfragen; Einzugsplan/Tickets unverständlich; Unnötiges löschen, ein einziges gültiges ZIP.
- 19:54–20:28 „Schmutziges“ Paket an Design = verantwortungslos; Fable-Paket erstellen.
- 21:00 Fable wird BossEntwickler; 21:09 Code für Mail/Einstellungen muss an Design geliefert werden (Zustände je Bereich).
- 22:21 Opusplan-Settings-Vorschlag (Opus plant, Sonnet tippt, Haiku sucht, Critic) vorgelegt: „Machen wir?“

### 10-12
- 14:27–14:33 Kapitelwechsel; Branch-Regel „main-protect“ prüfen; Loop für Design→Code-Lieferungen (Tests grün, CI grün, PR mit Design-Loop). Design soll in ~24 h einziehbar sein.
- 14:43–15:59 Mail-Konten-Hub, Konten-Naht, Schlüsselbund (siehe §2); Paket mit Spezifikation/Ist-Soll für Chef; Worker lesen ALFA+ALPHA-Einstellungen.
- 16:19–16:37 Artifact Bauzeitenplan (Querformat, Soll/Ist, Zeitstrahl, Meilensteine), agent-lesbar.
- 16:49–16:54 Abnahme Schlüsselbund: dist/ öffnen, Google anmelden, neu starten; Safari-Login klappt.
- 17:09–17:19 Ältere Artefakte = gleiche App, andere Ansätze; Token-/Farbdateien: Löschen vs. Umhängen prüfen, Fable fragen.
- 18:03–18:16 Integrationsmodell vergleichen (Slack/Monday/Carat/ERPNext/ClickUp/Claude); Wahr/Falsch-Spiel mit Sonnet (20+20 Aussagen; Treffer nur 7/20 wegen ALPHA↔alfaos-Verwechslung).
- 18:28–18:31 Idee: Vorab-20er-Liste vor Commit/Push.
- 18:48 2 Google-Konten verbunden; Konten gehören in Einstellungen.
- 19:01–19:09 Chef übergibt Design Specs + Wireflow für Hub; Design-Stand „Einstellungen Kacheln“.
- 20:09–20:24 Drei Mailfehler (web.de hängt, GMX-Absender, Dauerfehler) → Anbieter-Doku nutzen; Original-Fehlerbericht; Lastenheft/Sync-Paket an Design.
- 20:32–21:09 Fenstermaße 1512×982 / 960×600 hinterfragt; Rollenklärung „reine Funktion, keine Haut“.
- 21:35 224 eigenmächtige Stellen (78 Haut, 67 Werte, 22 Texte, 57 Verhalten) zurückzubauen.
- 23:17–23:40 Gegensicht auf Zip (6); Ehrlichkeitsprüfung; Design-gegen-Code rendern, ohne Bilder; Johannes: Maß-Entscheidungen lagen schon in Design (Blob/Breiten/Radien).

### 10-13
- 00:01 Maßregel (siehe §2); 00:40 Anatomie-Überblick; 01:16–02:05 Testprüfung/Mutationen/Testbereinigung.
- 12:01 Rückbau, dann 0.1.8.
- 12:03–12:36 Zip (7) auf Baubarkeit: nur oberflächlich geprüft → Vorwurf; vollständige Prüfung gefordert; Richtungsfehler („Design müsste nachbessern“) korrigiert.
- 12:39–14:33 Ursachenanalyse Vergessen; Chef bleibt angehalten; Boss managt Lieferung Design→Chef 100 % akkurat (5-fach validiert); Lastenheft validieren; Neustart in neuer Sitzung.
- 15:04–15:38 Prozess feilen (Hooks, Skills je Phase, Sichern, Feedbackschleifen); alle Vorschläge abwägen; Prompt an Design; Paket erst nach Design-Check.
- 15:45 Design liefert `paket-01/` (5 Bögen, WERTE.json, INHALT.json, NAMEN.md, INVENTAR.md 79 Bauteile, ZUSTAENDE.md). Fehlend: loadingMore, noFilterMatch, signInExpired, saving, queuedInOutbox; Farbleiter-Zitat nachzuliefern; Einstellungen existieren doppelt (4 Kategorien vs. 12 Abschnitte).
- 15:48 neue Boss-Sitzung c2a04c8a mit Auftrag: Eingang prüfen, einfrieren (SHA-256), Lastenheft schmal berichtigen, 5 Prüfdurchgänge; Chef nicht anschreiben, nicht committen/pushen.
- 15:54–17:11 3 unabhängige Sonnet-Prüfer; 4er-Leiter-Abgleich; 3 Bögen 1:1 rendern.
- 17:35 Rendering-Mängel (Postfach in Hülle, Schrift nicht geladen, Griff gerechnet statt gemessen, erfundene Trennlinien, Zeilen geschätzt) → Standpauke, Vertrauensfrage.
- 17:41–17:49 Chrome headless nur als Messwerkzeug; Spaltenmaße beweglich.
- 18:17 „Wer hat das entschieden?“ (headless-Chrome-Freigabe ohne seine Entscheidung).
- 18:24 Design-Daten-Protokoll statt Pixelkopien.
- 18:28–18:44 Issues abschaffen (alle löschen, vorher Kommentare lesen); CLAUDE.md ≤5 Bullets; ≤10 Docs mit Lese-Stempeln; leeres johannes-wortlaut.md klären.

## 4. Offen (Stand 10-13 18:44)
- Issues + Kommentare lesen, dann alle löschen.
- `ausgang/` bereinigen, ≤10 Docs, Lese-Zeitstempel einführen, `CLAUDE.md` kürzen.
- Leere `johannes-wortlaut.md` erklären/neu erzeugen (diese Datei ist der verdichtete Ersatz).
- 6er-Maße (space.punkt, space.blobRand) und Schriftgrößen 9/11,5/13/18 an Design zurück; Farbleiter-Wort von Johannes nachliefern; Einstellungen-Doppelfassung klären.
- Lastenheft schmal berichtigen (nur was Design noch liefern muss; Namen nur aus Entwurf; Quelle je Zeile; 5 Prüfdurchgänge).
- Design→Code-Datenprotokoll statt Pixelvergleich etablieren.
- Eigenmächtige Code-Stellen (224) zurückbauen; Mail-Konten-Hub/Integrations-Naht bauen; „main-protect“-Regel, Actions/Wiki/Projekte abschalten (10-12 offen).
