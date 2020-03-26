
tab=4*[0]
index=0
while index<4:
    val=input('Entrez un entier >')
    if val.isalpha() :
        print('Entier incorrect')
    else:
        tab[index]=int(val)
        index=index+1
max=tab[0]
min=tab[0]
index=0
for i in tab:
    if max<tab[index]:
        max=tab[index]
    if min>tab[index]:
        min=tab[index]
    index=index+1

print('Le min est '+str(min))
print('Le max est '+str(max))
