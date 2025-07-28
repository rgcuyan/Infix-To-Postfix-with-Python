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

def main():
    expresiones = [
        "3 4 2 * 1 5 - 2 ^ / +", 
    ]

    for i, expr in enumerate(expresiones, 1):
        print(f"Expresión {i}: {expr}")
        resultado = evaluar_postfix(expr)
        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    main()
