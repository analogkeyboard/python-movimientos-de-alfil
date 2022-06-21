import os

print("Programa para calcular el movimiento de la pieza alfil en el tablero de ajedrez.\n")
columnas=8


# se crea la matriz de tamaño 8x8 definido en la variablcolumnas
# usando la sintaxis de compresion de listas

v=[[0]*columnas for _ in range(columnas)]


print("Contenido de la matriz creada:",v)
print("\n")

# visualizacion de la matriz con los indices i,j de cada posicion
for i in range(columnas):
    
    for j in range(columnas):
         print(str(i)+","+str(j),end="\t")
    print("\n")
    
print("\n")

# introduccion de datos por parte del usuario
# el cual introducira la posicion deseada de i y j

pos_i=int(input("Indice i: "))
pos_j=int(input("Indice j: "))
# pos_i=4 
# pos_j=3

# matriz generada con los datos ingresados

# si los indices ingresados estan fuera de los limites de la matriz entonces
# muestra un mensaje de error al usuario
if pos_i>=0 and pos_i<=len(v)-1 and pos_j>=0 and pos_j<=len(v)-1:

    for i in range(columnas):
        
        for j in range(columnas):
        
        # cada posicion se llena con las iniciales B y N 
        # donde B es para blancas y N para negras
        # esto se logra identificando la suma de los indices
        # si la suma es par entonces sera blanca en caso contrario sera negra
            if (i+j)%2==0:
                v[i][j]='░░░'
            else:
                v[i][j]='███'
            
            # verificamos que los indices ingresados indiquen la posicion inicial del alfil
            # el caracter A es solo para representar la pieza
            if i==pos_i and j==pos_j:
                v[pos_i][pos_j]=' A '
                
                    
            #matriz identidad
            # si la matriz es de un tamaño cuadrado
            # entonces tendra una diagonal con ambos indices iguales
            # si los indices ingresados son parte de la diagonal entonces se marcara con un asterisco
            elif (i==j) and pos_i==pos_j:
                v[i][j]=' * '
        
            
            # matriz diagonal derecha
            elif (i+j)==(pos_i+pos_j):
                v[i][j]=' * '
           
            # matriz diagonal izquierda cuando la suma de los indices
            # son par o impar
            elif ((i+j)%2==1 or  (i+j)%2==0) and  (pos_i-pos_j)==i-j:
                
                v[i][j]=' * '
        
                    
            # imprime los valores de la matriz
            # se le agrega el end="" para que imprima en horizontal
           
            print(v[i][j],end="")
        
        # salto de linea para cada renglon
        print("")
else:
    
    print("indices fuera del limite")
    os.system("pause")