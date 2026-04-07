print("1. Estudante")
print("2. Trabalhador")
print("3. Idoso")
print("4. Comum")

tarifa = 2.5
erro = "Erro! Digite uma opção valida."

opc = int(input("Selecione a categoria do passageiro: "))
if opc > 0 and opc < 5:
    km = float(input("Insira a quantidade de quilometros(km) percorridos: "))

match opc:
    case 1:
        valor_total = (km * tarifa) * 0.5

    case 2:
        valor_total = (km * tarifa) * 0.8

    case 3:
        valor_total = 0

    case 4: 
        valor_total = km * tarifa
    case _:
        print(erro)

if opc > 0 and opc < 5:
    print(f"O valor final da passagem é R${valor_total:.2f}.")