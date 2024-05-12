#NUMPY
#Python üzerinde yüksek performanslı sayısal işlemler yapmak için kullanılır
#Numpy, Python'da bilimsel hesaplamalar için kullanılan bir kütüphanedir. Özellikle çok boyutlu diziler üzerinde yüksek performanslı matematiksel işlemler yapmak için idealdir.

import numpy as np
import time 


print(np.array([1,2,3,4,5,6]))     #burada en basit örneği ile bir dizi çağırılmış oldu

skaler = np.array(90)  #skaler boyutsuzdur
vektorel = np.array([1,2,3,4,5,6])   #vektorel tek boyutludur
matris = np.array([[1,2,3],[4,5,6],[7,8,9]])   #matris iki boyutludur
tensor = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])  #tensor üç boyutludur

print(skaler)
print(vektorel)
print(matris)
print(tensor)

print("Dizinin boyutu:", skaler.shape)
print("Dizinin boyutu:", vektorel.shape)
print("Dizinin boyutu:", matris.shape)      #shape , dizinin boyutunu bize verir
print("Dizinin boyutu:", tensor.shape)


print("Dizinin Türü:", type(skaler))  #türünü bize verir

sayi1 = np.array([1,2,3,4,5,6])
sayi2 = np.array([7,8,9,10,11,12])   #numpy üzerinde basit toplama işlemi 
toplam = sayi1 + sayi2
print("Toplam Sonucu:", toplam)
carp = sayi1 * 3    #numpy üzerinde basit bir çarpma işlemi
print("Sayi1 Çarpılmış Değerleri:", carp)


z1 = time.time()
liste = np.arange(1_000_000)**100
z2 = time.time()                    #burada neden numpy kütüphanesinin kullanılması gerektiğinin ispatı yapıldı
print(z2-z1)                        #python dan çok daha hızlı bir şekilde işlemleri gerçekleştirmektedir
                                    #burada bu test edilmiş oldu

vektor1 = np.array([0,1,2,3,4,5])
print(vektor1[1])
print(vektor1[0])   #burada numpy index değeri ile değerin hangi indexte yer aldığını bulabiliyoruz
print(vektor1[-1])


print(vektor1[1:4])
print(vektor1[:5])    #slice özelliği ise dizi içerisinden belli bir kısmın alınmasını sağlar
print(vektor1[1:6:2])

arr = np.array([[1, 2, 3],
                [4, 5, 6],      #çok boyutlu dizilerde slice işlemi yani dilimleme işlemi
                [7, 8, 9]])
print(arr[-1, :5])


vektor2 = np.array([1,2,3])
matris1 = np.array([[4,5,6],[7,8,9]])
print(vektor2)
print(matris1)
print(vektor2.size)     #burada size ifadesi bize toplam eleman sayısını döndürmektedir
print(matris1.size)

print(matris1.shape)    #bu ifade dizinin boyutlarını yani her boyutta kaç eleman olduğunu bize gösterir
print(vektor2.shape)

print(matris1.ndim)
print(vektor2.ndim)     #bu ifade dizinin kaç boyutlu olduğunu gösterir

print(matris1.dtype)
print(vektor2.dtype)    #bu ifade dizinin veri türünü bize verir(int,str vb.)


#NUMPY VERİ TİPİ DEĞİŞTİRME
sayilar = np.array([1,2,3,4,5,6])  #ilk önce biz bunu int formatında oluşturduk 
print(sayilar.dtype)

sayilar = np.array([1,2,3,4,5.0,6])   #sonra bunu float yaptık 
print(sayilar.dtype)

print(sayilar.astype("int32"))   #ve tekrardan türünü geri dönüştürmek istiyorsam 'astype' kullanırım
sayilar = np.array([1,2,3,4,5.0,6], dtype="int32")  #bu şekilde direk içinde de belirleyebiliriz
print(sayilar.dtype)


