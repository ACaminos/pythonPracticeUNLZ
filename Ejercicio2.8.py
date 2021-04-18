lista = [1,2,3,4,5,6,7,8,9,10]
i = 0
for i ,numero in enumerate(lista):
    if lista.index(i)%2 == 0 :
        lista.insert(i,'PAR')
        i = i + 1
    else :
        i = i + 1

print(lista)