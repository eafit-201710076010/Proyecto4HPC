# Proyecto4HPC
Proyecto HPC ST0263

## Grupo: 

## Mateo Flórez Restrepo
## Laura Sanchez Cordoba
## Santiago Arturo Zapata Chacon

### Proyecto HPC : Finding a most likely common ancestor 

*1. Problema o caso de estudio a resolver

A través del proceso evolutivo surgen diferentes especies cuyo ADN tiene algunas similitudes, lo que puede traducirse en que, en períodos históricos previos, hubo un ancestro común del que evolucionaron. Para hallar este ancestro (la posible cadena de ADN de este) se tienen varias cadenas homólogas que se desean analizar simultáneamente de manera que se encuentren las similitudes y llegar al ancestro común más probable.

### Código de honor

Yo, Santiago Zapata Chacón, mejoré la implementación del programa con openMP seleccionando el número de threads y colocando la secciones critica para proteger la memoria y así realizar una correcta ejecución del programa. También, realicé las pruebas con los diferentes datasets para así sacar un speedUp promedio y finalmente, realicé el script que genera los datasets `test.py`.

### PCAM
[pcam.md](https://github.com/lsanchezc613/Proyecto4HPC/blob/master/pcam.md)

### Cómo ejecutar

Se requiere estar en un cluster de colfax para ejecutar los ficheros

Para ejecutar el programa deseado deberá entrar a la carpeta que lo describe [ serial, omp, mpi ]

Luego, realizar los siguientes comandos:

    $ make
    $ make queue

Finalmente observar el fichero `output.txt` que contiene la cadena ancestra definitiva. Tambien se puede observar los fichero `process_*.o*` el cual indica el tiempo de ejecución.

### Análisis de resultados

### Videos
