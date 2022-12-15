def topla(x):
    toplam = (x*(x+1))/2
    return int(toplam)
def topla2(x):
    #base case
    if x==1:
        return 1
    #recursive case
    else:
        toplam_2= x+topla2(x-1)
        return toplam_2
print(topla(1))
print(topla(10))
print(topla(100))
print(topla2(10))
print(topla2(50))
print(topla2(5))