tarih = np.array(["2024-03-21"])
print(tarih.dtype)    #bir obje veri tipinden 
print(tarih.astype("datetime64"))   #burada ifadeyi tarih veri tipine dönüştürmüş olduk

#MATRİSLERDE SLICE OLUŞTURMA
matris2 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])  #matris oluşturma yapıldı
print(matris2)
print(matris2[0])
print(matris2[2])       #matrislerde slice işlemleri
print(matris2[1:4])
print(matris2[0, :2])  #virgülün sol tarafı satırları sağ tarafı sütunları seçer

#NUMPY'DA RANDOM MATRİS OLUŞTURMA 
print(dir(np.random))  #bütün metodları bana getirir 

print(np.random.randint(0,50))  #bu ifade rastgele tam sayılar getirilmesi için kullanılır
print(np.random.randint(0,50,(4,4)))  #bu ifade bize 4 tane matris getirir
print(np.random.randint(1,8,(3,3))) #bir ile sekiz arasında sayılar alır ve üçe üçlük bir matristen oluşur


print(np.arange(1,15))  #arange ifadesi ile aralık belirtmiş oluyoruz 
print(np.arange(1,15,3))


print(np.linspace(0,30,5))   #belirli bir aralıktaki sayıları belirli bir adette eşit aralıklarla içeren bir dizi oluşturmak için kullanılır
arr1 = np.linspace(0, 10, 3)
print(arr1)


m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m1.reshape(3,3))  #reshape metodu bir matrisin boyutunu değiştirmek için kullanılır
print(m1.reshape(9))



#PROJE1: RASTGELE MATRİS OLUŞTURMA VE İŞLEME ISI GRAFİĞİ OLUŞTURMA
import numpy as np
import matplotlib.pyplot as plt
mtr = np.random.randint(1,60,(4,4))   #matris oluşturuldu
print(mtr)
print(mtr.dtype)
print(mtr.astype)       #oluşturulan matrisin belirli özellikleri yazdırılmış oldu
print(mtr.size)
print(mtr.ndim)
print(mtr.shape)

ortalama = np.mean(mtr)   #mean ile matrisin ortalama değerini bulmuş olduk
print(ortalama)

toplam = np.sum(mtr)      #sum ile matrisin toplam değerini bulmuş olduk
print(toplam)

maximum = np.max(mtr)   #max ile matrisin en büyük değerini almış oluyoruz
minimum = np.min(mtr)   #min ifadesi ile matrisin en küçük değerini almış oluyoruz
print(maximum,minimum)

satir_toplami = np.sum(mtr, axis=1)  #matrisin satır toplamını bize verir
sutun_toplami = np.sum(mtr, axis=0)  #matrisin sütün toplamını bize verir
print(satir_toplami, sutun_toplami)

plt.imshow(mtr, cmap='hot', interpolation='nearest')
plt.colorbar()  # Renk ölçeği ekleme
plt.title('Matris Isı Haritası')    #oluşturulan matris ısı haritası olarak görselleştirilmiş oldu
plt.show()





#PROJE2:Matris Satır Toplamlarının Çizgi Grafiği Oluşturma
import numpy as np
import matplotlib.pyplot as plt

# 1. Rastgele Matris Oluşturma
matris = np.random.randint(1, 100, (6, 6))  # 6x6 boyutunda 1-100 arası rastgele sayılardan oluşan bir matris oluşturur

# 2. Her Satırın Toplamını Bulma
satir_toplamlari = np.sum(matris, axis=1)

# 3. Çizgi Grafiği Oluşturma
plt.plot(satir_toplamlari, marker='o', color='b', linestyle='-')
plt.title('Matris Satır Toplamları')
plt.xlabel('Satır Indeksleri')
plt.ylabel('Toplam Değerler')
plt.grid(True)  # Izgara ekleyerek grafiği daha okunabilir hale getirir
plt.show()
