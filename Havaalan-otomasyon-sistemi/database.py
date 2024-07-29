import mysql.connector

# MySQL bağlantı bilgileri
mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="havaalani"
)
mycursor = mydb.cursor()

# CREATE DATABASE
mycursor.execute("CREATE DATABASE IF NOT EXISTS havaalani")
mydb.commit()






mycursor.execute("""
    CREATE TABLE IF NOT EXISTS yoneticigiris (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        KULLANICI_ADI VARCHAR(25) NOT NULL,
        KULLANICI_SOYADI VARCHAR(25) NOT NULL,
        SIFRE VARCHAR(16) NOT NULL,
        E_MAIL VARCHAR(50) NOT NULL
    )
""")
mydb.commit()


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS kayit (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        KULLANICI_ADI VARCHAR(25) NOT NULL,
        KULLANICI_SOYADI VARCHAR(25) NOT NULL,
        SIFRE VARCHAR(16) NOT NULL,
        E_MAIL VARCHAR(50) NOT NULL,
        CINSIYET VARCHAR(1),
        DOGUM_TARIHI DATE,
        TELEFON VARCHAR(20),
        ADRES VARCHAR(100)
    )
""")
mydb.commit()

mycursor.execute("""
 CREATE TABLE havaalani.kargo (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  GONDERICI_ISMI VARCHAR(50) NOT NULL,
  ALICI_ISMI VARCHAR(50) NOT NULL,
  KARGO_ADI VARCHAR(50) ,
  KARGO_AGIRLIK INT NOT NULL,
  GONDEREN_ID INT,               
  KARGO_ICERIK VARCHAR(150) NOT NULL
);
""")
mydb.commit()


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS sehir (
        ID INT PRIMARY KEY,
        ULKE_ID INT,
        SEHIR_ISMI VARCHAR(50),
        FOREIGN KEY (ULKE_ID) REFERENCES ulke(ID)
    )
""")
mydb.commit()


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS ilce (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        SEHIR_ID INT,
        ILCE_ISMI VARCHAR(50),
        FOREIGN KEY (SEHIR_ID) REFERENCES sehir(ID)
    )
""")
mydb.commit()


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS adres (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        KAYIT_ID INT,
        SEHIR_ID INT,
        ILCE_ID INT,
        POSTA_KOD VARCHAR(5),
        ULKE_ID INT,
        FOREIGN KEY (KAYIT_ID) REFERENCES kayit(ID),
        FOREIGN KEY (SEHIR_ID) REFERENCES sehir(ID),
        FOREIGN KEY (ILCE_ID) REFERENCES ilce(ID),
        FOREIGN KEY (ULKE_ID) REFERENCES ulke(ID)
    )
""")
mydb.commit()


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS calisanlar (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        CALISAN_AD VARCHAR(25),
        CALISAN_SOYAD VARCHAR(25),
        TELEFON VARCHAR(20),
        CINSIYET VARCHAR(1),
        MAAS INT,
        HAVAALANI_ID INT,
        POZISYON_ID  INT      
        
    )
""")
mydb.commit()

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS personelpozisyonu (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        POZISYON_ADI VARCHAR(50),
        MAAS_ARALIGI VARCHAR(40),
        ACIKLAMA VARCHAR(150),                  
        FOREIGN KEY (ID) REFERENCES calisanlar(POZISYON_ID)
    )
""")
mydb.commit()


mycursor.execute("""
CREATE TABLE havaalani.ucak_bilgi (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  UCAK_ID INT,
  UCAK_MARKA VARCHAR(50),
  UCAK_MODEL VARCHAR(20),
  YOLCU_KAPASITESI INT,
  YAKIT_TURU VARCHAR(20)
);
""")
mydb.commit()

# CREATE TABLE havaalani.ucaklar
mycursor.execute("""
 CREATE TABLE havaalani.ucaklar (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  MARKA_ID INT,
  KUYRUK_NUMARASI VARCHAR(20),
  KAPASITE INT,
  UCUS_MENZILI INT,
  MAKS_HIZ INT,
  ILK_UCUS_TARIHI DATE,
  EMEKLILIK_TARIHI DATE
);
""")
mydb.commit()

# CREATE TABLE havaalani.seferler
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS seferler (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        KALKIS_SEHIR_ID INT,
        VARIS_SEHIR_ID INT,
        UCAK_ID INT,
        KUYRUK_NO VARCHAR(30),
        KALKIS_ZAMANI DATETIME,
        BILET_TUTARI INT,
        YOLCU_SAYISI INT,
        FOREIGN KEY (KALKIS_SEHIR_ID) REFERENCES sehir(ID),
        FOREIGN KEY (VARIS_SEHIR_ID) REFERENCES sehir(ID),
        FOREIGN KEY (UCAK_ID) REFERENCES ucaklar(ID)
    )
""")
mydb.commit()

# CREATE TABLE havaalani.havaalanlari
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS havaalanlari (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        PLAKA INT,         
        HAVAALANI_AD VARCHAR(50),
        IL VARCHAR(20),
        ILCE VARCHAR(20),
        ULKE_ID  INT,
        FOREIGN KEY (ID) REFERENCES calisanlar(HAVAALANI_ID)         
    )
""")
mydb.commit()

# CREATE TABLE havaalani.odeme
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS odeme (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        KULLANICI_ID INT,
        BANKA VARCHAR(20),
        KART_ISIM VARCHAR (25),
        KART_NO VARCHAR (16),
        KART_SON_AY VARCHAR (3),
        KART_SON_YIL VARCHAR (4),
        KART_CVV VARCHAR (3),
        FOREIGN KEY (KULLANICI_ID) REFERENCES kayit(ID)
    )
""")
mydb.commit()


mycursor.execute("""
CREATE TABLE havaalani.paketdetay (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  PAKET_ADI VARCHAR(30) NOT NULL,
  KOLTUK_SECIMI VARCHAR(40),
  YEMEK_SECIMI VARCHAR(40),
  BAGAJ_HAKKI VARCHAR(40),
  DIGER_AVANTAJLAR VARCHAR(100)
);

""")
mydb.commit()


mycursor.execute("""
CREATE TABLE havaalani.biletler (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  YOLCU_ID INT,
  SEFER_ID INT,
  UCRET INT,
  FOREIGN KEY (YOLCU_ID) REFERENCES kayit(ID),
  FOREIGN KEY (SEFER_ID) REFERENCES seferler(ID)
);
""")
mydb.commit()