import enchant
import os
from xml.dom import minidom

d=enchant.Dict("en_US")
#If you have predefined list of Medwords,
#d=enchant.DictWithPWL("en_US","MedTerms.dic")

#fr = open("q.xml",'r');
fw = open('q5_spellchecked_indri.xml', 'w')

xmldoc = minidom.parse('queries.clef2013ehealth.1-50.test(copy).xml')
qlist = xmldoc.getElementsByTagName('desc')

count=0
fw.write('<parameters>\n')
for query in qlist:
    fw.write('\t<query>\n')
    fw.write('\t\t<type>indri</type>\n')
    fw.write('\t\t<number>qtest' + str(count+1)+ '</number>\n')
    fw.write('\t\t<text>')
    ind_q = []
    fw.write('#combine(')
    for term in query.childNodes[0].nodeValue.split(" "):
        ind_q.insert(0, term)
        fw.write(term + " ")	
	#print term
	#print str(count+1)+" "+str(d.check(term))
	if not d.check(term):
		correctedList=d.suggest(term)
		fw.write(correctedList[0]+" ")
		print "To query"+str(count+1)+" added "+correctedList[0]
    fw.write(")")
    fw.write('</text>\n')
    fw.write('\t</query>\n')
    count = count+1
fw.write('</parameters>')
