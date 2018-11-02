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
  - [Decoradores](#decoradores)
    - [__Args y kwargs__](#args-y-kwargs)
  - [Programación orientada a objetos](#programaci%C3%B3n-orientada-a-objetos)

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

## Decoradores

__Programación por procesos__: Esta técnica consiste en basarse de un número muy bajo de expresiones repetidas, englobarlas todas en un procedimiento o función y llamarlo cada vez que tenga que ejecutarse.

__Python__ es un lenguaje que acepta diversos paradigmas como _programación orientada a objetos_ y la _programación funcional_, siendo estos los temas de nuestro siguiente módulo.

- Los __decoradores__ son una función que envuelve a otra función para modificar o extender su comportamiento.

- En __Python__ las funciones son ciudadanos de primera clase, _first class citizen_, esto significan que las funciones pueden recibir funciones como parámetros y pueden regresar funciones. Los decoradores utilizan este concepto de manera fundamental.

```python
def lower_case(func):
    def wrapper():
        # Execute code before
        result = func()
        # Execute code after
        return result

    return wrapper
```

__Otro concepto de decoradores__: sirven para ejecutar lógica del código antes y/o después de otra función, esto nos ayuda a generar funciones y código que pueda ser reutilizado fácilmente sin hacer más extenso nuestro código. Hay que recordar que si se genera una función dentro de otra, solo existirá en ese _scope_(dentro de la función padre), si se quiere invocar una función varias veces dentro de otras se tiene que generar de manera global.

### __Args y kwargs__

Pasan tal cual los valores de los argumentos que se le dan a la función. Los __args__ hacen referencia a _listas_ y los __kwargs__ a elementos de un _diccionario_ (llave: valor). Por ejemplo:

Ejemplo de __args__

```python
def test_value_args(n_arg, *args):
    print(f'First normal value: {n_arg}')

    for arg in args:
        print(f'This is one of the *args values: {arg}')

    print(type(args)) # tuple
    print(type(n_arg)) # str


if __name__ == '__main__':
    test_value_args('jesus', 'eloisa', 'tiana', 'aleisa', 'jana')
```

- El tipo de valor es una tupla
- Son convertidos los argumentos separados por _coma_

Ejemplo de __kwargs__

```python
def test_value_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f'{key} == {value}')

    print(type(kwargs)) # dict


if __name__ == '__main__':
    test_value_kwargs(family1 = 'Romero', family2 = 'Camarillo')
```

Ejemplo de __args y kwargs__

```python
def test_value_args_kwargs(*args, **kwargs):
    print(type(args)) # tuple
    print(args) # ('jesus', 'eloisa')
    print('*' * 50) # **************************************************
    print(type(kwargs)) # dict
    print(kwargs) # {'family': 'Romero Camarillo', 'city': 'Huajuapan'}


if __name__ == '__main__':
    test_value_args_kwargs('jesus', 'eloisa', family = 'Romero Camarillo', city = 'Huajuapan')
```

## Programación orientada a objetos

La programación orientada a objetos es un _paradigma de programación_ que otorga los medios para estructurar programas de tal manera que las propiedades y comportamientos estén envueltos en objetos individuales.

Para poder entender cómo modelar estos objetos tenemos que tener claros cuatro principios:

- __Encapsulamiento__: cada objeto tiene sus propias funciones, y datos sin afectar a otros, son lógica interna.
- __Abstracción__: el usuario podrá interactuar con el objeto sin necesidad de conocer toda la lógica del mismo.
- __Herencia__: si se declara un método en una clase todas las subclases heredan ese método, es decir: si tu declaras un método “imprime” que ejecute un print en una clase, las subclases podrán usar el método imprime, sin necesidad de declararlo en cada una.
- __Polimorfismo__: usando el ejemplo anterior, en cada subclase se puede modificar el método “imprime” por lo tal cada sub clase contara con un método imprime pero acorde a las necesidades de cada subclase.

Todos los objetos son una instancia de una clase. Las _clases_ simplemente nos sirven como un molde para poder generar diferentes instancias.

Los tipos básicos de Python (str, int, bool, etc.) están diseñados para representar cosas simples. Cuando requerimos crear estructuras más complejas (por ejemplo, un avión), podemos entonces utilizar clases.

La instancia, es el objeto concreto con valores reales.

Ejemplo de __class__

```python
class Airplane:
    def __init__(self, passengers, seats, pilots=[]):
        self.passengers = passengers
        self.seats = seats
        self._pilots = pilots

        def takeoff(self):
            pass

    airplain = Airplane(passengers=20, seats=30, pilots=['Tom', 'Billy'])
    airplain.passengers = 31
    airplain.takeoff()
```

__NOTAS!__: para declara una clase en __Python__ utilizamos la keyword class, después de eso le damos el nombre. Una convención en Python es que todas las clases empiecen con _mayúscula_ y se continua con _CamelCase_.

Un método fundamental es _dunder init_(`__init__`). Lo único que hace es inicializar la clase basado en los parámetros que le damos al momento de construir la clase.

`self` es una referencia a la clase. Es una forma interna por la que podemos acceder a las propiedades y métodos.