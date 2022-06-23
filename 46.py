a1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A.: '))
an = int(1)
for i in range (1,11):
    an = a1 + (i*r)
    print(an)