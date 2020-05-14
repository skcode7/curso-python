def sumar(*args):
    total = 0
    for valor in args:
        total += valor
    return total

def usuarios_autenticados(**kwargs):
    print(kwargs)

print(sumar(4, 5, 6))
usuarios_autenticados(charly=True, sk=False)