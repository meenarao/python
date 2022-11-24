#reading a file 
f = open("files.txt","r")
content=f.readline()
print(content)
f.close()