XML_File = XML_File = str('/Users/chris/Downloads/cfg000B82A8AC88.xml')


import xml.etree.ElementTree as ET
f1=open("/Users/chris/Desktop/temp.txt",'w+')
tree = ET.parse(XML_File)
root = tree.getroot()
root.tag 
'gs_provision version="1">'
root.attrib
{}
	
for child in root.iter():
	print(child.tag,'=',child.text,sep='',file=f1)







f1.close()

num_lines = sum(1 for line in open(/Users/chris/Desktop/temp.txt"))
import fileinput

with fileinput.FileInput("/Users/chris/Desktop/temp.txt", inplace=True) as file:
	for line in file:
		print(line.replace("None","0"), end='')