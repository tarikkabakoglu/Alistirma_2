import random
a=0
sayi=random.randint(10,98)
while a==0:
    if str(sayi)[0]==str(sayi)[1]:
        a=0
        sayi=random.randint(10,98)
    else:
        a=1
print(sayi)

j=0
while j==0:
    tahmin = int(input("bir tahmin giriniz:"))
    b = 0
    while b == 0:
        if tahmin < 10 or tahmin > 98 or str(tahmin)[0] == str(tahmin)[1]:
            tahmin = int(input("aralıkta ve rakamları farklı bir tahmin giriniz:"))
        if tahmin >= 10 and tahmin <= 98 and str(tahmin)[0] != str(tahmin)[1]:
            b=1
    if tahmin==sayi:
        print("2\n","tebrikler kazandınız")
        j=1
    elif str(tahmin)[::-1]==str(sayi):
        print(-2)
    elif str(tahmin)[0]==str(sayi)[1] or str(tahmin)[1]==str(sayi)[0]:
        print(-1)
    elif str(tahmin)[1]==str(sayi)[1] or str(tahmin)[0]==str(sayi)[0]:
        print(1)
    elif tahmin!=sayi:
        print(0)