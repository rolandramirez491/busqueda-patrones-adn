# Búsqueda de patrones en cadenas de ADN

## Descripción

Proyecto del Equipo 7 para la materia Estructura de Datos (Parcial 3).

El problema es encontrar una secuencia corta de letras (el **patrón**) dentro de una cadena muy larga (el **texto**). Como ejemplo práctico se busca un patrón de bases (A, C, G, T) dentro del ADN humano, que tiene más de 5 millones de letras.

El objetivo es implementar y comparar tres algoritmos de búsqueda de patrones:

- Búsqueda ingenua
- Knuth–Morris–Pratt (KMP), con su tabla de prefijos (función de fracaso)
- Rabin–Karp, con hashing de cadenas

y ver cuántas comparaciones hace cada uno para encontrar lo mismo.

## Dataset

**DNA Sequence Dataset** de Kaggle:
https://www.kaggle.com/datasets/nageshsingh/dna-sequence-dataset

Trae secuencias de ADN de humano, chimpancé y perro. Se usa el archivo `human.txt`:

- 4.380 secuencias de ADN humano
- 5.534.562 letras en total
- Cada línea tiene la secuencia y su clase separadas por una tabulación

El archivo `human.txt` ya viene incluido en el repositorio, en la misma carpeta que `BPC.py`.

## Tecnologías

- Python 3
- Librerías que ya vienen con Python (no hay que instalar nada):
  - `os`: para limpiar la pantalla y activar los colores en la terminal
  - `time`: para las pausas entre movimientos
  - `random`: para mostrar un fragmento al azar del ADN

## Implementación

Todo se hizo con **listas enlazadas**:

- **`nodo` y `ListaADN`**: el ADN se guarda en una lista enlazada simple, donde cada nodo tiene una letra y apunta a la siguiente.
- **`nodoDoble` y `TablaPrefijos`**: la tabla de prefijos de KMP se guarda en una lista doblemente enlazada. Para llegar a una posición se empieza por el lado más cercano (el primero o el último), así se recorre como máximo la mitad.
- **`Buscador`**: tiene los tres algoritmos.

**Búsqueda ingenua:** desde cada letra del ADN prueba si ahí empieza el patrón, comparando letra por letra. Si una falla, corre el patrón una posición.

**KMP:** primero construye la tabla de prefijos comparando el patrón contra sí mismo. Cada valor dice cuántas letras del comienzo del patrón se repiten hasta esa posición. Después recorre el ADN una sola vez sin devolverse: cuando falla, usa la tabla para saber desde dónde seguir.

**Rabin–Karp:** convierte el patrón y cada ventana del ADN en un número (hash). Solo compara letra por letra cuando los hash son iguales. Para pasar a la siguiente ventana usa el hash rodante: quita la letra que sale y mete la que entra, con dos punteros sobre la lista enlazada.

```
hash = (hash * base + letra) % primo                       base = 256, primo = 101
hash_nuevo = (base * (hash_viejo - letra_que_sale * h) + letra_que_entra) % primo
h = base^(m - 1) % primo
```

| Algoritmo | Complejidad temporal | Espacio extra |
|---|---|---|
| Ingenua | O(n · m) en el peor caso | O(1) |
| KMP | O(n + m) | O(m) por la tabla |
| Rabin–Karp | O(n + m) en promedio, O(n · m) en el peor caso | O(1) |

(n = largo del ADN, m = largo del patrón)

## Ejecución

1. Tener `human.txt` en la misma carpeta que `BPC.py` (ya viene en el repositorio).
2. Correr:

```bash
python BPC.py
```

3. El programa muestra un fragmento al azar del ADN: se selecciona el patrón con el mouse y se presiona Enter.
4. Elegir una opción del menú:

```
======= BUSQUEDA DE PATRONES EN ADN =======
1. Ver tabla de prefijos
2. Busqueda ingenua
3. KMP
4. Rabin-Karp
5. Cambiar patron
```

- La opción 1 muestra cómo se construye la tabla de prefijos paso a paso.
- Las opciones 2, 3 y 4 muestran la fórmula del algoritmo, los 10 primeros y los 20 últimos movimientos hasta encontrar el patrón, y el resultado final.
- Los resultados se van acumulando arriba del menú para compararlos.

Para cerrar el programa se usa `Ctrl + C` o se cierra la ventana.

## Resultados

Búsqueda en todo el ADN humano (5.534.562 letras):

**Patrón `GTTTGTGA`:**

| Algoritmo | Veces encontrado | Comparaciones |
|---|---|---|
| Ingenua | 96 | 7.319.438 |
| KMP | 96 | 6.987.056 |
| Rabin–Karp | 96 | 73.928 |

**Patrón `ATGCC`:**

| Algoritmo | Veces encontrado | Comparaciones |
|---|---|---|
| Ingenua | 7.323 | 7.356.422 |
| KMP | 7.323 | 6.929.398 |
| Rabin–Karp | 7.323 | 120.608 |

- Los tres algoritmos encuentran el patrón las mismas veces; lo que cambia es el trabajo que hacen.
- **Rabin–Karp** hace muchas menos comparaciones de letras (casi 100 veces menos) porque primero compara los hash, y solo revisa letras cuando los hash coinciden.
- **KMP** hace menos comparaciones que la ingenua porque nunca se devuelve en el texto. La diferencia es pequeña en el ADN porque los patrones casi no se repiten consigo mismos, y la tabla de prefijos queda casi toda en 0.

## Autores

- Roland Ramírez Patiño
