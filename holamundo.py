

def suma(n1, n2):
    result = n1 + n2

    if n1 is None:
        return "Falta numero n1"
    return result

n1 = int(input("Ingrese n1: "))

n2 = int(input("Ingrese n2: "))

result = suma(n1, n2)

print(result)