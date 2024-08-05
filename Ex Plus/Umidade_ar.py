def umidade():
    umidade = []

    e1 = float(input("Medição 1 - Digite a pressão do vapor do ar: "))
    es1 = float(input("Medição 1 - Digite a pressão do vapor saturado: "))
    umidade.append((e1 / es1) * 100)

    e2 = float(input("Medição 2 - Digite a pressão do vapor do ar: "))
    es2 = float(input("Medição 2 - Digite a pressão do vapor saturado: "))
    umidade.append((e2 / es2) * 100)

    e3 = float(input("Medição 3 - Digite a pressão do vapor do ar: "))
    es3 = float(input("Medição 3 - Digite a pressão do vapor saturado: "))
    umidade.append((e3 / es3) * 100)

    ur = sum(umidade) / len(umidade)

    if ur < 12:
        print("Estado de emergencia")
    elif ur >= 12 and ur <= 20:
        print("Estado de alerta")
    elif ur > 20 and ur <= 30:
        print("Estado de atenção")
    elif ur > 30 and ur <= 60:
        print("Estado aceitavel")
    else:
        print("Estado ideal")

umidade()