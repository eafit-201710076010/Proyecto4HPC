# Metodología PCAM

## 1. Diseño del problema

El objetivo del problema es encontrar el ancestro común más probable a partir del análisis evolutivo de un conjunto de 
datos donde se halla el ancestro común entre las cadenas de ADN de ciertas especies que se encuentran en cada dataset, 
la salida de los datasets permitirá posteriormente buscar la cadena de ADN más probable de un ancestro previo a los hallados.

**![](http://imgfz.com/i/F7yCrWh.png)**

**Dominio:** Datasets de formato .txt con las cadenas de ADN

**Rango:** Cadena del ancestro común más probable

## 2. Modelación (matemática/algorítmica del problema)

**![](http://imgfz.com/i/RYjy9iW.png)**

**Solución serial:** 

Se puede observar dada la complejidad del algoritmo que el cálculo de hallar la cadena del ancestro común
toma demasiado tiempo por cada dataset (teniendo en cuenta que son cadenas muy largas, puestas en un formato
matriz que debe recorrerse por completo) y este proceso debe repetirse nuevamente con los ancestros ya calculados.

La complejidad actual del algoritmo total seria O(m*n^2) siendo m la cantidad de datasets administrados.

## 3. Fases de PCAM
	
###	3.1. Partitioning:

**T1:** Cargar m datasets.

**T2:** Llenar una matriz por cada dataset.

**T3:** Crear la matriz de resultados (consensus).

**T4:** Por cada dataset, se invoca la función que retorna el ancestro más común.

**T5:** Dentro de la función, creamos un vector por cada base nitrogenada.

**T6:** Recorremos la matriz sumando la cantidad de bases nitrogenadas por columna y colocar
resultado a cada columna del vector correspondiente.

**T7:** Al tener los vectores de base nitrogenada completos, calculamos el consenso que es la
moda de los datos de cada columna de todos los vectores.

**T8:** Creamos una matriz con cada consenso.

**T9:** Se ejecuta nuevamente la función del ancestro más común con la matriz anterior.

**T10:** Se imprime la cadena del ancestro de los ancestros más común.

### 3.2. Communication:

**![](http://imgfz.com/i/DHeOdIa.png)**

### 3.3. Aglomeration:

**Data replication:** [T5], [T6], [T7], [T9] se ejecutan en múltiples hilos (OMP)

**Process replication:** [T1], [T2], [T4] se ejecutan en múltiples procesadores (MPI)

**Serial task:** [T3],[T8],[T10] se ejecutan una sola vez en toda la implementación.

### 3.4. Mapping

#### Modelo Master/Slave

**![](http://imgfz.com/i/gP4A3vb.png)**

**Síncrono:** El nodo master crea los nodos esclavos y a cada uno se le asigna un dataset respectivamente y espera que sean procesados.
Tras recibir los ancestros comunes de cada dataset se recolectan estos y se procesan para hallar un ancestro final más probable y se muestra
al final su cadena de ADN. 

**Asíncrono:** Cada nodo esclavo se encarga de procesar individualmente el dataset y hallar el ancestro comùn de las cadenas de ADN 
procesadas y, posteriormente las envía. 



