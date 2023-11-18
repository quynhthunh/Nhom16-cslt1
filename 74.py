print(' ',end='')
j=1
for i in range(1,11):
    print(" ",i,sep="",end="")
print("")
while j<=10:
    print(j,end=' ')
    for i in range(1,11):
        print(i*j,end=' ')
    print('')
    j=j+1