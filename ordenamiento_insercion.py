# Módulo necesario para generar números aleatorios
import random

def ordenamiento_por_insercion(lista):
    
    # Recorre la lista
    for indice in range(1, len(lista)):
        # Guarda el valor actual y la posición actual
        valor_actual = lista[indice]
        posicion_actual = indice

        # Si no está enla primera posición y el elemento anterior es mayor que el actual
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            # Le da al valor actual el valor y vuelve a la posición anterior
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        
        # Le da al valor actual (Que realmente es el anterior si ha entrado en el while) 
        # el valor del principio. Realmente hace un intercambio de valores actual por anterior
        lista[posicion_actual] = valor_actual
    return lista

# Crea una lista con números aleatorios y la muestra. Luego la ordena y la muestra
if __name__ == '__main__':
    tamano_de_lista = int(input('Deque tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)