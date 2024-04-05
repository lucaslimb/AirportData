#Qual o total de voos internacionais que partiram do aeroporto de Logan em 2014?
#Quando (mês/ano) ocorreu o maior trânsito de passageiros no aeroporto de Logan?
#Qual o total de passageiros que passaram pelo aeroporto de Logan,
# no ano que for especificado pelo usuário?
#Qual o mês que possui a maior média da diária de um hotel,
# com base no ano especificado pelo usuário?

with open("economic-indicators.csv", "r") as arquivo:
    totalVoos = 0
    maiorTransito = 0
    anoUsuario = input("Digite o ano: ")
    totalPassageirosAno = 0
    mesMaiorDiaria = 0
    maiorMediaDiaria = 0

    for linha in arquivo.readlines()[1:-1]:
        coluna = linha.split(",")
        if coluna[0] == "2014":
            totalVoos += float(coluna[3])
        if float(coluna[2]) > maiorTransito:
            maiorTransito = float(coluna[2])
            ano = coluna[0]
            mes = coluna[1]
        if anoUsuario == coluna[0]:
            totalPassageirosAno += float(coluna[2])
        if anoUsuario == coluna[0]:
            if float(coluna[5]) > maiorMediaDiaria:
                maiorMediaDiaria = float(coluna[5])
                mesMaiorDiaria = coluna[1]

    print("Total de voos no aeroporto de Logan em 2014: ", totalVoos)
    print("{}/{} ocorreu o maior trânsito de passageiros ({})".format(mes, ano, maiorTransito))
    print("Total de passageiros no ano de {}: {}".format(anoUsuario, totalPassageirosAno))
    print("Mês com a maior média de diária em um hotel em {}: {}".format(anoUsuario, mesMaiorDiaria))








