import csv

#-------------FUNÇÕES-----------------------
#BUSCA DADOS DE UM ARQUIVO CSV. PARAMETRO:NOME DO ARQUIVO
def getData(filename):
    file = open(filename, "r", encoding="cp437")
    data = list( csv.reader(file, delimiter=",")) #lista de listas
    file.close()
    data = data[1:]
    return data

def showMenu(dictionary):
  for key, value in dictionary.items():
    print(key, "\t", value)

def executeMenu(option):
  print("\n\t\t\t", options[option], "\n")

def filterByYear(data, ano_escolhido):
  data2 = []
  for row in data:
    date = row[0].split("-")
    y = int(date[0])
    if ano_escolhido == y:
      data2.append(row)
  return data2

def filterByMonth(data2, mes_escolhido):
  data3 = []
  for row in data2:
    date = row[0].split("-")
    m = int(date[1])
    if mes_escolhido == m:
      data3.append(row)
  return data3
      
def busca_artista(data, artista_escolhido):
  contador_artista = 0
  for row in data:
    artista = row[3].lower()
    if artista_escolhido.lower() in artista:
      print(row)
      contador_artista += 1
  return contador_artista
      

def cada_mes_sem(x, data3):
  for i in range(1,x):
    posicao_escolhida = i 
    posicao_mes_sem(data3, posicao_escolhida)

def posicao_mes_sem(data3, posicao_escolhida):
  lista_posicao_semana = []
  NSemanas = []
  maior = 0
  for row in data3:
    if int(row[1]) == posicao_escolhida:
      lista_posicao_semana.append(row)
  for row in lista_posicao_semana:
    if int(row[6]) > maior:
      maior = int(row[6])
      NSemanas.append(row)
  print(NSemanas[len(NSemanas)-1])



def busca_posicao(data3, posicao_escolhida):
  lista_posicao_semana = []
  NSemanas = []
  maior = 0
  print(f"\nEssas são as posições {posicao_escolhida} gerais do mês:\n")
  for row in data3:
    if int(row[1]) == posicao_escolhida:
      print(row)
      lista_posicao_semana.append(row)
  print(f"\nEssa é a posição {posicao_escolhida} principal do mês:\n")
  for row in lista_posicao_semana:
    if int(row[6]) > maior:
      maior = int(row[6])
      NSemanas.append(row)
  print(NSemanas[len(NSemanas)-1])



def artista_mais_semanas(data3):
  maior = 0
  NSemanas = []
  for row in data3:
    if int(row[6]) >= maior:
      maior = int(row[6])
      NSemanas.append(row)
  return NSemanas[len(NSemanas)-1]

def artista_mais_apareceu(data):
  artistas_vezes = {}
  for row in data:
    artista = row[3]
    if artista in artistas_vezes:
      artistas_vezes[artista] += 1
    else:
      artistas_vezes[artista] = 1
  mais_popular = max(artistas_vezes.items(), key = lambda k: k[1])
  return mais_popular

#-----------FUNÇÕES DE ORGANIZAÇÃO---------------
def funcao1():
  ano_escolhido = int(input("Digite o ano escolhido (XXXX): "))
  mes_escolhido = int(input("Digite o mês escolhido (XX): "))
  data2 = filterByYear(data, ano_escolhido)
  data3 =filterByMonth(data2, mes_escolhido)
  cada_mes_sem(11, data3)
  
    

def funcao2():
  ano_escolhido = int(input("Digite o ano escolhido (XXXX): "))
  data2 = filterByYear(data, ano_escolhido)
  for i in range(1,13):
    data3 = filterByMonth(data2, i)
    cada_mes_sem(2, data3)

def funcao3():
  ano_escolhido = int(input("Digite o ano escolhido (XXXX): "))
  mes_escolhido = int(input("Digite o mês escolhido (XX): "))
  data2 = filterByYear(data, ano_escolhido)
  data3 =filterByMonth(data2, mes_escolhido)
  cada_mes_sem(101, data3)

def funcao4():
  artista_escolhido = input("Digite o artista escolhido: ")
  contador_artista = busca_artista(data, artista_escolhido)
  print(f"\nArtista {artista_escolhido} apareceu:  {contador_artista} vezes\n")
  
def funcao5():
  ano_escolhido = int(input("Digite o ano escolhido (XXXX): "))
  mes_escolhido = int(input("Digite o mês escolhido (XX): "))
  posicao_escolhida = int(input("Digite a posição escolhida: "))
  data2 = filterByYear(data, ano_escolhido)
  data3 =filterByMonth(data2, mes_escolhido)
  busca_posicao(data3, posicao_escolhida)
  print("\n")
  
def funcao6():
  ano_escolhido = int(input("Digite o ano escolhido (XXXX): "))
  mes_escolhido = int(input("Digite o mês escolhido (XX): "))
  data2 = filterByYear(data, ano_escolhido)
  data3 =filterByMonth(data2, mes_escolhido)
  artista_com_mais_semanas = artista_mais_semanas(data3)
  print(f"\nArtista {artista_com_mais_semanas[3]} esteve no ranking por {artista_com_mais_semanas[6]} semanas, sendo assim o artista com mais semanas.\n")

def funcao7():
  mais_popular = artista_mais_apareceu(data)
  print(f"\n A artista que mais apareceu na lista foi {mais_popular[0]}, com {mais_popular[1]} entradas.\n")
  print(mais_popular)


#----------VARIÁVEIS-------------------------
data = getData("billboard.csv")
options = {"1":"Top 10 de um mês / ano específico",
           "2":"Top 12 do ano (1º de cada mês)",
           "3":"Top 100 de um mês / ano específico",
           "4":"Busca por artista",
           "5":"Busca por posição na lista no mês / ano",
           "6":"Artista que ficou mais semanas no mês / ano",
           "7":"Artista que mais apareceu na lista",
           "SAIR":"Sair do programa"}


#-------------PRINCIPAL------------------
#for activity in disney_activities:
#  print(activity[0])

selected = ""
while selected != "SAIR":
  print("-"*70)
  print("Top 100 músicas da Billboard (Janeiro de 1958 a Novembro de 2021)")
  print("-"*70)
  showMenu(options)
  print("-"*70)
  selected = input("Selecione uma opção: ").upper() 
  executeMenu(selected)
  
  if selected == "1":
    funcao1()

  elif selected == "2":
    funcao2()
    
  elif selected == "3":
    funcao3()

  elif selected == "4":
    funcao4()

  elif selected == "5":
    funcao5()

  elif selected == "6":
    funcao6()
    
  elif selected == "7":
    funcao7()
'''
  elif selected != "1" and selected != "2" and selected != "3" and selected != "4" and selected != "5" and selected != "6" and selected != "7" and selected != "SAIR":
    print("Erro! Digite apenas as opções mostradas!")
    continue
'''
