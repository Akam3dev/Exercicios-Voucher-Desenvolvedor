nome_completo = input("Digite o seu nome completo: ")
idade = int(input("Digite sua idade: "))

try:
    if idade >= 18:
        print("Parabéns você passou para a próxima fase! E esta na primeira fase.")
        cargo = 1
        curso = input("Possui curso? [sim], [nao]: ")
        curso = curso.lower()
    else:
        print("Infelizmente não foi aprovado para a primeira fase, obrigado pela sua participação!")

    if curso == "sim" and cargo == 1:
        print("Parabéns você passou para a próxima fase! E esta na segunda fase")
        cargo = 2
        nota = float(input("Digite a nota: "))
    else:
        print("Infelizmente não foi aprovado para a segunda fase, obrigado pela sua participação!")

    if nota > 7 and cargo == 2:
        print("Parabéns você passou para a próxima fase! E esta apta para a etapa final")
        cargo = 3
    else:
        print("Infelizmente não foi aprovado para a terceira fase, obrigado pela sua participação!")
except NameError:
    print("")