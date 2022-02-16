from random import randint
oyundurumu= True
while oyundurumu :
    sayimiz = randint(0, 100)
    hakkimiz = 5

    while hakkimiz != 0 :
            girilen = int(input("Bir sayı giriniz:"))
            if girilen < sayimiz:
                hakkimiz -= 1
                print(hakkimiz, "can kaldı. Sayı daha BÜYÜK")
                continue
            elif girilen > sayimiz:
                hakkimiz -= 1
                print(hakkimiz, "can kaldı. Sayı daha KÜÇÜK" )
                continue
            else:
                print("tebrikler tutulan sayı {} idi , bildiniz..".format(sayimiz))
                break
    while hakkimiz == 0:
                 print("Üzgünüz yeniden deneyin... tutulan sayı {} idi".format(sayimiz))
                 break
    kontrol = input("devam etmek ister misiniz ? E-H : ")
    if kontrol == "e":
        oyundurumu = True
    else:
        oyundurumu = False
        print("yine bekleriz..")
        break