def toliq_ism_yasa(ism, familiya):
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
talaba1 = toliq_ism_yasa('dilshodbek','sobirov')
talaba2 = toliq_ism_yasa('jasur','nabiyev') 
print(f"Darsga kelmagan talabalar:{talaba1} va {talaba2}")