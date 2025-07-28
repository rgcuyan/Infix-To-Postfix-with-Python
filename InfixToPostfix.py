import re

#--------------------------------------------------------------------
regex = r'^[0-9+\-*/^() ]+$'

# Compilación del patrón de expresión regular hecha en VERBOSE para usarla varias veces y no compilarla cada vez
patron = re.compile(regex, re.VERBOSE)

#-------------------------------FUNCION PARA VALIDAR UNA CADENA INFIX, VALIDA BALANCEO DE PARENTESIS, USO CORRECTO DE LOS SIGNOS Y QUE HAYAN VALORES NUMERICOS-------------------------------------
def tokenizar(expresion):
    # Encuentra todos los números y operadores/paréntesis
    return re.findall(r'\d+|[+\-*/^()]', expresion)

def validar_expresion(expresion):
    
    expresion = expresion.strip()#Quita espacios en blanco al inicio y al final de la cadena

    if not patron.match(expresion):# la funcion match verifica que la expresión cumpla con el patrón definido por la expresión regular (regex)
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
    tokens = tokenizar(expresion) 
    #tokens = expresion.split()
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
    
    prioridad = {
        '+':1, 
        '-':1, 
        '*':2, 
        '/':2, 
        '^':3
        }
    
    salida = []
    pila = []
    tokens = tokenizar(expresion) 

    for token in tokens:
        #print(token)
        if token.isdigit():     #Si es digito entonces lo guarda en la salida
            salida.append(token)
            #print(pila)
        elif token == '(': #Si es parentesisi inicial entonces se mete en la pila
            pila.append(token)
        elif token == ')':  #Si es 
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()
        elif es_operador(token):  
            while (pila and pila[-1] != '(' and prioridad[pila[-1]] >= prioridad[token]):
                salida.append(pila.pop())
            pila.append(token)
        else:
            raise ValueError(f"Token inválido: {token}")
    
    while pila:
        salida.append(pila.pop())

    return " ".join(salida)


def es_operador(token):
    return token in "+-*/^"


'''#Pruebas de la función
print(validar_expresion("3 + 4 * 2"))            # True
print(validar_expresion("3 + + 4"))              # False (operadores consecutivos)
print(validar_expresion("( 3 + 4 ) * 2"))        # True
print(validar_expresion("3 + (4 * 2"))           # False (paréntesis no balanceados)
print(validar_expresion("3 + a * 2"))            # False (caracter inválido)
print(validar_expresion(" + 3 * 2"))             # False (operador al inicio)
print(validar_expresion("3 * 2 -"))               # False (operador al final)'''


#--------------------------------------------------------------------

def evaluar_postfix(postfix):
    pila = []
    tokens = postfix.split()

    for token in tokens:
        if token.isdigit():
            pila.append(float(token))
        else:
            if len(pila) < 2:
                raise ValueError("Expresión inválida")
            b = pila.pop()
            a = pila.pop()

            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("División por cero")
                pila.append(a / b)
            elif token == '^':
                pila.append(a ** b)
            else:
                raise ValueError(f"Operador no reconocido: {token}")
    
    if len(pila) != 1:
        raise ValueError("Expresión inválida: operandos sobrantes")
    return pila[0]


arregloExpresiones = []
with open("Expresiones.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if validar_expresion(linea) == True:
            arregloExpresiones.append(linea)
            #print(linea)
            resultadoPostfix = infixToPostfix(arregloExpresiones.pop())
            resultado = evaluar_postfix(resultadoPostfix)
            print(f"Expresion: {linea}")
            print(f"Postfix: {resultadoPostfix}")
            print(f"Resultado: {resultado}\n")
            print()