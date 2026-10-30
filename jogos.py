jogos = 0
opcao = 0

# Laço para identificar qual ação o usuário quer explorar. Caso seja 1, pedirá para registrar os jogos, gols feitos e sofridos;
# Se 2, mostrará todos os resultados obtidos através dos dados coletados na opção 1;
# Se 3, encerrará o programa sem mostrar nada.


while opcao != 3:
    print("")
    print("===== CAMPANHA DO TIME DE VÁRZEA =====")
    print("1 - Registrar campanha")
    print("2 - Ver resumo da campanha")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

# Se escolher opção 1, pedirá informações, como: quantidade de jogos, gols marcados e gols sofridos.
# Quantidade de jogos registrados deve ser maior que 0 até 30.

    if opcao == 1:
        jogos = int(input("Quantos jogos o time disputou (1 a 30)? "))
        while jogos < 1 or jogos > 30:
            print("Quantidade inválida! Tente novamente.")
            jogos = int(input("Digite a quantidade de jogos: "))
        pontos = 0
        vitorias = 0
        empates = 0                
        derrotas = 0
        goleadas = 0
        gols_pro = 0
        gols_contra = 0
        maior_gols = 0
        jogos_registrados = []

# Aqui criamos um range que vai percorrer o número de jogos registrados.

        for numero_jogo in range(1, jogos + 1):
            print("")
            print("--- Jogo", numero_jogo, "---")
# Aqui pedirá a quantidade de gols marcados.
            gols_marcados = int(input("Gols marcados: "))
            while gols_marcados < 0:
                print("Gols não podem ser negativos!")
                gols_marcados = int(input("Gols marcados: "))
# Aqui pedirá a quantidade de gols sofridos.
            gols_sofridos = int(input("Gols sofridos: "))
            while gols_sofridos < 0:
                print("Gols não podem ser negativos!")
                gols_sofridos = int(input("Gols sofridos: "))
# Dentro desse if, elif e else, vai retornar quais jogos foram ganhos, empatados ou perdidos.
            # Resultado e pontuação
            if gols_marcados > gols_sofridos:
                resultado = "Vitória"
                pontos = pontos + 3
                vitorias = vitorias + 1
            elif gols_marcados == gols_sofridos:
                resultado = "Empate"
                pontos = pontos + 1
                empates = empates + 1
            else:
                resultado = "Derrota"
                derrotas = derrotas + 1
# Aqui irá calcular se a diferença de gols é maior ou igual a 3, caso seja true retornará como "goleada".
            if gols_marcados > gols_sofridos and gols_marcados - gols_sofridos >= 3:
                goleadas = goleadas + 1
                print("*** GOLEADA! ***")
            gols_pro = gols_pro + gols_marcados
            gols_contra = gols_contra + gols_sofridos
# Nessa parte registrará sempre que houver a maior quantidade de gols marcados em uma partida.
            if gols_marcados > maior_gols:
                maior_gols = gols_marcados
# Nesse ponto irá mostra os resultados geral de cada jogo.
            jogos_registrados.append([numero_jogo, gols_marcados, gols_sofridos, resultado])
            print("Resultado:", gols_marcados, "x", gols_sofridos, "-", resultado)

# Se escolher a opção 2, exibirá os resultados geral de todos os jogos e dados coletados.

    elif opcao == 2:
# Se não houver registros de jogos o sistema será encerrado.
        if jogos == 0:
            print("Nenhum jogo registrado ainda. Use a opção 1 primeiro.")
# Tendo os registros, fará o cálculo do aproveitamento do time. Se maior ou igual que 70%, "Briga pelo título"; 
# Maior ou igual 50%, "Zona de classificação";
# Maior ou igual 30%, "Meio da tabela"; Se nenhuma das opções, "Risco de rebaixamento".

        else:
            aproveitamento = pontos / (jogos * 3) * 100

            if aproveitamento >= 70:
                situacao = "Briga pelo título"
            elif aproveitamento >= 50:
                situacao = "Zona de classificação"
            elif aproveitamento >= 30:
                situacao = "Meio de tabela"
            else:
                situacao = "Risco de rebaixamento"
# Nessa parte mostrará o resultado geral da Campanha. Quantidade de jogos, pontos, vitórias, empates, derrotas, goleadas, gols marcados,
#gols sofridos, saldo de gols, média de gols por partida, maior número de gols em um jogo, aproveitamento e situação.
            print("")
            print("===== RESUMO DA CAMPANHA =====")
            for jogo in jogos_registrados:
                print("Jogo", jogo[0], ":", jogo[1], "x", jogo[2], "-", jogo[3])
            print("Pontos:", pontos)
            print("Vitórias:", vitorias, "| Empates:", empates, "| Derrotas:", derrotas)
            print("Goleadas:", goleadas)
            print("Gols pró:", gols_pro, "| Gols contra:", gols_contra)
            print("Saldo de gols:", gols_pro - gols_contra)
            print("Média de gols marcados por jogo:", round(gols_pro / jogos, 1))
            print("Maior número de gols em um jogo:", maior_gols)
            print("Aproveitamento:", round(aproveitamento, 1), "%")
            print("Situação:", situacao)
# Se o número escolhido não for igual as opções disponíveis retornará "Opção Inválida!" e o sistema encerra.
    elif opcao != 3:
        print("Opção inválida! Escolha 1, 2 ou 3.")

print("Encerrando o sistema...")