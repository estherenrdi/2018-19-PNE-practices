def printing(filename):
    archivo = open(filename, 'r')
    hola = archivo.read()
    archivo.close()
    return hola
archiv = 'CPLX2.txt'
print(printing(archiv))

