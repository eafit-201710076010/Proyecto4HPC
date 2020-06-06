# Proyecto4HPC
Proyecto HPC ST0263

## Grupo: 

## Mateo Flórez Restrepo
## Laura Sanchez Cordoba
## Santiago Arturo Zapata Chacon

### Proyecto HPC : Finding a most likely common ancestor 

### Código de honor

Yo, Laura Sánchez Córdoba confirmo que este trabajo ha sido realizado de manera original por cada uno de los miembros del equipo, basados en el siguiente problema: http://rosalind.info/problems/cons/. Por mi parte, mi participación fue en la implementación de la primera versión del código usando OpenMP, analizando las tareas (en este caso específico, los ciclos) que podían ser paralelizados según la metodología PCAM, que fue un trabajo conjunto; además llevé a cabo la elaboración del makefile.

Yo, Santiago Zapata Chacón, mejoré la implementación del programa con openMP seleccionando el número de threads y colocando la secciones critica para proteger la memoria y así realizar una correcta ejecución del programa. También, realicé las pruebas con los diferentes datasets para así sacar un speedUp promedio y finalmente, realicé el script que genera los datasets `test.py`.

Yo, Mateo Flórez Restrepo realicé el análisis general del problema que permitió definir la solución de este, el pseudo-código y la posterior implementación serial, donde con esta pudiese leer los datasets y convertirlos en una matriz para poder realizar el procesamiento. Además, me encargué de la medición y realización de pruebas de tiempo.

### Descripción

#### 1. Problema o caso de estudio a resolver

A través del proceso evolutivo surgen diferentes especies cuyo ADN tiene algunas similitudes, lo que puede traducirse en que, en períodos históricos previos, hubo un ancestro común del que evolucionaron. Para hallar este ancestro (la posible cadena de ADN de este) se tienen varias cadenas homólogas que se desean analizar simultáneamente de manera que se encuentren las similitudes y llegar al ancestro común más probable.

#### 2. Objetivo y alcance

**Objetivo:** 
Las cadenas homólogas de ADN se encuentran dispuestas en una matriz indicando las bases nitrogenadas que las componen, para analizar estas similitudes de la manera más eficiente, se propone la paralelización para hallar cuales son las bases que más se repiten al sumarlas por columnas. De los mayores valores calculados al final, se hallará la cadena del ancestro.   

**Alcance:** 
Paralelizar las columnas de las cadenas ADN cuyo resultado sea más veloz que la implementación secuencial a la hora de hallar el ancestro común.

#### 3. Requerimientos técnicos

- Lenguaje programación: C++
- Framework de paralelización OMP y/o MPI
- Cluster HPC Colfax (Opción: procesador Intel Xeon Phi processor 7210 with 4-way hyper-threading)

#### 4. Plan de Trabajo 

| Plan de trabajo |
| --------------- |
| Análisis y diseño del problema |
| Implementación secuencial de la solución |
| Diseño paralelización, evaluación speed up |
| Agregar procesamiento paralelo a la implementación (Memoria compartida) utilizando cluster Colfax |
| Evaluación de resultados |


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
A continuación se muestran tablas de los resultados tras medir el tiempo de ejecución del algoritmo de forma serial y paralelizada con OpenMP con datasets de diferentes tamaños (se recalca que estos datasets contienen cadenas de ADN), además se adjunta el cálculo del SpeedUp y Otra tabla que indica la eficiencia del algoritmo según el número de hilos usados.

### Tiempos de Ejecución

| Datasets | Longitud ADN | Tiempo Serial | Tiempo OMP | SpeedUp |
| -------- | ------------ | ------------- | ---------- | ------- |
| Datasets 1,2,3 | 10000 | 22.786246 | 5.701938 | 3.99622 |
| Datasets 4,5,6 | 8000 | 13.763690 | 3.438240 |  4.00312 |
| Datasets 7,8,9 | 7000 | 12.898869 | 3.380041 | 3.81618 |
| Datasets 10,11,12 |5000 | 8.502806 | 2.596404 | 3.27483 |
|        |        |        | **SpeedUp Promedio** | **3.77258** |     

#### Eficiencia

| Hilos | Tiempo OMP | Speed up | Eficiencia |
| ----- | ---------- | -------- | ---------- |
| 1 | 50.423577 | 0.45189 | 0.45189 |
| 8 | 12.701559 | 1.79397 | 0.22424 |
| 32 | 6.586549 | 3.45951 | 0.10810 |
| 64 | 5.701938 | 3.99622 | 0.06244 |
| 128 | 5.343405 | 4.26436 | 0.03331 |
| 256 | 5.236814 | 4.35116 | 0.01699 |

#### Gráficos

##### Tiempos Seriales tras la ejecución del algoritmo con diferente cantidad de cadenas

![](http://imgfz.com/i/MpP60g3.png)

##### Tiempos usando OMP tras la ejecución del algoritmo con diferente cantidad de cadenas


![](http://imgfz.com/i/HbejoRS.png)

Si bien el comportamiento es el mismo se puede ver la gran disminución entiempos de ejecución.

### Videos

[Santiago Arturo Zapata Chacón](https://youtu.be/NeIknaStScE)

[Laura Sánchez Córdoba](https://web.microsoftstream.com/video/86f3e95f-a981-4055-82ae-c62b087648e4)
