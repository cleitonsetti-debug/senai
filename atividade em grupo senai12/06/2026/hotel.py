
print("--- SISTEMA DE RESERVAS: POUSADA CONFORTO ---")
PRECO_DIARIA = 150.00

while True:
    print("\n[1] Simular Reserva | [2] Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        dias = float(input("Digite a quantidade de diárias desejadas: "))
        
        # Validação do limite máximo de dias
        if dias < 0.99:
            print("escolha uma diaria de pelo menos um dia")
            break
        
        if dias > 30:
            print("Erro: O limite máximo para reserva online é de 30 dias.")
            
        valor_total = dias * PRECO_DIARIA
        
        # Aplicação do desconto para estadias longas
        if dias > 7:
            print("Parabéns! Você ganhou R$ 100.00 de desconto por longa estadia.")
            valor_desconto = valor_total - 100.00
            
        print(f"O valor total da sua reserva é: R$ {valor_desconto:.2f}")
        
    elif opcao == "2":
        print("Obrigado pelo interesse!")
        break