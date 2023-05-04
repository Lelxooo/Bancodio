menu = """
==================MENU==================


[d] Depósito
[s] Saque
[e] Extrato
[0] Sair


========================================

=> """
c = """
Gostaria de continuar a operação?

[y] Sim
[n] Não
"""
vs = 0
vd = 0
saldo = vd - vs
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3
sr = LIMITE_SAQUE - numero_saque
extrato = f"""
                Valor depositado:
                     R${vd:.2f}
                Valor de saque:
                     R${vs:.2f}
                Saques restantes:
                     {sr}
                Slado atual:
                     {saldo}
                     
        """

while True:
    m = input(menu)

    if m == "d":
        print("Depósito")
        vd = float(input("Qual valor você gostaria de depositar? \n"))
        saldo = saldo + vd
        m2 = input(c)
        if m2 == "n":
            break

    elif m == "s":
        print("Saque")
        numero_saque += 1
        if numero_saque == 4:
            print("Você atingiu o limite de saque por hoje, por favor, tente novamente amanhã!")
            break
        vs = float(input("Qual valor você gostaria de sacar? \n"))
        if vs >= 500:
            print("Pera lá amigão, R$500 é o limite de saaque, recomece a operação e tente novamente com um valor menor!")
            break
        if vs > saldo:
            print(f"""
            Você não tem dinheiro o suficiente em sua conta para continuar essa operação
            Saldo em conta: {saldo}
            Valor da tentativa de saque: {vs}
                                                                                        Por favor, recomece a operação e tente novamente com um valor menor!             
            """)
            break
        saldo = saldo - vs
        m2 = input(c)
        if m2 == "n":
            break

    elif m == "e":
        print(extrato)
        break


    elif m == "q":
        break
    else:
        print("Comando errado, por favor selecione uma opção válida.")