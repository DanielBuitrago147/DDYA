# 📊 Diseño de Datos y Algoritmos (DDYA)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

Repositorio dedicado a la resolución de guías, talleres, parciales y proyectos prácticos de la asignatura **Diseño de Datos y Algoritmos**. Incluye la implementación manual de estructuras de datos lineales (listas, pilas, colas), no lineales (árboles BST y AVL, grafos) y algoritmos de búsqueda y ordenamiento en Python.

---

## 📁 Estructura del Repositorio

```text
DDYA/
├── semana 2/                      # Organización de precios en mercado (Insertion Sort)
├── semana 3/                      # Organización y búsqueda de productos (Merge Sort + Búsqueda Binaria)
├── semana 4/                      # Catálogo y consulta eficiente de productos
├── semana 7/                      # Sistema de atención: Colas, Pilas y Listas Doblemente Enlazadas
├── semana 8/                      # Organización de códigos mediante Árboles (BST y AVL)
├── semana 9/                      # Recorrido de red de distribución mediante Grafos (BFS y DFS)
├── dev-pr-dynamic/                # Desarrollo dinámico: Optimización de consultas de catálogo
└── parcial-grafos-red-transporte/ # Evaluación práctica: Implementación de Red de Distribución con Grafos
```

---

## 📝 Detalle de las Problemáticas y Ejercicios

### 🔹 Semana 2: Organización de Precios en Mercado
Una tienda necesita organizar los precios de sus productos según la cantidad $n$ indicada por el usuario.
* **Algoritmo Utilizado:** *Insertion Sort*.
* **Funcionalidad:**
  * **Punto 1 (Orden Ascendente):** Ordena los precios del menor al mayor para mostrar primero los productos más económicos.
  * **Punto 2 (Orden Descendente):** Ordena los precios del mayor al menor para destacar primero los productos más costosos.

---

### 🔹 Semana 3: Organización y Búsqueda de Productos
Administración de un listado de $n$ códigos numéricos de productos desordenados.
* **Algoritmos Utilizados:** *Merge Sort* y *Búsqueda Binaria*.
* **Funcionalidad:**
  * **Punto 1 (Ordenamiento con Merge Sort):** Aplica la estrategia *Divide y Conquistar* para ordenar los códigos de menor a mayor.
  * **Punto 2 (Búsqueda Binaria):** Búsqueda eficiente $O(\log n)$ sobre la lista ordenada para verificar la existencia de un código.

---

### 🔹 Semana 4: Catálogo y Consulta de Productos
Diseño de un sistema de catálogo estructurado para almacenar información clave (`nombre`, `categoría`, `precio` y `cantidad disponible`).
* **Funcionalidad:** Organización del catálogo para realizar búsquedas por criterios específicos y retornar resultados de disponibilidad.

---

### 🔹 Semana 7: Sistema de Atención de una Tienda
Control de atención a clientes, registro de operaciones y administración del catálogo utilizando tres estructuras de datos fundamentales:
* **Estructuras Utilizadas:** Colas (FIFO), Pilas (LIFO) y Listas Doblemente Enlazadas.
* **Funcionalidad:**
  * **Punto 1 (Cola de Clientes):** Atención en orden de llegada (agregar a cola, atender cliente, mostrar clientes en espera).
  * **Punto 2 (Pila de Operaciones):** Historial de clientes atendidos. Permite visualizar el último atendido y deshacer la última atención (retirando de la pila y regresando al cliente al inicio de la cola).
  * **Punto 3 (Lista Doblemente Enlazada):** Catálogo de productos (`código`, `nombre`, `precio`) con navegación bidireccional (primer a último y viceversa), inserción al final, búsqueda y eliminación por código.

---

### 🔹 Semana 8: Organización de Códigos mediante Árboles
Comparación entre estructuras jerárquicas no balanceadas y balanceadas para organizar códigos de bodega.
* **Estructuras y Algoritmos:** Árbol Binario de Búsqueda (BST) y Árbol AVL (con cálculo de factor de balance y rotaciones simples/dobles).
* **Funcionalidad:**
  * **Punto 1 (BST):** Construcción e inserción exacta sin reordenar ni balancear.
  * **Punto 2 (Árbol AVL):** Balanceo dinámico tras cada inserción mediante rotaciones (Izquierda, Derecha, Doble Izq-Der, Doble Der-Izq).
  * **Puntos 3, 4 y 5 (Recorridos Recursivos):** Implementación de recorridos *Preorden* (Raíz-Izq-Der), *Inorden* (Izq-Raíz-Der) y *Postorden* (Izq-Der-Raíz).
  * **Visualización:** Renderizado gráfico de los árboles (usando librerías como `matplotlib` / `networkx`) para comparación visual entre BST y AVL.

---

### 🔹 Semana 9: Recorrido de una Red de Distribución
Modelado de una red de mensajería no dirigida con centros de distribución (vértices) y carreteras (aristas).
* **Estructura y Algoritmos:** Grafos mediante Lista de Adyacencia, *BFS* (Breadth-First Search con Colas) y *DFS* (Depth-First Search con Pila/Recursión).
* **Funcionalidad:**
  * **Punto 1 (Grafo):** Representación de centros (`A`-`G`) y sus conexiones directas.
  * **Punto 2 (BFS):** Exploración por niveles comenzando desde un centro principal (`A`).
  * **Punto 3 (DFS):** Inspección en profundidad a través de la red.
  * **Punto 4 (Punto Inicial Personalizado):** Permite al usuario seleccionar el nodo de origen.
  * **Punto 5 (Búsqueda BFS de Rutas):** Rastreo del camino más corto en cantidad de conexiones entre dos nodos.
  * **Punto 6 (Dinámico):** Agregar nuevos centros (nodos) y conexiones (aristas) bidireccionales en tiempo de ejecución.

---

### 🔹 parcial-grafos-red-transporte: Evaluación Práctica de Red de Distribución
Implementación y resolución práctica enfocada en el modelado de redes de transporte y distribución con grafos no dirigidos, rutas óptimas con BFS, recorridos DFS y expansión dinámica de nodos.

---

### 🔹 dev-pr-dynamic: Módulo Dinámico de Catálogo
Extensión enfocada en la optimización y flexibilidad de la estructura del catálogo de productos para reducir tiempos de respuesta ante volúmenes de datos variables.
