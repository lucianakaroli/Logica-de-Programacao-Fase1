#Mes numérico de 1 a 12
#Cada mes do ano: temperatura maxima em Celsius

#Calcular:
# a) Temperatura media máxima anual
# b) Quantidade de meses escaldantes (temperatura > 33 graus)
# c) Mes mais escaldante do ano (deve ser escrito por extenso)
# d) Mes menos escaldante do ano (deve ser escrito por extenso)


incluido_mes_janeiro = False
incluido_mes_fevereiro = False
incluido_mes_marco = False
incluido_mes_abril = False
incluido_mes_maio = False
incluido_mes_junho = False
incluido_mes_julho = False
incluido_mes_agosto = False
incluido_mes_setembro = False
incluido_mes_outubro = False
incluido_mes_novembro = False
incluido_mes_dezembro = False

#meses numericos de 1 a 12(nao aceitar letras e numeros maiores ou menores)
meses_validos = 0
while meses_validos <= 11:
  mes = (input("Por favor, digite um número correspondente a um mes (de 1 a 12):"))
  if mes.isnumeric() == False:
    print(f"Erro. É apenas válido números. (Tente de 1 a 12).")
  else:
    mes = int(mes)
    if mes < 1 or mes > 12:
      print(f"Mês invalido. Apenas números de 1 a 12 são aceitos.")
    else:
        print(f"Certo, você escolheu o mês:", (mes))
        meses_validos = meses_validos + 1
        if mes == 1:
          if incluido_mes_janeiro:
            print("Mes de janeiro ja foi incluído! Por favor, tente outro mes")
          else:
            incluido_mes_janeiro = True

        if mes == 2:
           if incluido_mes_fevereiro:
             print("Mes de fevereiro ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_fevereiro = True

        if mes == 3:
           if incluido_mes_marco:
             print("Mes de março ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_marco = True

        if mes == 4:
           if incluido_mes_abril:
             print("Mes de abril ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_abril = True

        if mes == 5:
           if incluido_mes_maio:
             print("Mes de maio ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_maio = True

        if mes == 6:
           if incluido_mes_junho:
             print("Mes de junho ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_junho = True

        if mes == 7:
           if incluido_mes_julho:
             print("Mes de julho ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_julho = True

        if mes == 8:
           if incluido_mes_agosto:
             print("Mes de agosto ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_agosto = True

        if mes == 9:
           if incluido_mes_setembro:
             print("Mes de setembro ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_setembro = True

        if mes == 10:
           if incluido_mes_outubro:
             print("Mes de outubro ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_outubro = True

        if mes == 11:
           if incluido_mes_novembro:
             print("Mes de novembro ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_novembro = True

        if mes == 12:
           if incluido_mes_dezembro:
             print("Mes de dezembro ja foi incluído! Por favor, tente outro mes")
           else:
            incluido_mes_dezembro = True

#temperatura em Celsius

temperatura_valida = 0
while temperatura_valida <=12:
  temperatura = (input("Por favor, digite a maior temperatura do mês respectivo (em Celsius):"))
  if temperatura.isnumeric() == False:
    print(f"Erro. É apenas válido números. (Tente de -60 a 50).")
  else:
    temperatura = float(temperatura)
    if temperatura < -60 or temperatura > 50:
      print(f"Temperatura invalida. Apenas números de -60 a 50 são aceitos.")
    else:
        print(f"Certo, você digitou a temperatura:", (temperatura))
        temperatura_valida = temperatura_valida + 1


temperatura_total= 0
soma=0
while temperatura_total >= -50 or temperatura_total <= 50:
    print("temperatura total", temperatura_total)
    temperatura = float(input("Digite a temperatura do mês:"))
    while temperatura < -60 or temperatura >50:
      print("Temperatura inválida. Deve estar no intervalo de -60 e 50 graus.")
      temperatura = float(input(" > Digite novamente a temperatura:"))

    mes = int(input("Digite um número correspondente a um mês. De 0 a 12"))
    while mes < 1 or mes > 12:
      print("Mes inválido. Deve estar no intervalo de 1 a 12.")
      mes = int(input("> Digite novamente o número do mês. De 1 a 12:"))

#calcular
# a) Temperatura media máxima anual
    soma = soma + temperatura_total
    temperatura_total = temperatura_total + 1

print("Media das temperaturas:", soma/temperatura_total)


