# WORLD CRAFT ASCII: PARTE 2
![Screenshot 2022-05-16 074159](https://user-images.githubusercontent.com/104838545/168879248-7d57408b-088b-40de-9680-2e4f0b4ea44f.png) <br>

Este reto se trata de implementar un programa que asigne cree de manera aleatoria el mundo del jugador
<h2>CREACIÓN DE LOS MUROS</h2>
Esta función tiene como objetivo crear una lista de posiciones en el
mundo de 32 por 32 bloques en las que se encuentran los muros.
Ejemplo
muros=["0:2”,”1:0","1:1","1:2","2:1","2:2",”3:1”,”3:2”,”4:1”,”4:2”] <br>
• Esta pequeña lista parcial indica las posiciones en donde hay <br>
muros (primero va el numero de la fila y luego el de la columna):  <br>
![Screenshot 2022-05-17 125556](https://user-images.githubusercontent.com/104838545/168879524-8d7902f8-1745-457d-aeae-abd9cab32d69.png)
 <br>
Se debe implementar una función que recibe como entrada cuatro
listas que corresponden a: 1) lista con número de filas x, 2) lista
número de columnas, 3) lista con ancho del muro y 4) lista con largo
del muro Estas listas indican la fila y la columna en la que debe
hacerse un muro de las dimensiones dadas, es decir retornar una
lista en Python de muros como la del ejemplo anterior. <br>
![Screenshot 2022-05-17 125718](https://user-images.githubusercontent.com/104838545/168879561-9da655cb-22b5-49b1-9fe1-09c4eb33922c.png)
 <br>
