# Sandpile identity

Berechnet das Identitätselement der abelschen Sandhaufen-Gruppe auf einem n×n-Gitter
und rendert es als PNG. Nur Go-Standardbibliothek.

    go run . -n 400 -out identity400.png -scale 2

Ausgabe: Topple-Zahlen, Korn-Histogramm, drei Gruppen-Checks
((e+e)°=e, (m+e)°=m, (m+m)°≠m) und die Kantenlänge des zentralen 2er-Quadrats.

Quellen:
- Bak, Tang, Wiesenfeld, "Self-organized criticality", Phys. Rev. Lett. 59 (1987)
- Dhar, "Self-organized critical state of sandpile automaton models", Phys. Rev. Lett. 64 (1990)
- Levine, Propp, "What is … a sandpile?", Notices AMS 57(8), 2010 – Formel e = (2m − (2m)°)°

## Messreihe: zentrales 2er-Quadrat

    for n in $(seq 30 300); do go run . -n $n -quiet; done   # n side side/n

Dateien `sweep_*.txt` (n, Seite, Verhältnis), Grafik via `python3 plot_sweep.py` → `sweep.html`.

Befund (n = 30 … 500, 173 Größen): Seite ≈ 0,415·n + 1,1 (lineare Anpassung, RMS 0,67,
Ganzzahl-Quantisierung). Das Verhältnis Seite/n fällt von 0,44 (n≈50) auf 0,418 (n = 400 … 500);
ob es gegen eine feste Konstante konvergiert, ist aus diesen Daten nicht entscheidbar.
Bei ungeradem n hat die Identität ein Kreuz aus Einsen durch das Zentrum mit einer 0 in der Mitte;
das Kreuz endet genau am Rand des 2er-Quadrats. Bei geradem n gibt es kein Kreuz.
