import os
from scrap.getcontent import getarticle

def savelink():
    isi = getarticle(input("Link Article : "))
    isiberita = isi[0]
    isiberita = " ".join(isiberita)
    totalisi = len(isiberita.replace(" ",""))
    judul = isi[1]
    f = open("isi.txt","w")
    f.write(isiberita)
    f.close()
    return judul,totalisi

def process():
    title,total = savelink()
    os.system("python mapred.py isi.txt > tes.txt")
    read= open("tes.txt","r")
    file=read.readlines()[-10:]
    file.reverse()
    read.close()
    x = "="*20
    print("\n")
    print(f"Title : {title}\nTotal Word : {total}\n{x}")
    for res in file:
        print(f"{res}\n{x}")

if __name__ =="__main__":
    process()