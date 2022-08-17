import docx2txt
import re

file = docx2txt.process("Resume 1.docx")

pattern1 = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net)')
pattern2 = re.compile(r'[+-0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]')

matches1 = pattern1.finditer(file)
matches2 = pattern2.finditer(file)

for x in matches1:
    print(x.group(0))

for y in matches2:
    print(y.group(0))
