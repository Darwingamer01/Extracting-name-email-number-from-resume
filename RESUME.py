import docx2txt
import re

file = docx2txt.process("Resume 1.docx")

l = list()
s=""

for x in file:
    if x!= '\n':
        s+=x
    elif s!='':
        l.append(s)
        s = ""

#for x in l:
#    print(x)

#print(l[0])

for k in range(len(l)):
    if "Tools & Technology" in l[k]:
        for i in range(k, len(l)):
            if "Experience" in l[i]:
                for j in range(i, len(l)):
                    if "Education" in l[j]:
                        break
                    else:
                        print(l[j])