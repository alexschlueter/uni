#!/usr/bin/python
#cvs2Tex, copyright Axel Buss
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
reader = csv.reader(open(args[0], "rb"), delimiter=delimiter)

s = reader.next()
columns = len(s)
for i in range(columns):
	schreib("c|")
schreib("}\n")
schreib("\\hline \n")
string = ""
i = 0
for j in range(columns - 1):
	string = string + "%s & " % s[j]
	i = j
string = string + s[i+1]
schreib(string + "\\\\ \n\\hline \n")
for row in reader :
	string = ""
	for j in range(columns- 1):
		string = string + "%s & " % row[j]
		i = j
	string = string + row[i+1]
	schreib(string + "\\\\ \n\\hline \n")
schreib("\\end{tabular}\n")
schreib("\\end{table}\n")		
fobj.close()
print "Tabelle aus %s nach %s geTeXt" % (args[0], args[1])

