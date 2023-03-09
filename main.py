# PYTHON VERİ TİPLERİ

#1 String(metin) veri tipleri:
    # Metinsel verileri saklamak için kullandığımız veri tipidir. Çift tırnak veya tek tırnak içerinde verileri saklarız.
kamp = "Python Kamp Günlükleri"
print(kamp)

#2 Numberik(Sayısal) veri tipleri:
    # Sayısal veri tiplerinin içerisindeki değerler sabit uzunluktadırlar. Sayısal verileri saklamak için kullanırız. 
    # int: Bellek üzerinde 4 byte yer kaplar ve tam sayı değerlerini barındırır.
    # long: Veri tipinin uzunluğu 64 bittir ve tam sayı değerlerini barındırır.
    # float: Uzunluğu 32 bittir ve ondalıklı sayı türünde verileri barındırır.
    # complex: Karmaşık sayıları içerisinde barındırır ve aynı zamanda gerçek ve sanal olmak üzere iki kısımdan oluşur.

#3 Sequence(Sıralama) veri tipleri
    #Python diline özel beri tipleri vardır.
    #list: Birden çok veri ögesi iceren veri yapılarıdır. İçerisinde veriler virgüllerle ayrılır ve köşeli parantez ile tanımlanır.,
    #tuple: List yapısına çok benzerdir fakat bazı farklılıkları bulunur. Köşeli parantez yerine normal parantez kullanılır ve değiştirilemez verilere sahiptir
#4 Mapping(Haritalama) veri tipleri
    # İçerisinde karma tablo yapıları bulunduran bir veri tipidir. Key ve value mantığıyla çalışır. İçerisinde verileri anahtar ve bu anahtara karşılık gelen değerler olarak tutar.
    #dictionary: Python dilinde dictionary olarak bilinir. Küme parantez kullanılarak oluşturulur.
#5 Boolean: Doğru veya yanlış, 0 veya 1  değerlerini döndüren bir veri tipidir. 

#------------------------------------------------------------------------------------------
#Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# Kurslarım, Tüm Kurslar, Kariyer, Sık Sorulan Sorular,© Kodlama.io 2023.,Kullanım Koşulları,Gizlilik Politikası => String
# Kategori, Eğitmen => List
# Password => int
# Full Name => String
# Aktif Üyelikleriniz kısmında abonelik adı, ÜCret, Kayıt Tarihi ve Eylemler kısımlarının altına yeni veriler eklenebilme durumu olduğu için o kısımda bir list yapısıdır. Kategorize edilmiş bir durum vardır.
# Notifications => Boolean tipinde bir veri tipinden oluşturulmuştur. İsteğe bağlı olarak açıp kapatabildiğimiz iki seçenekli bir buton vardır. Yes or No
# Kart bilgisi ekleme kısmında kart numarası, posta kodu cvc kodu vb kısımlar => int,
# Aynı kart bilgisi kısmında Ülke kısmı ise list veri tipinden oluşturulmuştur. Çünkü bir çok ülke ismi verilmiştir ve bunlar listelenmiştir.
# Fatura adresi kısmında ülke => list, açık adres => string, posta kodu => int,long
# Yine fatura adresi kısmında "teslimat adresi fatura ile aynı" kısmında tik işareti atmak veya atmamak gibi bir seçenek olduğu için boolean veri tipi olduğunu düşünüyorum.
# Are you a business? Enter your Tax ID kısmında bir karar yapısı vardır. If you are a business, enter your Tax ID.

#----------------------------------------------------------------------------------------------
#Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

soru = "Are you a business? Enter your Tax ID"
if soru== True:
    print("Tax ID giriniz")

#----
bitir_ve__devam_et = True
if bitir_ve__devam_et==True:
    print("Daire içi mavi olur")
else:
    print("Daire içi yarı mavi yarı beyaz kalsın")

