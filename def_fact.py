n=int(input("enter N"))
def fact_(n):
    if(n==0):
        return 1
    else:
        return n * fact_(n - 1)
print(fact_(n))
