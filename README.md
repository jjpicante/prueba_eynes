# Ref: Developer Exercises

Cree un repositorio de git y dentro de ese repositorio cree carpetas según el nombre del ejercicio. Por
cada ejercicio, generar un branch nuevo con el nombre del ejercicio, commitear los subsecuentes
avances y cuando el ejercicio esté terminado mergear a master. Subir ese repositorio a algún sitio (github,
bitbucket). Al finalizar responder al correo del cual le fue enviado este documento informando la url del
repositorio.

- En lo posible proveer DocTests (https://docs.python.org/3/library/doctest.html) o algún otro
mecanismo de testeo

- En lo posible usar Python 3

## Nombre: Simple

### Descripción

Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10 elementos. Retornar la lista.

Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.

## Nombre: Matriz

### Descripción

Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.

## Nombre: Clases

### Descripción

Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.

Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.

Si printeamos el objeto creado debe mostrarse una representación amigable.

El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.

Permitir la multiplicación del círculo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0.


