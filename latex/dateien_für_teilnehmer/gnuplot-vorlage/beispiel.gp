### Einstellungen
# Terminal: Wählt pdf, um als PDF-Datei auszugeben,
#     oder wxt, um das Ergebnis auf dem Bildschirm zu sehen
set terminal pdf
#set terminal wxt
# Werte mit Komma als Dezimal-Separator einlesen (Linux)
set decimalsign locale "de_DE.UTF8"
# Werte mit Komma als Dezimal-Separator einlesen (Windows)
#set decimalsign locale "german"
# Dezimalbrüche mit Komma ausgeben
set decimalsign ','
# Zwischenschritte auf x-Achse anzeigen
set mxtics
# Zwischenschritte auf y-Achse anzeigen
set mytics
# Legende unterhalb des Diagramms anzeigen
set key bmargin
# Beim fit-Befehl nicht so viele Infos in die Konsole schreiben
set fit quiet
# Fehler auf berechnetet Parametern in Variablen <parameter>_err speichern
set fit errorvariables

# Beispiel einer Funktionsdefinition:
# Funktion f(x) (eine Gerade)
# Parameter m und b müssen vor der Verwendung definiert
# werden (z.B. durch Anwendung von "fit")
f(x) = m * x + b

### Erstellung eines Graphen
# Name der Ausgabedatei
set output "beispiel.pdf"
# x-Bereich auf x ≤ 800
set xrange [:800]
# x-Bereich auf das Intervall [-25; 25] beschränken
set yrange [-25:25]
# Beschriftung x-Achse
set xlabel "Zeit [s]"
# Beschriftung y-Achse
set ylabel "Temperatur [°C]"
# fit-Befehl
#     - nur Punkte im x-Intervall [18; 24,2] berücksichtigen
#     - Funktion f(x) zum Fitten benutzen
#     - Messwerte aus der Datei "messwerte.txt" lesen
#     - Spalte 1 für x-Werte und Spalte 2 für y-Werte verwenden
#     - Parameter m und b bestimmen
fit [18:24.2] f(x) "messwerte.txt" using 1:2 via m, b 
# plot-Befehl
#     - Punkte in Datei "messwerte.txt" plotten
#         * Spalte 1 für x-Werte und Spalte 2 für y-Werte verwenden
#         * keine Legende
#     - Funktion f(x) plotten (mit berechneten Parametern!)
#         * als Legende einen Text mit eingefügten Zahlen verwenden;
#           statt "%.3g" wird jeweils eine der Zahlen, die nach der Zeichenkette
#           angegeben wird, auf 3 Kommastellen gerundet eingefügt
plot "messwerte.txt" using 1:2 notitle, \
	f(x) title sprintf("Ausgleichsgerade (Raumtemperatur): (%.3g) x + (%.3g)", m, b)
# Ausgabe der berechneten Parameter in der Konsole
print "Berechnete Parameter:"
print "m = ", m, " +- ", m_err, "; b = ", b, " +- ", b_err


