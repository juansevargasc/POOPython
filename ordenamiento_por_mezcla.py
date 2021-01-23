import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2 
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)
    
        # Llamada recursiva en cada mitad.
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0; j = 0
        # Iterador de la lista principal
        k = 0

        print(f'Lista prev while {lista}')
        print(f'Prev while: izquierda {izquierda}, derecha {derecha}')
        while i < len(izquierda) and j < len(derecha):
            print(f'if {izquierda[i]} < {derecha[j]}')
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
            print("Lista W1 ", lista)
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
            print("Lista W2", lista)

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            print("Lista W3", lista)
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño será la lista? '))
    
    lista = ( [random.randint(0, 100) for i in range(tamano_de_lista) ] ) # LLenar de números aleatorios los elementos de la lista
    #lista = [2, 4, 6, 1, 8, 3, 5, 7]
    print(lista)
    print('-' * 20)
    
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)