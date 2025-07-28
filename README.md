# Infix-To-Postfix-with-Python

El siguiente programa es un algoritmo que primero lee el archivo "Expresiones.txt", donde se encuentran varias expresiones matemáticas escritas en notación infix (infija), separadas por saltos de línea.
Luego, el programa valida que cada expresión esté correctamente escrita, incluyendo el balanceo de paréntesis y el uso adecuado de los operadores.
Una vez validadas, las expresiones infix se convierten a notación postfix (postfija) y posteriormente se evalúan para calcular su resultado numérico.

En la division de trabajo Ruddy Cuyan - 1360324 se encargo del integrante A y  se encargo del integrante B:

1. Integrante A (Ruddy Cuyan - 1360324) – Conversión de Infix → Postfix
Responsabilidades:
- Leer la expresión infix desde el archivo expresiones.txt.
- Validar la expresión con expresiones regulares (regex).
- Usar el algoritmo Shunting Yard (de Dijkstra) para convertir la expresión infix a postfix.
- Guardar la expresión postfix para que el otro integrante pueda evaluarla.

2. Integrante B – Evaluación de la Expresión Postfix
Responsabilidades:
- Recibir la expresión postfix (generada por su compañero).
- Evaluar la expresión usando una pila (stack):
- Mostrar el resultado final.