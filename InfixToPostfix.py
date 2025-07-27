import re
#Espacio de trabajo para Ruddy

regex = r'''
^                       # inicio de cadena
\s*                     # posibles espacios al inicio
(                       # inicio grupo de primer número o paréntesis
    \d+                 # uno o más dígitos (número)
    |                   # o
    \(                  # paréntesis apertura
)                       
(                       # inicio grupo repetición de operador + número o paréntesis
    \s*                 # posibles espacios
    [+\-*/^]            # operador permitido
    \s*                 # posibles espacios
    (                   # siguiente número o paréntesis
        \d+
        |               
        \(
    )
)*                      # cero o más repeticiones
\s*                     # posibles espacios finales
\)?                     # opcional paréntesis cierre (esto lo validamos fuera)
$                       # fin de cadena
'''

# Compilación del patrón de expresión regular hecha en VERBOSE para usarla varias veces y no compilarla cada vez
patron = re.compile(regex, re.VERBOSE)

# Función para validar la expresión regular
def validar_expresion(expresion):
    if not patron.match(expresion):      # la funcion match verifica que la expresión cumpla con el patrón definido por la expresión regular (regex)
        return False
    # Validar balance de paréntesis:
    balance = 0
    for c in expresion:
        if c == '(':
            balance += 1    #por cada ( se suma 1
        elif c == ')':
            balance -= 1    #por cada ) se resta 1
        if balance < 0:
            return False
    return balance == 0     # Al final debe de dar 0 para que los paréntesis estén balanceados

#Pruebas de la función
print(validar_expresion("3 + 4 * 2"))            # True
print(validar_expresion("3 + + 4"))              # False (operadores consecutivos)
print(validar_expresion("( 3 + 4 ) * 2"))        # True
print(validar_expresion("3 + (4 * 2"))           # False (paréntesis no balanceados)
print(validar_expresion("3 + a * 2"))            # False (caracter inválido)
print(validar_expresion(" + 3 * 2"))             # False (operador al inicio)
print(validar_expresion("3 * 2 -"))               # False (operador al final)