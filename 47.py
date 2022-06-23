a1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.G.: '))
an = int(1)
for i in range (1,11):
    an = a1*(r**i)
    print(an)