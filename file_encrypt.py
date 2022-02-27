import sys,os,colorama

from cryptography.fernet import Fernet

from colorama import Fore, Back, Style

colorama.init()

su = sys.platform

print(Fore.RED+"""BURDA ŞİFRELENEN YADA BAŞKA AMAÇLA KULLANANDAN SORUMLU DEĞİLİM SORUMLULUK KATİYEN KABUL ETMİYORUM!!!!! 

Deneme amaçlı key.txt yapın key.txt adlı dosyanız varsa silinir!!""")

if su == "linux":

    o = open("key.txt","w")

    o.write("hello")

    o.close()

    key3 = Fernet.generate_key()

    fer3 = Fernet(key3)

    print(Fore.RED+"unutma ==> \n "+str(key3))    

    gir = input(Fore.RED+"Şifrelenecek dosya: ")

    def sifre3():

           oku3 = open(gir,"rb")

           oku3 = oku3.read()

           yaz3 = open(gir, "wb") 

           paw3 = fer3.encrypt(oku3)

           yaz3.write(paw3)

           yaz3.close()

sifre3()

    

    

if su == "win32":

    o = open("key.txt","w")

    o.write("hello")

    o.close()

    key2 = Fernet.generate_key()

    fer2 = Fernet(key2)

    gir1 = input(Fore.RED+"Şifrelenecek dosya: ")

    print(Fore.RED+"unutma ==> \n "+str(key2))    

    oku2 = open(gir1,"rb")

    oku2 = oku2.read()

    yaz2 = open(gir1, "wb") 

    paw2 = fer2.encrypt(oku2)

    yaz2.write(paw2)

    yaz2.close()

        

        

if su == "darvin":

    o = open("key.txt","w")

    o.write("hello")

    o.close()

    key1 = Fernet.generate_key()

    fer1 = Fernet(key1)

    gir2 = input(Fore.RED+"Şifrelenecek dosya: ")

    print(Fore.RED+"unutma ==> \n "+str(key1))

    oku1 = open(gir2,"rb")

    oku1 = oku1.read()

    yaz1 = open(gir2,"wb")

    paw1 = fer.encrypt(oku1)

    yaz1.write(paw1)

    yaz1.close()
