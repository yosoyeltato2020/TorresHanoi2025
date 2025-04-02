def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")
    else:
        if n > 1:
            # Mover n-1 discos de origen a auxiliar usando destino como apoyo
            hanoi(n-1, origen, destino, auxiliar)
            print(f"Mover disco de {origen} a {destino}")
            # Mover n-1 discos de auxiliar a destino usando origen como apoyo
            hanoi(n-1, auxiliar, origen, destino)

# Ejemplo con 3 discos
hanoi(3, 'A', 'B', 'C')

