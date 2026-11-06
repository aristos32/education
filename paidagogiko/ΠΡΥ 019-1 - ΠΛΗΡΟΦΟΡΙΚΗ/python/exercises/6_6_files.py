f = open("test2.txt", "r+")
#f.write('1st rine. \n')
#f.write('2nd \tline. \n')
#print(f.readlines())
for line in f:
    lista = line.split()
    print(lista[1])
f.close()
