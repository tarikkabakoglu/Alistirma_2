def carp(x):
    #base case
    if x==1:
        return 1
    #recursive case
    else:
        return x*carp(x-1)
print(carp(4))
print(carp(6))

