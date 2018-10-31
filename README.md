# Curso de Python 2018 de Platzi con David Aroesti

- [Curso de Python 2018 de Platzi con David Aroesti](#curso-de-python-2018-de-platzi-con-david-aroesti)
  - [Palabras reservadas de Python](#palabras-reservadas-de-python)
  - [Variables y expresiones](#variables-y-expresiones)
  - [Funciones](#funciones)
  - [Estructuras condicionales](#estructuras-condicionales)
  - [Strings en Python](#strings-en-python)
  - [Operaciones con Strings](#operaciones-con-strings)
  - [Slices en Python](#slices-en-python)
  - [For loops](#for-loops)

Este es un curso introductorio para aprender a programar con Python de Platzi. Es la última actualización de 2018 con David Aroesti nuevamente como profesor.

## Palabras reservadas de Python

Estas son palabras que por ningún motivo debemos usar como variables, ya que nos ocasionarán errores de compilación en Python

|Palabra|Palabra  |Palabra  |Palabra  |Palabra|
|-------|---------|---------|---------|-------|
| False | await   | else    | import  | pass  |
| None  | break   | except  | in      | raise |
| True  | class   | finally | is      | return|
| and   | continue| for     | lambda  | try   |
| as    | def     | from    | nonlocal| while |
| assert| del     | global  | not     | with  |
| async | elif    | if      | or      | yield |

## Variables y expresiones

- Una expresion (__expression__) es una combinación de valores, variables y operadores.

```python
2 + 2
```

- Un enunciado (__statement__) es una unidad de código que tiene un efecto

```python
age = 20
```

- Orden de operaciones PEMDAS
  - Paréntesis
    - Exponente
      - Multiplicación
      - División
        - Adición
        - Substracción

## Funciones

En el contexto de la programación las funciones son simplemente una agrupación de enunciados(__statments__) que tienen un nombre.

Una función tiene un nombre, debe ser descriptivo, puede tener parámetros y puede regresar un valor después que se generó el cómputo.

Python es un lenguaje que se conoce como _batteries include_ (baterías incluidas) esto significa que tiene una librería estándar con muchas funciones y librerías.

Para declarar funciones que no son las globales, las _built-in functions_, necesitamos importar un módulo.

Con el keyword `def` declaramos una función.

![Tabla de Funciones Built-In de Python](./assets/python-built-in-functions.jpg)

## Estructuras condicionales

Para comprender el flujo de nuestro programa debemos entender un poco sobre estructuras y expresiones booleanas

`==` se refiere a igualdad
`!=` no hay igualdad.
`>` mayor que
`<` menor que
`>=` mayor o igual
`<=` menor o igual

`and` unicamente es verdadero cuando ambos valores son verdaderos
`or` es verdadero cuando uno de los dos valores es verdadero.
`not` es lo contrario al valor. Falso es Verdadero. Verdadero es Falso.

![Tabla de Conditionals de Python](./assets/python-conditionals.jpg)

## Strings en Python

- Las cadenas (__strings__) son un tipo con comportamiento diferente a los _int_, _float_ y _bool_.
  - Las cadenas son secuencias
  - las secuencias se pueden acceder a través de un índice

```python
apple = 'apple'
apple[1]
```

- Las cadenas (al igual que otras secuencias) tienen una logitud
  - Para saber la longitud de una secuencia, se puede usar la función __len()__

```python
len(apple)
```

- En Python, los caracteres que componen un string se reutilizan a lo largo del programa
  - Esto ayuda a reducir la cantidad de memoria que necesita el programa
  - También significa que las strings deben ser inmutables

```python
x = 'a'
y = 'b'
id(x) == id(y)
```

## Operaciones con Strings

Los strings tienen varios métodos que nosotros podemos utilizar.

- __upper__: convierte todo el string a mayúsculas
- __lower__: convierte todo el string a minúsculas
- __find__: encuentra el indice en donde existe un patrón que nosotros definimos
- __startswith__: significa que empieza con algún patrón.
- __endswith__: significa que termina con algún patrón
- __capitalize__: coloca la primera letra en mayúscula y el resto en minúscula

__in__ y __not in__ nos permite saber con cualquier secuencia sin una subsecuencia o substrings se encuentra adentro de la secuencia mayor.

__dir__: Nos dice todos los métodos que podemos utilizar dentro de un objeto.

```python
constante_perro = 'perro'
dir(constante_perro)
```

__help__: nos imprime en pantalla el _docstrings_ o comentario de ayuda o instrucciones que posee la función. Casi todas las funciones en Python las tienen.

```python
def my_function():
    """Este es un texto de ayuda de cómo usar esta función"""
    pass
```

Ahora, al correr Python, podemos ver dicha documentación:

```python
help(my_function)
```

## Slices en Python

Los _slices_ en Python nos permiten nos permiten manejar secuencia de manera poderosa.

Al significar _rebanada_ la funcionalidad está más que dada. Los slices se usan de la siguiente manera: `secuencia[comienzo:final:pasos]`

```python
my_name = 'Alejandro'
my_name[0] # returns 'A'
my_name[-1] # returns 'o'
my_name[0:3] # returns 'Ale'
my_name[::2] # returns 'Aeado'
my_name[3:3] # returns ''
my_name[:] # returns 'Alejandro'
my_name[1:-1:2] # returns 'ljnr'
```

## For loops

Las _iteraciones_ es uno de los conceptos más importantes en la programación. En Python existen muchas manera de iterar pero las dos principales son los `for` loops y `while` loops.

Los __for__ loops nos permiten iterar a través de una secuencia y los __while__ loops nos permiten iterara hasta cuando una condición se vuelva falsa.

for loops:

- Tienen dos keywords break y continue que nos permiten salir anticipadamente de la iteración
- Se usan cuando se quiere ejecutar varias veces una o varias instrucciones.

```python
for [variable] in [secuencia]:
```

Es una convención usar la letra `i` como variable en nuestro for, pero podemos colocar la que queramos.

__range__: Nos da un objeto rango, es un iterador sobre el cual podemos generar secuencias.