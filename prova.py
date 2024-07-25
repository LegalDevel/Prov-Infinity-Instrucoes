numeroAlunos = int(input("Digite a quantidade de alunos da sala de aula: "))
mediaGeral = 0

for aluno in range(numeroAlunos):
    nome = input("Digite o nome do aluno: ")
    n1 = float(input(f"Digite a primeira nota: "))
    n2 = float(input(f"Digite a segunda nota: "))
    n3 = float(input(f"Digite a terceira nota: "))

    media = (n1 + n2 + n3)/3
    mediaGeral += media

    situacao = "Aprovado" if media >= 7.0 else "Reprovado"

    print("\nAluno:", nome)
    print("Notas:", n1, n2, n3)
    print("Média:", media)
    print("Situação", situacao)

mediaGeral /= numeroAlunos
print("\nMédia Geral da turma:", mediaGeral)


        
    