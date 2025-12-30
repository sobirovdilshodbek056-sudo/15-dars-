product = lambda x, y : x ** y
def daraja(n):
    return lambda x : x**n
kvadrat = daraja(2)
kub = daraja(3)
print(f"2-ning kvadrati {kvadrat(2)} ga, kubi {kub(2)} ga teng")
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")


from math import sqrt
sonlar = list(range(19)) # 0 dan 19 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))
sonlar = list(range(19)) # 0 dan 19 gacha sonlar ro'yxati
def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x
print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz


a = [9, 5, 8]
b = [7, 12, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)






