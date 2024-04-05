"""year = ano do dado
month = mês do dado
logan_passengers = qntd de passageiros totais
logan_intl_flights = total de voos internacionais que partiram do aeroporto
hotel_occup_rate = % de vagas ocupadas nos hotéis de Boston
hotel_avg_daily_rate = média diária (dólar) de um hotel em Boston
unemp_rate = porcentagem de desempregados em Boston"""

#Qual o total de voos internacionais que partiram do aeroporto de Logan em 2014?
with open("economic-indicators.csv", "r") as arquivo:
    total = 0
    for linha in arquivo.readlines()[1:-1]:
        lista = linha.split(",")
        if lista[0] == "2014":
            total += float(linha.split(",")[3])
    print("Total de voos em 2014: ", total)

print("")
#Quando (mês/ano) ocorreu o maior trânsito de passageiros no aeroporto de Logan?
with open("economic-indicators.csv", "r") as arquivo:
    maior = 0
    for linha in arquivo.readlines()[1:-1]:
        lista = linha.split(",")
        if float(lista[2]) > maior:
            maior = float(lista[2])
            ano = lista[0]
            mes = lista[1]
    print("{}/{} - total de passageiros: {}".format(mes, ano, maior))

print("")
#Qual o total de passageiros que passaram pelo aeroporto de Logan,
# no ano que for especificado pelo usuário?
anoUsuario = input("Digite o ano: ")
totalAno = 0
with open("economic-indicators.csv", "r") as arquivo:
    if anoUsuario >= "2013" and anoUsuario <= "2019":
        for linha in arquivo.readlines()[1:-1]:
            if anoUsuario == linha.split(",")[0]:
                totalAno += float(linha.split(",")[2])
        print("Total de passageiros no ano de {}: {}".format(anoUsuario, totalAno))
    else:
        print("Ano não encontrado!")

#Qual o mês que possui a maior média da diária de um hotel,
# com base no ano especificado pelo usuário?
mesMaiorDiaria = 0
maiorMediaDiaria = 0
with open("economic-indicators.csv", "r") as arquivo:
    for linha in arquivo.readlines()[1:-1]:
        if anoUsuario == linha.split(",")[0]:
            if float(linha.split(",")[5]) > maiorMediaDiaria:
                maiorMediaDiaria = float(linha.split(",")[5])
                mesMaiorDiaria = linha.split(",")[1]
    print("Mês de maior média diária em {}: {}".format(anoUsuario, mesMaiorDiaria))