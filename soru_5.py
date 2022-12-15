import math
def superasalmi(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    for i in range(2,(int(math.sqrt(int(str(x)[0:4]))+1))):
        if int(str(x)[0:4]) % i == 0:
            return False
    for i in range(2,(int(math.sqrt(int(str(x)[0:3]))))+1):
        if int(str(x)[0:3]) % i == 0:
            return False
    for i in range(2,(int(math.sqrt(int(str(x)[0:2])))+1)):
        if int(str(x)[0:2]) % i == 0:
            return False
    for i in range(2,(int(math.sqrt(int(str(x)[0:1]))))+1):
        if int(str(x)[0:1]) % i == 0:
            return False
    for i in range(2,(int(math.sqrt(int(str(x)[0]))))+1):
        if int(str(x)[0:5]) % i == 0:
            return False
    return True

for i in range(10000,100001):
    if superasalmi(i)==True:
        print(i,end=" ")

