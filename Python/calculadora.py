
def soma(a,b):
    return a + b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao(a,b):
    if b == 0 or a == 0:
        return "Erro!"
    else:
        return a/b

def menu():
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Sair")

    decisao = input("O que deseja realizar? ")
    numero1 = float(input("Digite o primeiro valor: "))
    numero2 = float(input("Digite o segundo valor: "))

    if(decisao == "1"):
        resultado = soma(numero1, numero2)
        print(resultado)
    elif(decisao == "2"):
        resultado = subtracao(numero1, numero2)
        print(resultado)
    elif(decisao == "3"):
        resultado = multiplicacao(numero1, numero2)
        print(resultado)
    elif(decisao == "4"):
        resultado = divisao(numero1, numero2)
        print(resultado)
    elif(decisao == "5"):
        print("Saindo do programa...")
    else:
        print("Digito invalido!")
        menu()


if __name__ == "__main__":
    menu()




