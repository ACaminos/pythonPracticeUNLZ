import random
lista=[]
cont_repe = 0 
num = 0
for i in range(20):    
    lista.append(random.randrange(0, 100, 2))
print(lista)

for i in range(len(lista)):
    num = lista[i]
    print("num: " , num)
    for j in range(len(lista)):
        if lista[j] == num:
            cont_repe += 1
    print("cont_repe: " , cont_repe)
    cont_repe = 0
