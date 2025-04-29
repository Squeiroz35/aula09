arrayaluno=["joao","carlos","maria","luiza","isabel"]
nomedigi= input("digite um nome:")
mensagem= "este nome nao esta na lista"
for x in range (len(arrayaluno)):
    if nomedigi == arrayaluno[x]:
        mensagem=f"{nomedigi}, esta na lista e na posição {x}"

print (mensagem)