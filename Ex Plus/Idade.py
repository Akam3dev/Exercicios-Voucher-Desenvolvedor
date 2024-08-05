'''
def gisele():
    idades = []
    for i in range(3):
        idades.append(int(input(": ")))

    idades.remove(max(idades))
    idades.remove(min(idades))

    print(idades[0])
gisele()
'''

n1 = int(input("idade 1: "))
n2 = int(input("idade 2: "))
n3 = int(input("idade 3: "))

maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

if n1 != maior and n1 != menor:
    print(n1)
elif n2 != maior and n2 != menor:
    print(n2)
elif n3 != maior and n3 != menor:
    print(n3)