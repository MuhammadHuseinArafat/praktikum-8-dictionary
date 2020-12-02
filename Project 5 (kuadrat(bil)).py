#Latihan Nomor 5
def kuadrat(bil):
        output = []
        for i in range (len(bil)):
                kali = bil[i]**2
                output.append(kali)
        return output
bil = [2, 4, 5, 6]
kuadrat = kuadrat(bil)
print(kuadrat)
