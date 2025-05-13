lista = []
busqueda = input()

def linearsearch(lista,busqueda):
    for i in range (len(lista)):
        if lista[i] == busqueda:
            return i
    return False

#Ejemplo
lista = [3,2,1]
print (linearsearch(lista,3)) #imprimiria 0, ya que es el indice de lo que estamos buscando