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
