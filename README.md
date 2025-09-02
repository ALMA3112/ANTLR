# Calculadora ANTLR

Una calculadora de expresiones matemáticas implementada usando ANTLR4 para el análisis sintáctico. Este repositorio contiene dos implementaciones: una en **Java** y otra en **Python**.

##  Características

### Versión Java
- Operaciones básicas: suma, resta, multiplicación, división
- Funciones trigonométricas: `sin`, `cos`, `tan`
- Funciones matemáticas: `sqrt`, `ln`, `log`, `rad`, `deg`
- Factorial (`!`)
- Variables y asignación
- Paréntesis para precedencia
- Soporte para números decimales

### Versión Python
- Operaciones básicas: suma, resta, multiplicación, división
- Funciones trigonométricas: `sin`, `cos`, `tan`
- Funciones matemáticas: `sqrt`, `ln`, `log`, `pow`, `max`, `min`
- Variables y asignación
- Paréntesis para precedencia
- Manejo de errores (división por cero)

##  Requisitos

### Para Java
- Java 8 o superior
- ANTLR 4.x
- JAR de ANTLR runtime

### Para Python
- Python 3.6 o superior
- ANTLR4 Python runtime: `pip install antlr4-python3-runtime`

##  Instalación y Uso

### Versión Java

1. **Generar el parser y lexer:**
   ```bash
   antlr4 -visitor LabeledExpr.g4
   javac -cp ".:antlr-4.x.x-complete.jar" *.java
   ```

2. **Ejecutar:**
   ```bash
   java -cp ".:antlr-4.x.x-complete.jar" Main
   ```

3. **Ejemplo de uso:**
   ```
   Calculadora 
   x = 5
   y = 3
   x + y * 2
   11.00
   sin(45)
   0.85
   sqrt(16)
   4.00
   5!
   120.00
   ```

### Versión Python

1. **Generar el parser y lexer:**
   ```bash
   antlr4 -Dlanguage=Python3 -visitor LabeledExpr.g4
   ```

2. **Ejecutar:**
   ```bash
   python main.py
   ```

3. **Ejemplo de uso:**
   ```
   Escribe expresiones (Ctrl+D para terminar):
   x = 10
   y = 5
   x + y
   15.0
   pow(2, 3)
   8.0
   max(10, 20, 5)
   20.0
   ```

##  Sintaxis Soportada

### Operadores
- `+` - Suma
- `-` - Resta  
- `*` - Multiplicación
- `/` - División

### Funciones (Java)
- `sin(x)` - Seno (en grados)
- `cos(x)` - Coseno (en grados)
- `tan(x)` - Tangente (en grados)
- `sqrt(x)` - Raíz cuadrada
- `ln(x)` - Logaritmo natural
- `log(x)` - Logaritmo base 10
- `rad(x)` - Grados a radianes
- `deg(x)` - Radianes a grados

### Funciones (Python)
- `sin(x)` - Seno (en radianes)
- `cos(x)` - Coseno (en radianes)
- `tan(x)` - Tangente (en radianes)
- `sqrt(x)` - Raíz cuadrada
- `ln(x)` - Logaritmo natural
- `log(x)` - Logaritmo base 10
- `pow(x, y)` - x elevado a la y
- `max(x, y, ...)` - Valor máximo
- `min(x, y, ...)` - Valor mínimo

### Otros
- `!` - Factorial (solo Java)
- Variables: `variable = expresion`
- Paréntesis para agrupar: `(expresion)`

##  Gramática ANTLR

Las gramáticas definen la sintaxis del lenguaje:

- **Java**: Soporta factorial como operador postfijo y signos unarios
- **Python**: Soporta múltiples argumentos en funciones y manejo de líneas vacías

## Ejemplos de Uso

### Cálculos Básicos
```
2 + 3 * 4
# Resultado: 14.00
```

### Variables
```
pi = 3.14159
radio = 5
area = pi * radio * radio
# Resultado: 78.54
```

### Funciones Trigonométricas
```
# Java (grados)
sin(30)
# Resultado: 0.50

# Python (radianes)  
sin(1.5708)
# Resultado: 1.0
```

##  Limitaciones

- **Java**: Las funciones trigonométricas trabajan en grados
- **Python**: Las funciones trigonométricas trabajan en radianes
- **Java**: Solo soporta factorial para números enteros
- **Python**: No implementa factorial
- División por cero genera error en Python, pero no está manejada en Java
