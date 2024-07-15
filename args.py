# def soma_argumentos(n1, *args):
#     n1 = 0
#     for i in args:
#         n1 += i
#     return (f"numeros : {args}, resultado: {n1}")


# x = soma_argumentos(5, 10, 20, 30, 40)
# print(x)

# def retornar_media(*args):
#     soma = sum(args)
#     return soma / len(args)

# y = retornar_media(6,6,6,6,6,10)
# print(y)

def dados(**kwargs):
    return kwargs

x = dados(nome = input(": "), sobrenome = input(": "), email = input(": "), pais = input(":"), idade = int(input(": ")), phone = input(": "))
print(x)