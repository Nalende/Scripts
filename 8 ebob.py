
devam = True
while devam:

    def ebob(a,b):
        bosListe=[]
        for i in range(1,(min(a,b)+1)):
            if a % i ==0 and b % i ==0:
                bosListe.append(i)

        print(max(bosListe))
        return i



    ilk = int(input("ilk sayıyı giriniz : "))
    ikinci = int(input("ikinci sayıyı giriniz : "))
    ebob(ilk,ikinci)



