notas=[""]*5
soma=0
contador=0
for x in range(5):
    notas[x] =float(input("digite uma nota:"))

for i in range (5):
    soma+= notas[i]
media=soma/5
for j in range (5):
    if notas[i]>media:
        contador=contador+1

print(f"{contador} notas seraos maiores que a media {media}")