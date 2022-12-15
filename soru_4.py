def fibonacci(x):
    i=1
    j=1
    for a in range(0,x):
        if a == 1 or a == 0:
            print(1,end=" ")
        else:
            print(i+j,end=" ")
            toplam=i+j
            i=j
            j=toplam
fibonacci(30)

################################

def fibonacci(x):
    if x == 1 or x == 0:
        return 1
    else:
        #recursive case
        return fibonacci(x-1)+fibonacci(x-2)
for i in range(0,30):
    print(fibonacci(i),end=" ")


