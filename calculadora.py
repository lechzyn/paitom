
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
    while True:
        print("1 - Soma")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        print("5 - Sair")

        decisao = input("O que deseja realizar? ")
        if (decisao == "5"):
            print("Saindo do programa...")
            break

        numero1 = float(input("Digite o primeiro valor: "))
        numero2 = float(input("Digite o segundo valor: "))

        if(decisao == "1"):
            resultado = soma(numero1, numero2)
            print(resultado)
            print("")
        elif(decisao == "2"):
            resultado = subtracao(numero1, numero2)
            print(resultado)
            print("")
        elif(decisao == "3"):
            resultado = multiplicacao(numero1, numero2)
            print(resultado)
            print("")
        elif(decisao == "4"):
            resultado = divisao(numero1, numero2)
            print(resultado)
            print("")

        else:
            print("Digito invalido!")



if __name__ == "__main__":
    menu()



