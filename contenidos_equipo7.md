# Equipo 7: Algoritmos de búsqueda de patrones en cadenas

Este documento sigue el orden de los **contenidos tentativos** del PDF. Debajo de cada título va la explicación y los resultados de nuestros programas.

Archivo de código:
- `BPC.py`: el ejemplo práctico con ADN de Kaggle (los 3 algoritmos).

---

## 1. Representación y procesamiento de cadenas de caracteres

Una cadena es una secuencia de caracteres en orden, por ejemplo el ADN `ATGCCATG`. Cada carácter tiene una posición que empieza en 0.

```
posición:  0 1 2 3 4 5 6 7
cadena:    A T G C C A T G
```

Se puede guardar de dos formas:
- **Arreglo (string normal de Python):** las letras van seguidas en memoria y se llega directo a cualquier posición, por ejemplo `texto[5]`.
- **Lista enlazada:** cada letra es un nodo que apunta a la siguiente. Para llegar a la posición 5 toca recorrer desde el inicio.

En `BPC.py` el ADN se guarda como **lista enlazada simple**: cada nodo tiene una letra y apunta a la siguiente.

---

## 2. Problema de búsqueda exacta de patrones

Se tiene un **texto** de largo **n** y un **patrón** de largo **m**. Hay que encontrar todas las posiciones donde el patrón aparece exactamente igual dentro del texto.

```
texto:   A T G C C A T G C C
patrón:  A T G C C
         ↑         ↑
     posición 0  posición 5   → aparece 2 veces
```

Aplicado al ADN: buscar una secuencia de bases (por ejemplo `ATGCC`) dentro del ADN humano.

---

## 3. Algoritmo de búsqueda ingenua

**Idea:** pone el patrón en cada posición del texto y compara letra por letra. Si una letra falla, corre el patrón una posición y vuelve a empezar.

```
texto:   A T G A T G C
patrón:  A T G C          ← falla en la 4ta letra
           A T G C        ← falla en la 1ra
             A T G C      ← falla en la 1ra
               A T G C    ← ¡coincide!
```

**Problema:** cuando falla, vuelve a comparar letras que ya había revisado.

---

## 4. Algoritmo Knuth–Morris–Pratt (KMP)

**Idea:** recorre el texto **una sola vez, sin devolverse nunca**. Cuando hay un fallo, usa la **tabla de prefijos** para saber cuánto de lo que ya revisó le sirve, y sigue desde ahí.

```
texto:   A B A B A ...
patrón:  A B A B C
                 ↑ falla (A no es C)

La ingenua volvería a empezar en la posición 1.
KMP mira la tabla: ya tiene "AB" que es igual al inicio del patrón,
entonces corre el patrón y sigue comparando sin devolverse en el texto:

texto:   A B A B A ...
patrón:      A B A B C
                 ↑ sigue aquí
```

---

## 5. Construcción y funcionamiento de la tabla de prefijos

### Qué es

En cada posición del patrón, la tabla dice **cuántos números del principio del patrón se acaban de repetir**.

Ejemplo pequeño:

| Posición | Lo que va hasta ahí | Comienzo que se repite al final | Tabla |
|---|---|---|---|
| 0 | A | nada | 0 |
| 1 | AB | nada | 0 |
| 2 | ABA | **A** | 1 |
| 3 | ABAB | **AB** | 2 |
| 4 | ABABC | nada | 0 |

### Construcción

Se usa un contador `k` que guarda cuántos van iguales al comienzo:
1. Si el número actual es igual a `patron[k]`, se suma 1 a `k`.
2. Si es diferente, `k` se devuelve con `k = tabla[k - 1]` hasta que coincida o llegue a 0.
3. Se guarda `k` en la tabla.

### Funcionamiento

Cuando KMP falla después de haber coincidido varias letras, mira la tabla en la posición anterior al fallo. Ese número le dice desde dónde seguir en el patrón, sin devolverse en el texto.

---

## 6. Algoritmo Rabin–Karp y utilización de hashing de cadenas

**Idea:** convierte el patrón en un número (hash) y cada ventana del texto también. Primero compara números, y solo si son iguales compara letra por letra.

**Hash rodante:** para pasar a la siguiente ventana no se recalcula todo, solo se quita la letra que sale y se agrega la que entra:

```
hash_nuevo = (base * (hash_viejo - letra_que_sale * h) + letra_que_entra) % primo
```

donde `h = base^(m-1) % primo`.

Con lista enlazada usa **dos punteros** que avanzan juntos:

```
A → T → G → C → C → A → T → ...
↑                   ↑
sale                entra
```

No necesita lista doble porque nunca se devuelve.

---

## 7. Comparación del número de operaciones realizadas

### Con el ADN humano real de Kaggle (`BPC.py`, 4.380 secuencias, 5.534.562 letras, patrón `ATGCC`)

| Algoritmo | Encontrados | Comparaciones |
|---|---|---|
| Ingenua | 7.323 | 7.356.422 |
| KMP | 7.323 | 6.929.398 |
| Rabin-Karp | 7.323 | 120.608 |

Rabin-Karp hace muchas menos comparaciones de letras porque primero compara los hash.

---

## 8. Complejidad temporal y espacial de los algoritmos

n = largo del texto, m = largo del patrón.

| Algoritmo | Mejor caso | Peor caso | Espacio |
|---|---|---|---|
| Ingenua | O(n) | O(n · m) | O(1) |
| KMP | O(n + m) | O(n + m) | O(m) por la tabla |
| Rabin-Karp | O(n + m) | O(n · m) si muchos hash coinciden | O(1) |

Si la tabla de prefijos se guarda en lista enlazada, construirla pasa de O(m) a O(m²).

---

## 9. Aplicaciones en búsqueda de texto y procesamiento de secuencias

- **Ctrl + F** en editores de texto y navegadores.
- **ADN y bioinformática:** buscar genes o secuencias dentro de un genoma (nuestro ejemplo práctico).
- **Antivirus:** buscan firmas de virus dentro de los archivos.
- **Detección de plagio:** Rabin-Karp compara muchos pedazos de texto usando hash.
- **Filtros de spam y búsqueda en bases de datos.**

---

## Conclusión

- Los tres algoritmos encuentran lo mismo; cambia cuánto trabajo hacen.
- **KMP** nunca se devuelve en el texto gracias a la tabla de prefijos.
- **Rabin-Karp** compara números antes que letras y casi no hace comparaciones de más.
- **Arreglo vs lista enlazada:** la lista enlazada funciona, pero nunca gana. Donde más pierde es en la tabla de prefijos, porque ahí hay que saltar a posiciones.
