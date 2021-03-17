#1
#a
a = [1-x for x in range(1,11)]
print(a)

#b
b = [4**x for x in range(8)]
print(b)
#c
c = [x for x in b if x%2==0]
print(c)


#2

liczby = [x for x in range(1,20)]
parzyste = [x for x in liczby if x%2==0]
print(parzyste)

#3

produkty = {"chleb":"szt" , "mleko":"1" ,"masło":"1"}
print(produkty)
produkt_szt = [x for x in produkty.keys() if produkty[x]=='szt']
print(produkt_szt)


#4

def tr(a,b,c):

    if(((a**2)+(b**2))==c**2):
        return  "Prostokątny"
    return  "Nie prostokątny"
print(tr(1,2,3))


#5


def trap(a=2,b=5,h=1):
    if(a==0 or b==0 or h==0):
        return 0
    return (((a+b)*h)/2)

print(trap())


#6

def ilelci(a=1,b=4,li=10):
    if(li==1):
        return 1
    return ilelci(a,b,li-1)*b

print(ilelci(1,2,3))