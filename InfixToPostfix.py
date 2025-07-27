import re

#--------------------------------------------------------------------
regex = r'^[0-9+\-*/^() ]+$'

# Compilación del patrón de expresión regular hecha en VERBOSE para usarla varias veces y no compilarla cada vez
patron = re.compile(regex, re.VERBOSE)

#--------------------------------------------------------------------
# Función para validar la cadena infix
def validar_expresion(expresion):
    
    expresion = expresion.strip()       #Quita espacios en blanco al inicio y al final de la cadena

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
        if balance < 0:  # Paréntesis de cierre sin apertura
            return False
    if balance != 0:
        return False     # Al final debe de dar 0 para que los paréntesis estén balanceados
    
    # Validar operadores consecutivos o mal ubicados
    tokens = expresion.split()
    operadores = "+-*/^"
    for i in range(len(tokens)):
        if tokens[i] in operadores:
            # No puede empezar ni terminar con operador
            if i == 0 or i == len(tokens)-1:
                return False
            # No puede haber dos operadores seguidos
            if tokens[i-1] in operadores:
                return False
            # No puede haber un operador justo después de '('
            if tokens[i-1] == '(':
                return False
            # No puede haber un operador justo antes de ')'
            if i < len(tokens)-1 and tokens[i+1] == ')':
                return False
    return True

def infixToPostfix(expresion):
    for variable in expresion:
        print(variable)

#Pruebas de la función
print(validar_expresion("3 + 4 * 2"))            # True
print(validar_expresion("3 + + 4"))              # False (operadores consecutivos)
print(validar_expresion("( 3 + 4 ) * 2"))        # True
print(validar_expresion("3 + (4 * 2"))           # False (paréntesis no balanceados)
print(validar_expresion("3 + a * 2"))            # False (caracter inválido)
print(validar_expresion(" + 3 * 2"))             # False (operador al inicio)
print(validar_expresion("3 * 2 -"))               # False (operador al final)


def es_operador(token):
    return token in "+-*/^"

#--------------------------------------------------------------------
arregloExpresiones = []
with open("Expresiones.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if validar_expresion(linea) == True:
            arregloExpresiones.append(linea)
            print(linea)

