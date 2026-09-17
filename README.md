# 📊 Diseño de Datos y Algoritmos (DDYA)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

Repositorio dedicado a la resolución de guías, talleres y proyectos prácticos de la asignatura **Diseño de Datos y Algoritmos**. Incluye la implementación de estructuras de datos, algoritmos de ordenamiento y algoritmos de búsqueda en Python.

---

## 📁 Estructura del Repositorio

```text
DDYA/
├── semana 2/           # Organización de precios en mercado (Insertion Sort)
├── semana 3/           # Organización y búsqueda de productos (Merge Sort + Búsqueda Binaria)
├── semana 4/           # Catálogo y consulta eficiente de productos
└── dev-pr-dynamic/     # Desarrollo dinámico: Optimización de consultas de catálogo
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
Administración de un listado de $n$ códigos numéricos de productos que inicialmente se encuentran desordenados.
* **Algoritmos Utilizados:** *Merge Sort* y *Búsqueda Binaria*.
* **Funcionalidad:**
  * **Punto 1 (Ordenamiento con Merge Sort):** Aplica la estrategia de *Divide y Conquistar* (Dividir, Conquistar y Combinar) para ordenar los códigos de menor a mayor.
  * **Punto 2 (Búsqueda Binaria):** Realiza búsquedas eficientes $O(\log n)$ sobre la lista ordenada para verificar si un código de producto específico existe o no.

---

### 🔹 Semana 4: Catálogo y Consulta de Productos
Diseño de un sistema de catálogo estructurado para almacenar información clave de los productos: `nombre`, `categoría`, `precio` y `cantidad disponible`.
* **Funcionalidad:** Permite mantener el catálogo organizado para realizar búsquedas por criterios específicos y retornar respuestas claras sobre la disponibilidad del producto.

---

### 🔹 dev-pr-dynamic: Módulo Dinámico de Catálogo
Extensión enfocada en la optimización y flexibilidad de la estructura del catálogo de productos.
* **Funcionalidad:** Implementación de consultas dinámicas para reducir tiempos de respuesta al trabajar con volúmenes de productos variables.

---

## 🛠️ Tecnologías y Herramientas

* **Lenguaje:** [Python 3.x](https://www.python.org/)
* **Control de Versiones:** Git & GitHub

---

## 👨‍💻 Autor

* **Daniel Buitrago** — [@DanielBuitrago147](https://github.com/DanielBuitrago147)
