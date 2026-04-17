contador = 1
notas = 0

while contador <= 3:
    nota = float(input(f"digite a nota { contador } "))
    if nota < 0 or nota > 10:
        print("nota invalida. a nota deve estar entre 0 e 10")
        continue
    contador += 1
    notas += nota
    media = notas / 4
    print("a media de notas e: ", media)
    if media >= 7:
        print("o aluno esta aprovado")
    if media >= 5:
        print("o aluno esta em recuperação")
    else:
        print("o aluno esta reprovado")