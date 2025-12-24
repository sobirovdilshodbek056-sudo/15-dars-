# 15-dars: While tsikli

# while -"toki" yoki "qachonki" deb tarjima qilinadi.
# Ya'ni, toki shart to'g'ri (True) ekan, kod bajarilaveradi.

# 1-misol: Oddiy while tsikli
print("--- 1-misol: 1 dan 5 gacha sanash ---")
son = 1
while son <= 5: # toki son 5 dan kichik yoki teng ekan
    print(son, end=' ')
    son += 1 # son ni 1 taga oshiramiz, aks holda tsikl abadiy aylanadi
print("\nTugadi!\n")


# 2-misol: Foydalanuvchi inputi bilan ishlash
print("--- 2-misol: Input bilan ishlash ---")
savol = "Istalgan son kiriting (to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(f"Siz kiritgan so'z/son: {qiymat}")
print("Dastur to'xtadi.\n")


# 3-misol: Ishora (Flag) dan foydalanish
print("--- 3-misol: Ishora (Flag) ---")
print("(Dastur to'xtashi uchun 'stop' deb yozing)")
ishora = True
while ishora:
    matn = input("Biror nima yozing: ")
    if matn == 'stop':
        ishora = False # Loop shu yerdan keyin qayta aylanmaydi
    else:
        print(matn)
print("Flag o'zgardu, tsikl tugadi.\n")


# 4-misol: break yordamsida tsiklni to'xtatish
print("--- 4-misol: break ---")
print("Kvadratini hisoblaymiz (chiqish uchun 'chiqish' deb yozing)")
while True: # Abadiy tsikl
    qiymat = input("Son kiriting: ")
    if qiymat == 'chiqish':
        break # Tsiklni to'liq to'xtatadi
    if qiymat.isdigit():
        print(f"{qiymat} ning kvadrati = {int(qiymat)**2}")
    else:
        print("Iltimos, son kiriting!")
print("Dastur tugadi.\n")


# 5-misol: continue - qadam tashlab o'tish
print("--- 5-misol: continue ---")
print("1 dan 10 gacha bo'lgan faqat juft sonlarni chiqaramiz")
son = 0
while son < 10:
    son += 1
    if son % 2 != 0: # Agar toq son bo'lsa
        continue # Tsiklning boshiga qaytadi, pastdagi kod bajarilmaydi
    print(son, end=' ')
