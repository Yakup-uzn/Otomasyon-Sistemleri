import mysql.connector

# Bağlantı bilgileri
baglan = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
}

try:
    # MySQL veritabanına bağlanma
    connection = mysql.connector.connect(**baglan)

    # Cursor oluşturma
    cursor = connection.cursor()

    # users veritabanını oluştur
    cursor.execute("CREATE DATABASE IF NOT EXISTS users")

    # Kullanıcı tablosunu oluştur
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users.kullanici (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            kullanici_adi VARCHAR(55),
            kullanici_sifre VARCHAR(55)
        )
    """)

    # Kayıt tablosunu oluştur
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users.kayit (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            kullanici_adi_soyadi VARCHAR(55),
            kullanici_AD VARCHAR(55),
            kullanici_sifre VARCHAR(255),
            kullanici_posta VARCHAR(255)
        )
    """)

    # Randevu tablosunu oluştur
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users.randevu (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            kullanici_adi VARCHAR(55),
            tckimlik VARCHAR(11),
            telefon VARCHAR(15),
            gun VARCHAR(15),
            ay VARCHAR(15),
            yil VARCHAR(15)
        )
    """)

except mysql.connector.Error as err:
    print(f"Hata: {err}")
finally:
    # Bağlantıyı kapat
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Bağlantı kapatıldı.")
