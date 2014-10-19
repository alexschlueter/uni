#!/usr/bin/python
#cvs2Tex, copyright Axel Buß
import csv
from optparse import OptionParser


parser = OptionParser("csv2TeX.py [Optionen] <input.csv> <output.tex>") 
parser.add_option("-c", "--caption", dest="caption", 
                  help="Caption") 
parser.add_option("-l", "--label", dest="label", 
                  help="Label") 
parser.add_option("-d", "--delimiter", dest="delimiter",help="Delimiter")

(optionen, args) = parser.parse_args() 

if (optionen.label != None):
	label = optionen.label
else:
	label = "Label"
if (optionen.caption != None):
	caption = optionen.caption
else:
	caption = "Caption"
if (optionen.delimiter != None):
	delimiter = optionen.delimiter
	if (delimiter == "\\t"):
		delimiter = "\t"
else:
	delimiter = ","
fobj = open(args[1], "w") 
schreib = fobj.write
schreib("\\begin{table}[H] \n")
schreib("\\centering \n")
schreib("\\caption{%s}\n" %caption) 
schreib("\\label{%s}\n" %label)
schreib("\\begin{tabular}{|")
#with open(args[0]) as csvfile:
#    dialect = csv.Sniffer().sniff(csvfile.read(1024))
#    csvfile.seek(0)
#    reader = csv.reader(csvfile, dialect)
reader = csv.reader(open(args[0], "r"), delimiter=delimiter)

s = next(reader)
columns = len(s)
for i in range(columns):
	schreib("c|")
schreib("}\n")
schreib("\\hline \n")
string = ""
for j in range(columns - 1):
	string = string + "%s & " % s[j]
string = string + s[columns-1] # letzter Eintrag braucht kein & am Ende
schreib(string + "\\\\ \n\\hline \n")
for row in reader :
	string = ""
	for j in range(columns- 1):
		string = string + "%s & " % row[j]
		string = string + row[columns-1] # letzter Eintrag braucht kein & am Ende
	schreib(string + "\\\\ \n\\hline \n")
schreib("\\end{tabular}\n")
schreib("\\end{table}\n")		
fobj.close()
print ("Tabelle aus %s nach %s geTeXt" % (args[0], args[1]))

