import docx2txt
import re

file = docx2txt.process("Resume 1.docx")
l = list()
s = ""
for x in file:
    if x!= '\n':
        s+=x
    elif s!= "":
        l.append(s)
        s = ""

#To print all of the data given in resume;
#for x in l:
#    print(x)

print (l[0])

for j in range(len(l)):
    if "LinkedIn" in l[j]:
        for f in range(j+1, (len(l))):
                if "Professional Summary" in l[f]:
                    break
                else:
                    print(l[f])

#To print Professional Summary;
#for k in range(len(l)):
#    if "Professional Summary"in l[k]:
#        for h in range(k, len(l)):
#            if "Tools & Technology" in l[h]:
#                break
#            else:
#                print(l[h])


pattern1 = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net)')
pattern2 = re.compile(r'[+-0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]')

matches1 = pattern1.finditer(file)
matches2 = pattern2.finditer(file)

#To print only email address and
#for x in matches1:
#    print(x.group(0))

#for y in matches2:
#    print(y.group(0))
