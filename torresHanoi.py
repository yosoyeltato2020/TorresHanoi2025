def hanoi(n, origen, destino, auxiliar, torres):
    """
    Función recursiva para resolver el problema de las Torres de Hanoi.
    
    Parámetros:
    - n: Número de discos a mover.
    - origen: Torre desde donde se moverán los discos.
    - destino: Torre hacia donde se moverán los discos.
    - auxiliar: Torre auxiliar que ayuda en el proceso.
    - torres: Diccionario con el estado actual de las torres.
    """
    if n == 1:
        # Caso base: Si solo hay un disco, lo movemos directamente de origen a destino
        disco = torres[origen].pop()  # Sacamos el disco de la torre de origen
        torres[destino].append(disco)  # Lo colocamos en la torre de destino
        print(f"Mover disco {disco} de {origen} a {destino}")
    else:
        # Paso 1: Mover n-1 discos desde la torre de origen a la torre auxiliar
        hanoi(n - 1, origen, auxiliar, destino, torres)
        
        # Paso 2: Mover el disco restante (el más grande) desde la torre de origen a la torre destino
        hanoi(1, origen, destino, auxiliar, torres)
        
        # Paso 3: Mover los n-1 discos desde la torre auxiliar a la torre destino
        hanoi(n - 1, auxiliar, destino, origen, torres)

def resolver_torres_de_hanoi(n):
    """
    Función principal para inicializar las torres y resolver el problema de las Torres de Hanoi.
    
    Parámetros:
    - n: Número de discos que queremos mover.
    """
    # Inicializamos las torres usando un diccionario
    torres = {
        'A': list(range(n, 0, -1)),  # Torre de origen con todos los discos en orden descendente
        'B': [],  # Torre auxiliar vacía
        'C': []   # Torre de destino vacía
    }
    
    print("Estado inicial de las torres:")
    print(torres)  # Mostramos el estado inicial de las torres
    
    # Llamamos a la función recursiva para resolver el problema
    hanoi(n, 'A', 'C', 'B', torres)
    
    print("Estado final de las torres:")
    print(torres)  # Mostramos el estado final de las torres

# Ejemplo de uso
n = 3  # Número de discos a mover
resolver_torres_de_hanoi(n)  # Llamamos a la función principal
