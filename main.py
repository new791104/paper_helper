filename = "a.txt"

readfile = open(filename,'r')
writefile = open("output.txt","w")
paragraph = ""

with open(filename) as file:
    lines = (line.strip('\r\n') for line in file)  #lines 是底下 for迴圈 的 generator, string.strip() 是一個刪減字串的方法
    for line in lines:
        paragraph += line
        print(line,end='')

writefile.write(paragraph)
readfile.close()
writefile.close()

