filename = "a.txt"

readfile = open(filename,'r')
writefile = open("output.txt","w")
paragraph = ""

for line in open(filename,'r'):
    line -= '\r\n'
    paragraph += line
    print(line)
writefile.write(paragraph)
#print(paragraph,end="")
readfile.close()
writefile.close()

