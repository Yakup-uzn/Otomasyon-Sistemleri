import tkinter as tk
from tkinter import* 
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness() #farklı ekranlara geçince otomatik ölçeklendirmeyi iptal edebilmek için


app=customtkinter.CTk()
app.geometry("1100x900")
app.resizable(False,False)
app.title("OBS")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

global verilerim
global kullanici
global mycursor
global id
global mydb
global tree
buttons1 = ["Ögretmen ekle", "Hademe ekle", "Memur ekle", "Disiplin ekle","Sınıf ekle","Ögrenciyi sınıfa ekle","Şikayet görüntüle ögretmen","Şikayet görüntüle ögrenci", "Çıkış yap"]
func1 = ["Ogretmen_ekle", "Hademe_ekle", "Memur_ekle", "Disiplin_ekle","Sinif_ekle","Ogrenci_sinif_ekle","sikayet_goruntule_ogretmen","sikayet_goruntule_ogrenci","giris_yap"]
buttons = ["Ödev gör", "Disiplin var mı", "Şikayet ekle","Çıkış yap"]
func = ["Odev_gor", "Disiplin_kontrol", "Şikayet_ekle","giris_yap"]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()
		
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       
def database_bagla():
     global mydb
     mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="obs"
    )
     global mycursor
     mycursor = mydb.cursor()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_label(master, text,x, y):
    label = customtkinter.CTkLabel(master, text=text,font=('century gothic',17))
    label.place(x=x, y=y)
    return label

def create_button(master,text,x,y,fonk):
    button = customtkinter.CTkButton(master, text=text, anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b",command=fonk)
    button.place(x=x,y=y)
    return button


def verileri_listele(a):
    global id
    database_bagla()
    mycursor = mydb.cursor()

    # Veritabanındaki kayıtları seç
    mycursor.execute(a)
    kayıtlar = mycursor.fetchall()

    # Treeview'i temizle
    for row in tree.get_children():
        tree.delete(row)

    #mycursor kayıtları Treeview'e ekle
    for kayıtlar in kayıtlar:
        tree.insert("", "end", values=kayıtlar)

    mydb.close()

def verileri_listele2(a,deger):
    global id
    database_bagla()
    

    # Veritabanındaki kayıtları seç
    mycursor.execute(a,deger)
    kayıtlar = mycursor.fetchall()

    # Treeview'i temizle
    for row in tree.get_children():
        tree.delete(row)

    #mycursor kayıtları Treeview'e ekle
    for kayıtlar in kayıtlar:
        tree.insert("", "end", values=kayıtlar)

    mydb.close()    

def kullanici_():
     global kullanici
     global id
     global verilerim
     for row in verilerim:  
        kullanici=row[2]+ " " +row[3]
        id=row[0]
            

def bilgi():
        frame_sag_ust=customtkinter.CTkFrame(master=app,width=725,height=40,corner_radius=10)
        frame_sag_ust.place(x=350,y=25)
        my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(30,30))
        image_label = customtkinter.CTkLabel(frame_sag_ust, image=my_image,text="")
        image_label.place(x=680,y=5)
        label_text = tk.StringVar()
        label_text.set(kullanici)    
        label1=customtkinter.CTkLabel(frame_sag_ust,textvariable=label_text,font=('century gothic',17))
        label1.place(x=450,y=5)
        digerlabel_text = tk.StringVar()
        digerlabel_text.set(id)    
        label2=customtkinter.CTkLabel(frame_sag_ust,textvariable=digerlabel_text,font=('century gothic',17))
        label2.place(x=430,y=5)

def logo():
        frame_sol_ust=customtkinter.CTkFrame(master=app,width=300,height=120,corner_radius=10)
        frame_sol_ust.place(x=25,y=25)
        label1=customtkinter.CTkLabel(frame_sol_ust,text="ALTUN ÜNİVERSİTESİ",font=('century gothic',17))
        label1.place(x=120,y=50)
        my_image = customtkinter.CTkImage(dark_image=Image.open("logo.png"), size=(80,80))
        image_label = customtkinter.CTkLabel(frame_sol_ust, image=my_image,text="")
        image_label.place(x=20,y=20)
       
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def giris_yap():

        clear_widgets(app)
        app.tkraise()
        def giris_yap():
                global verilerim
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="obs"
                )

                mail=E_mail.get()
                password=Sifre.get()
                hangisisin=radio_var.get()


                if hangisisin == 1:
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT OGRENCI_ID,CINSIYET,OGRENCI_AD,OGRENCI_SOYAD,OGRENCI_TEL,OGRENCI_MAIL,OGRENCI_SIFRE FROM ogrenciler WHERE OGRENCI_MAIL=%s and OGRENCI_SIFRE=%s",(mail,password))
                
                        
                        verilerim = mycursor.fetchall() 
                        kullanici_()
                        if verilerim:
                                Odev_gor()
                        else:
                                # Veri bulunamadı, hata mesajı göster
                                messagebox.showerror("Hata", "Yanlış şifre veya kullanıcı adı!")
                elif hangisisin == 2:
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT VELI_ID,CINSIYET,VELI_AD,VELI_SOYAD,VELI_TEL,VELI_MAIL,VELI_SIFRE FROM veli WHERE VELI_MAIL=%s and VELI_SIFRE=%s",(mail,password))
                        
                        verilerim=mycursor.fetchall() 
                        kullanici_()

                        if verilerim:
                                aile()
                        else:
                                # Veri bulunamadı, hata mesajı göster
                                messagebox.showerror("Hata", "Yanlış şifre veya kullanıcı adı!")
                elif hangisisin == 3:
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT MUDUR_ID,CINSIYET,MUDUR_AD,MUDUR_SOYAD,MUDUR_TEL,MUDUR_MAIL,MUDUR_SIFRE FROM mudur WHERE MUDUR_MAIL=%s and MUDUR_SIFRE=%s",(mail,password))
                
                        verilerim=mycursor.fetchall() 
                        kullanici_()

                        if verilerim:
                                Ogretmen_ekle()
                        else:
                                # Veri bulunamadı, hata mesajı göster
                                messagebox.showerror("Hata", "Yanlış şifre veya kullanıcı adı!")
                elif hangisisin == 4:
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT OGRETMEN_ID,OKUL_ID,OGRETMEN_AD,OGRETMEN_SOYAD,OGRETMEN_TEL,OGRETMEN_MAIL,OGRETMEN_SIFRE FROM ogretmen WHERE OGRETMEN_MAIL=%s and OGRETMEN_SIFRE=%s",(mail,password))
                
                        verilerim=mycursor.fetchall() 
                        kullanici_()

                        if verilerim:
                                ders()
                        else:
                                # Veri bulunamadı, hata mesajı göster
                                messagebox.showerror("Hata", "Yanlış şifre veya kullanıcı adı!")


        img = Image.open("arkaplan.jpg")
        width, height = 1100, 900
        img_resized = img.resize((width, height), Image.LANCZOS)
        img1 = ImageTk.PhotoImage(img_resized)
        arkatema = tk.Label(master=app, image=img1)
        arkatema.pack()

        frame=customtkinter.CTkFrame(master=app,width=800,height=700,fg_color="gray21",corner_radius=20,bg_color="#282828")
        frame.place(x=150,y=100)

        label1=customtkinter.CTkLabel(master=frame,text="Hoşgeldiniz",font=('century gothic',35),text_color="white smoke")
        label1.place(x=310,y=100)

        label2=customtkinter.CTkLabel(master=frame,text="Giriş Yapınız",font=('century gothic',25),text_color="DarkSlateGray4")
        label2.place(x=330,y=180)

        E_mail=customtkinter.CTkEntry(master=frame,width=380,placeholder_text="E-mail",border_color="#f5f5f5",font=('Microsoft YaHei UI Lıght',30),text_color="white smoke")
        E_mail.place(x=205,y=250)

        Sifre=customtkinter.CTkEntry(master=frame,width=380,placeholder_text="Şifre",show="*",border_color="#f5f5f5",font=('Microsoft YaHei UI Lıght',30),text_color="white smoke")
        Sifre.place(x=205,y=330)

        radio_var = tk.IntVar(value=0)
        ogrenci_buton = customtkinter.CTkRadioButton(frame, text="Öğrenci ", variable= radio_var, value=1, font=('Microsoft YaHei UI Lıght',20), text_color="white smoke", hover_color="#b2b2b2", fg_color="#b2b2b2")
        ogrenci_buton.place(x=201,y=410)

        veli_buton = customtkinter.CTkRadioButton(frame, text="Veli ", variable= radio_var, value=2, font=('Microsoft YaHei UI Lıght',20), text_color="white smoke", hover_color="#b2b2b2", fg_color="#b2b2b2")
        veli_buton.place(x=306,y=410)

        mudur_buton = customtkinter.CTkRadioButton(frame, text="Müdür ", variable= radio_var, value=3, font=('Microsoft YaHei UI Lıght',20), text_color="white smoke", hover_color="#b2b2b2", fg_color="#b2b2b2")
        mudur_buton.place(x=375,y=410)

        ogretmen_buton = customtkinter.CTkRadioButton(frame, text="Öğretmen ", variable= radio_var, value=4, font=('Microsoft YaHei UI Lıght',20), text_color="white smoke", hover_color="#b2b2b2", fg_color="#b2b2b2")
        ogretmen_buton.place(x=467,y=410)

        label3=customtkinter.CTkLabel(master=frame,text="Hesabınız yok mu ?",font=('Microsoft YaHei UI Lıght',17),text_color="white smoke")
        label3.place(x=267,y=520)

        Button1=customtkinter.CTkButton(master=frame,text="hemen kayıt ol",width=50,fg_color="gray21",text_color="#528b8b",hover_color="gray21",font=('Microsoft YaHei UI Lıght',17), command=kayit)
        Button1.place(x=412,y=520)

        Button2=customtkinter.CTkButton(master=frame,text="Giriş",width=280,corner_radius=10,hover_color="#1c1c1c",fg_color="#528b8b",font=('Microsoft YaHei UI Lıght',25), command=giris_yap)
        Button2.place(x=255,y=480)

        app.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def kayit():


        clear_widgets(app)
        app.tkraise()
        def kayit_ol():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="obs"
            )

            mycursor = mydb.cursor()

            Ad=Kullanici_adi.get()
            Soyad=Kullanici_soyad.get()
            E_mail=Mail.get()
            Password=Sifre.get()
            Tel=telefon.get()
            adress=adres.get()
            ikametbas=ikamet_baslangic.get()
            ikametsure=ikamet_suresi.get()
            Cins=cinsiyet.get()
            veli_ogrenci=radio_var.get()

            dizi = [Ad,Soyad,E_mail,Password,Tel,adress,ikametbas,ikametsure,Cins]

            a = 1

            for i in dizi:
                if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                    messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!') 
                    a += 1 
                    break
            if a == 1:
                if veli_ogrenci == 1:
                    insert1 = "INSERT INTO ogrenciler (CINSIYET,OGRENCI_AD,OGRENCI_SOYAD,OGRENCI_TEL,OGRENCI_MAIL,OGRENCI_SIFRE) VALUES (%s, %s, %s, %s, %s, %s)"
                    degerler1 = (Cins,Ad,Soyad,Tel,E_mail,Password)
                    mycursor.execute(insert1, degerler1)
                    mydb.commit()

                    select = "SELECT OGRENCI_ID FROM ogrenciler WHERE OGRENCI_MAIL=%s"
                    mycursor.execute(select, (E_mail, ))
                    ogrenciminid = mycursor.fetchone()                   
                    
                    insert2 = "INSERT INTO ogrenciadres (OGRENCI_ID, IKAMET_BASLANGIC, IKAMET_SURESI, ADRES_DETAY) VALUES (%s, %s, %s, %s)"
                    degerler2 = (ogrenciminid[0],ikametbas,ikametsure,adress)
                    mycursor.execute(insert2, degerler2)
                    mydb.commit()
                    messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                else:
                    insert1 = "INSERT INTO veli (CINSIYET,VELI_AD,VELI_SOYAD,VELI_TEL,VELI_MAIL,VELI_SIFRE) VALUES (%s, %s, %s, %s, %s, %s)"
                    degerler1 = (Cins,Ad,Soyad,Tel,E_mail,Password)
                    mycursor.execute(insert1, degerler1)
                    mydb.commit()
                    
                    select = "SELECT VELI_ID FROM veli WHERE VELI_MAIL=%s"
                    mycursor.execute(select, (E_mail, ))
                    veliminid = mycursor.fetchone()

                    insert2 = "INSERT INTO veliadres (VELI_ID, IKAMET_BASLANGIC, IKAMET_SURESI, ADRES_DETAY) VALUES (%s, %s, %s, %s)"
                    degerler2 = (veliminid[0],ikametbas,ikametsure,adress)
                    mycursor.execute(insert2, degerler2)
                    mydb.commit()
                    messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                      

        img = Image.open("arkaplan.jpg")
        width, height = 1100, 900
        img_resized = img.resize((width, height), Image.LANCZOS)
        img1 = ImageTk.PhotoImage(img_resized)
        arkatema = tk.Label(master=app, image=img1)
        arkatema.pack()

        frame=customtkinter.CTkFrame(master=app,width=800,height=700,fg_color="gray21",corner_radius=20,bg_color="#282828")
        frame.place(x=150,y=100)

        label1=customtkinter.CTkLabel(master=frame,text="Hoşgeldiniz",font=('century gothic',30),text_color="white smoke")
        label1.place(x=415,y=40)

        label2=customtkinter.CTkLabel(master=frame,text="Kayıt Olunuz",font=('century gothic',20),text_color="DarkSlateGray4")
        label2.place(x=440,y=90)

        Kullanici_adi_label=customtkinter.CTkLabel(master=frame,text="Adınız :",font=('century gothic',20),text_color="DarkSlateGray4")
        Kullanici_adi_label.place(x=100,y=150)
        Kullanici_adi=customtkinter.CTkEntry(master=frame,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2", text_color="black")
        Kullanici_adi.place(x=300,y=150)

        Kullanici_soyad_label=customtkinter.CTkLabel(master=frame,text="Soyadınız :",font=('century gothic',20),text_color="DarkSlateGray4")
        Kullanici_soyad_label.place(x=100,y=200)
        Kullanici_soyad=customtkinter.CTkEntry(master=frame,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2", text_color="black")
        Kullanici_soyad.place(x=300,y=200)

        Mail_label=customtkinter.CTkLabel(master=frame,text="Mail :",font=('century gothic',20),text_color="DarkSlateGray4")
        Mail_label.place(x=100,y=250)
        Mail=customtkinter.CTkEntry(master=frame,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2", text_color="black")
        Mail.place(x=300,y=250)

        Sifre_label=customtkinter.CTkLabel(master=frame,text="Şifre :",font=('century gothic',20),text_color="DarkSlateGray4")
        Sifre_label.place(x=100,y=300)
        Sifre=customtkinter.CTkEntry(master=frame,width=380,border_color="white",show="*",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2", text_color="black")
        Sifre.place(x=300,y=300)

        telefon_label=customtkinter.CTkLabel(master=frame,text="Telefon :",font=('century gothic',20),text_color="DarkSlateGray4")
        telefon_label.place(x=100,y=350)
        telefon=customtkinter.CTkEntry(master=frame,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2", text_color="black")
        telefon.place(x=300,y=350)

        adres_label=customtkinter.CTkLabel(master=frame,text="Adres :",font=('century gothic',20),text_color="DarkSlateGray4")
        adres_label.place(x=100,y=400)
        adres=customtkinter.CTkEntry(master=frame,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2", text_color="black")
        adres.place(x=300,y=400)

        ikamet_baslangic_label=customtkinter.CTkLabel(master=frame,text="İkamet Başlangıç :",font=('century gothic',20),text_color="DarkSlateGray4")
        ikamet_baslangic_label.place(x=100,y=450)
        ikamet_baslangic=customtkinter.CTkEntry(master=frame,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2", text_color="black")
        ikamet_baslangic.place(x=300,y=450)

        ikamet_suresi_label=customtkinter.CTkLabel(master=frame,text="İkamet Süresi :",font=('century gothic',20),text_color="DarkSlateGray4")
        ikamet_suresi_label.place(x=100,y=500)
        ikamet_suresi=customtkinter.CTkEntry(master=frame,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2", text_color="black")
        ikamet_suresi.place(x=300,y=500)

        cinsiyet_label=customtkinter.CTkLabel(master=frame,text="Cinsiyet :",font=('century gothic',20),text_color="DarkSlateGray4")
        cinsiyet_label.place(x=100,y=550)
        cinsiyet=customtkinter.CTkComboBox(master=frame,values=["K","E"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
        cinsiyet.place(x=300,y=550)

        radio_var = tk.IntVar(value=0)
        ogrenci_buton = customtkinter.CTkRadioButton(frame, text="Öğrenci ", variable= radio_var, value=1, font=('Microsoft YaHei UI Lıght',19), text_color="white smoke", hover_color="#b2b2b2", fg_color="#b2b2b2")
        ogrenci_buton.place(x=480,y=552)

        veli_buton = customtkinter.CTkRadioButton(frame, text="Veli ", variable= radio_var, value=2, font=('Microsoft YaHei UI Lıght',19), text_color="white smoke", hover_color="#b2b2b2", fg_color="#b2b2b2")
        veli_buton.place(x=614,y=552)

        label3=customtkinter.CTkLabel(master=frame,text="Hesabınız var mı?",font=('Microsoft YaHei UI Lıght',15),text_color="white smoke")
        label3.place(x=380,y=640)

        Button_cikis=customtkinter.CTkButton(master=frame,text="hemen giriş yap",width=50,fg_color="gray21",text_color="#528b8b",hover_color="gray21",font=('Microsoft YaHei UI Lıght',15), command=giris_yap)
        Button_cikis.place(x=501,y=640)

        Button2=customtkinter.CTkButton(master=frame,text="Kayıt ol",width=280,corner_radius=10,hover_color="#1c1c1c",fg_color="#528b8b",font=('Microsoft YaHei UI Lıght',17), command=kayit_ol)
        Button2.place(x=355,y=610)  

        app.mainloop() 

#----------------------veli----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def aile():
        
        clear_widgets(app)
        app.tkraise()
        def aile_ekle():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="obs"
            )

            mycursor = mydb.cursor()

            aile=aile_adi.get()
            ailekisi=aile_kisi_sayisi.get()
            idm=ogrenci_id.get()
            
        
            
            a=1
            
            # Herhangi bir boşalan varmı kontrol sağlar
            dizi = [aile, ailekisi, idm]
            
            for i in dizi:
                if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                    messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                    a += 1
                    break

            #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
            if a == 1 :
                insert1 = "INSERT INTO aile (AILE_AD, AILE_KISI_SAYISI, OGRENCI_ID) VALUES (%s, %s, %s)"
                degerler1 = (aile, ailekisi, idm)
                mycursor.execute(insert1, degerler1)
                messagebox.showinfo("Bilgi", "Aile başarıyla eklendi")
                mydb.commit()
                mydb.close()


        def verileri_listele():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="obs"
            )
            mycursor = mydb.cursor()

            # Veritabanındaki kayıtları seç
            join = "SELECT AILE_ID, OGRENCI_ID, AILE_AD, AILE_KISI_SAYISI FROM aile"
            mycursor.execute(join)
            kayıtlar = mycursor.fetchall()

            # Treeview'i temizle
            for row in tree.get_children():
                tree.delete(row)

            #mycursor kayıtları Treeview'e ekle
            for kayıtlar in kayıtlar:
                tree.insert("", "end", values=kayıtlar)

            mydb.close()



        def kayit_sil():
            selected_item = tree.selection()

            if not selected_item:
                messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
                return

            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="obs"
                )
                mycursor = mydb.cursor()

                # Seçilen kaydın KALKIS_SEHIR_ID değerini al
                
                selected_id = tree.item(selected_item, 'values')[0]

                # Kaydı sil
                mycursor.execute("DELETE FROM aile WHERE AILE_ID = %s", (selected_id,))

                mydb.commit()
                mydb.close()

                # Kayıtları güncelle
                verileri_listele()
        
        
        
        



  
        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=489,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=271,corner_radius=10)
        frame_alt.place(x=350,y=600)

        logo()
        bilgi()

        button = customtkinter.CTkButton(frame_sol_alt, text="Aile ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=aile)
        button.place(x=40,y=50)

        button2 = customtkinter.CTkButton(frame_sol_alt, text="Aile bilgi ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=aile_bilgi)
        button2.place(x=40,y=100)

        button4 = customtkinter.CTkButton(frame_sol_alt, text="Çıkış yap", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=giris_yap)
        button4.place(x=40,y=650)

        header=customtkinter.CTkLabel(frame_sag_alt,text="AILE EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        ogrenci_id_label = customtkinter.CTkLabel(frame_sag_alt, text="Öğrenci ID :",font=('century gothic',17))
        ogrenci_id_label.place(x=50, y=100)
        ogrenci_id=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        ogrenci_id.place(x=200,y=100)

        aile_adi_label = customtkinter.CTkLabel(frame_sag_alt, text="Aile Adı :",font=('century gothic',17))
        aile_adi_label.place(x=50, y=150)
        aile_adi=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        aile_adi.place(x=200,y=150)

        aile_kisi_sayisi_label = customtkinter.CTkLabel(frame_sag_alt, text="Aile Kişi Sayısı :",font=('century gothic',17))
        aile_kisi_sayisi_label.place(x=50, y=200)
        aile_kisi_sayisi=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        aile_kisi_sayisi.place(x=200,y=200)
        
        Button1=customtkinter.CTkButton(frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b",command=aile_ekle)
        Button1.place(x=435,y=450)

        tree_columns = ("AILE_ID","OGRENCI_ID","AILE_AD","AILE_KISI_SAYISI")
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)
        
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=verileri_listele)
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",width=60, command=kayit_sil)
        button_sil.place(x=320, y=0)    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      
def aile_bilgi():
        clear_widgets(app)
        app.tkraise()
        def aile_bilgi_ekle():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="obs"
            )

            mycursor = mydb.cursor()

            anne=anne_adi.get()
            baba=baba_adi.get()
            annebaba=anne_baba.get()
            kardes=kardes_sayisi.get()
            evgelir=ev_geliri.get()
            idm=ogrenci_id.get()
            
            a=1
            
            # Herhangi bir boşalan varmı kontrol sağlar
            dizi = [anne, baba, annebaba, kardes, evgelir, idm]
            
            for i in dizi:
                if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                    messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                    a += 1
                    break

            #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
            if a == 1 :
                insert1 = "INSERT INTO ailebilgi (OGRENCI_ID ,ANNE_AD, BABA_AD, ANNE_BABA_AYRI_MI, KAC_KARDES, EV_GELIRI) VALUES (%s, %s, %s, %s, %s, %s)"
                degerler1 = (idm, anne, baba, annebaba, kardes, evgelir)
                mycursor.execute(insert1, degerler1)
                messagebox.showinfo("Bilgi", "Aile bilgisi başarıyla eklendi")
                mydb.commit()
                mydb.close()


        def verileri_listele():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="obs"
            )
            mycursor = mydb.cursor()

            # Veritabanındaki kayıtları seç
            join = "SELECT AILE_UYESI_ID, OGRENCI_ID, ANNE_AD, BABA_AD, ANNE_BABA_AYRI_MI, KAC_KARDES, EV_GELIRI FROM ailebilgi"
            mycursor.execute(join)
            kayıtlar = mycursor.fetchall()

            # Treeview'i temizle
            for row in tree.get_children():
                tree.delete(row)

            #mycursor kayıtları Treeview'e ekle
            for kayıtlar in kayıtlar:
                tree.insert("", "end", values=kayıtlar)

            mydb.close()



        def kayit_sil():
            selected_item = tree.selection()

            if not selected_item:
                messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
                return

            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="obs"
                )
                mycursor = mydb.cursor()

                # Seçilen kaydın KALKIS_SEHIR_ID değerini al
                
                selected_id = tree.item(selected_item, 'values')[0]

                # Kaydı sil
                mycursor.execute("DELETE FROM ailebilgi WHERE AILE_UYESI_ID = %s", (selected_id,))

                mydb.commit()
                mydb.close()

                # Kayıtları güncelle
                verileri_listele()
        
        
        
        





        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=489,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=271,corner_radius=10)
        frame_alt.place(x=350,y=600)

        logo()
        bilgi()

        button = customtkinter.CTkButton(frame_sol_alt, text="Aile ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=aile)
        button.place(x=40,y=50)

        button2 = customtkinter.CTkButton(frame_sol_alt, text="Aile bilgi ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=aile_bilgi)
        button2.place(x=40,y=100)

        button4 = customtkinter.CTkButton(frame_sol_alt, text="Çıkış yap", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=giris_yap)
        button4.place(x=40,y=650)

        header=customtkinter.CTkLabel(frame_sag_alt,text="AILE BILGI EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        ogrenci_id_label = customtkinter.CTkLabel(frame_sag_alt, text="Öğrenci ID :",font=('century gothic',17))
        ogrenci_id_label.place(x=50, y=100)
        ogrenci_id=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        ogrenci_id.place(x=200,y=100)

        anne_adi_label = customtkinter.CTkLabel(frame_sag_alt, text="Anne Adı :",font=('century gothic',17))
        anne_adi_label.place(x=50, y=150)
        anne_adi=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        anne_adi.place(x=200,y=150)

        baba_adi_label = customtkinter.CTkLabel(frame_sag_alt, text="Baba Adı :",font=('century gothic',17))
        baba_adi_label.place(x=50, y=200)
        baba_adi=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        baba_adi.place(x=200,y=200)

        anne_baba_label = customtkinter.CTkLabel(frame_sag_alt, text="Ebeveyn Ayrı Mı :",font=('century gothic',17))
        anne_baba_label.place(x=50, y=250)
        anne_baba=customtkinter.CTkComboBox(frame_sag_alt,values=["evet","hayır"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',17))
        anne_baba.place(x=200,y=250)

        kardes_sayisi_label = customtkinter.CTkLabel(frame_sag_alt, text="Kardeş Sayısı :",font=('century gothic',17))
        kardes_sayisi_label.place(x=50, y=300)
        kardes_sayisi=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        kardes_sayisi.place(x=200,y=300)

        ev_geliri_label = customtkinter.CTkLabel(frame_sag_alt, text="Ev Geliri :",font=('century gothic',17))
        ev_geliri_label.place(x=50, y=350)
        ev_geliri=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        ev_geliri.place(x=200,y=350)
        
        Button1=customtkinter.CTkButton(frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b",command=aile_bilgi_ekle)
        Button1.place(x=435,y=450)

        tree_columns = ("AILE_BILGI_ID","OGRENCI_ID","ANNE_AD","BABA_AD", "ANNE_BABA_AYRI_MI", "KARDES_SAYISI", "EV_GELIRI")
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)
        
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=verileri_listele)
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",width=60, command=kayit_sil)
        button_sil.place(x=320, y=0)

#----------------------ögretmen----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      
def ders():
        
        clear_widgets(app)
        app.tkraise()
        def ders_ve_konu_ekle():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="obs"
            )

            mycursor = mydb.cursor()

            ders=ders_adi.get()
            konu=ders_konusu.get()

            
        
            
            a=1
            
            # Herhangi bir boşalan varmı kontrol sağlar
            dizi = [ders, konu]
            
            for i in dizi:
                if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                    messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                    a += 1
                    break

            #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
            if a == 1 :
                insert1 = "INSERT INTO ders (DERS_ADI, DERS_KONUSU) VALUES (%s, %s)"
                degerler1 = (ders, konu)
                mycursor.execute(insert1, degerler1)
                messagebox.showinfo("Bilgi", "Ders adı ve konusu başarıyla eklendi")
                mydb.commit()
                mydb.close()


        def verileri_listele():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="obs"
            )
            mycursor = mydb.cursor()

            # Veritabanındaki kayıtları seç
            join = "SELECT DERS_ID, DERS_ADI, DERS_KONUSU FROM ders"
            mycursor.execute(join)
            kayıtlar = mycursor.fetchall()

            # Treeview'i temizle
            for row in tree.get_children():
                tree.delete(row)

            #mycursor kayıtları Treeview'e ekle
            for kayıtlar in kayıtlar:
                tree.insert("", "end", values=kayıtlar)

            mydb.close()



        def kayit_sil():
            selected_item = tree.selection()

            if not selected_item:
                messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
                return

            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="obs"
                )
                mycursor = mydb.cursor()

                # Seçilen kaydın KALKIS_SEHIR_ID değerini al
                
                selected_id = tree.item(selected_item, 'values')[0]

                # Kaydı sil
                mycursor.execute("DELETE FROM ders WHERE DERS_ID = %s", (selected_id,))

                mydb.commit()
                mydb.close()

                # Kayıtları güncelle
                verileri_listele()
        

        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)


        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=489,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=271,corner_radius=10)
        frame_alt.place(x=350,y=600)

        logo()
        bilgi()

        button = customtkinter.CTkButton(frame_sol_alt, text="Ders konusu ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=ders)
        button.place(x=40,y=50)

        button2 = customtkinter.CTkButton(frame_sol_alt, text="Ödev ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=odev)
        button2.place(x=40,y=100)

        button3 = customtkinter.CTkButton(frame_sol_alt, text="Şikayet ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=ogretmen_sikayet)
        button3.place(x=40,y=150)

        button4 = customtkinter.CTkButton(frame_sol_alt, text="Çıkış yap", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=giris_yap)
        button4.place(x=40,y=650)

        header=customtkinter.CTkLabel(frame_sag_alt,text="DERS KONUSU EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        ders_adi_label = customtkinter.CTkLabel(frame_sag_alt, text="Ders Adı :",font=('century gothic',17))
        ders_adi_label.place(x=50, y=100)
        ders_adi=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        ders_adi.place(x=200,y=100)

        ders_konusu_label = customtkinter.CTkLabel(frame_sag_alt, text="Ders Konusu :",font=('century gothic',17))
        ders_konusu_label.place(x=50, y=150)
        ders_konusu=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        ders_konusu.place(x=200,y=150)

        Button1=customtkinter.CTkButton(frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b", command=ders_ve_konu_ekle)
        Button1.place(x=435,y=450)

        tree_columns = ("DERS_ID","DERS_ADI","DERS_KONUSU")
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)

        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=verileri_listele)
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",width=60, command=kayit_sil)
        button_sil.place(x=320, y=0) 
      
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      
def odev():
        clear_widgets(app)
        app.tkraise()
        def odev_ekle():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="obs"
            )

            mycursor = mydb.cursor()

            ogrenci=ogrenci_id.get()
            verilis=verilis_tarih.get()
            teslim=teslim_tarih.get()
            icerik=odev_icerik.get()
            ders=ders_adi.get()
            konu=odev_konusu.get()
            yuzde=not_yuzdesi.get()

            
            a=1
            
            # Herhangi bir boşalan varmı kontrol sağlar
            dizi = [ogrenci, verilis, teslim, icerik, ders, konu, yuzde]
            
            for i in dizi:
                if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                    messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                    a += 1
                    break

            #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
            if a == 1 :
                insert1 = "INSERT INTO odev (OGRENCI_ID, VERILIS_TARIH, TESLIM_TARIH, ODEV_ICERIK, ODEV_KONUSU, NOT_YUZDESI, DERS_ADI) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                degerler1 = (ogrenci, verilis, teslim, icerik, konu, yuzde, ders)
                mycursor.execute(insert1, degerler1)
                messagebox.showinfo("Bilgi", "Ödev başarıyla eklendi")
                mydb.commit()
                mydb.close()


        def verileri_listele():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="obs"
            )
            mycursor = mydb.cursor()

            # Veritabanındaki kayıtları seç
            join = "SELECT ODEV_ID, OGRENCI_ID, VERILIS_TARIH, TESLIM_TARIH, ODEV_ICERIK, ODEV_KONUSU, NOT_YUZDESI, DERS_ADI FROM odev"
            mycursor.execute(join)
            kayıtlar = mycursor.fetchall()

            # Treeview'i temizle
            for row in tree.get_children():
                tree.delete(row)

            #mycursor kayıtları Treeview'e ekle
            for kayıtlar in kayıtlar:
                tree.insert("", "end", values=kayıtlar)

            mydb.close()



        def kayit_sil():
            selected_item = tree.selection()

            if not selected_item:
                messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
                return

            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="obs"
                )
                mycursor = mydb.cursor()

                # Seçilen kaydın KALKIS_SEHIR_ID değerini al
                
                selected_id = tree.item(selected_item, 'values')[0]

                # Kaydı sil
                mycursor.execute("DELETE FROM odev WHERE ODEV_ID = %s", (selected_id,))

                mydb.commit()
                mydb.close()

                # Kayıtları güncelle
                verileri_listele()
        
        

        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=489,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=271,corner_radius=10)
        frame_alt.place(x=350,y=600)

        logo()
        bilgi()

        button = customtkinter.CTkButton(frame_sol_alt, text="Ders konusu ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=ders)
        button.place(x=40,y=50)

        button2 = customtkinter.CTkButton(frame_sol_alt, text="Ödev ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=odev)
        button2.place(x=40,y=100)

        button3 = customtkinter.CTkButton(frame_sol_alt, text="Şikayet ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=ogretmen_sikayet)
        button3.place(x=40,y=150)

        button4 = customtkinter.CTkButton(frame_sol_alt, text="Çıkış yap", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=giris_yap)
        button4.place(x=40,y=650)

        header=customtkinter.CTkLabel(frame_sag_alt,text="ÖDEV EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        ogrenci_id_label = customtkinter.CTkLabel(frame_sag_alt, text="Öğrenci ID :",font=('century gothic',17))
        ogrenci_id_label.place(x=50, y=100)
        ogrenci_id=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        ogrenci_id.place(x=200,y=100)

        verilis_tarih_label = customtkinter.CTkLabel(frame_sag_alt, text="Veriliş Tarihi :",font=('century gothic',17))
        verilis_tarih_label.place(x=50, y=150)
        verilis_tarih=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        verilis_tarih.place(x=200,y=150)

        teslim_tarih_label = customtkinter.CTkLabel(frame_sag_alt, text="Teslim Tarihi :",font=('century gothic',17))
        teslim_tarih_label.place(x=50, y=200)
        teslim_tarih=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        teslim_tarih.place(x=200,y=200)

        odev_icerik_label = customtkinter.CTkLabel(frame_sag_alt, text="Ödev İçeriği :",font=('century gothic',17))
        odev_icerik_label.place(x=50, y=250)
        odev_icerik=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        odev_icerik.place(x=200,y=250)

        ders_adi_label = customtkinter.CTkLabel(frame_sag_alt, text="Ders Adı :",font=('century gothic',17))
        ders_adi_label.place(x=50, y=300)
        ders_adi=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        ders_adi.place(x=200,y=300)

        odev_konusu_label = customtkinter.CTkLabel(frame_sag_alt, text="Ödev Konusu :",font=('century gothic',17))
        odev_konusu_label.place(x=50, y=350)
        odev_konusu=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        odev_konusu.place(x=200,y=350)

        not_yuzdesi_label = customtkinter.CTkLabel(frame_sag_alt, text="Not Yüzdesi :",font=('century gothic',17))
        not_yuzdesi_label.place(x=50, y=400)
        not_yuzdesi=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        not_yuzdesi.place(x=200,y=400)

        Button1=customtkinter.CTkButton(frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b", command=odev_ekle)
        Button1.place(x=435,y=450)

        tree_columns = ("ODEV_ID","OGRENCI_ID","VERILIS_TARIH","TESLIM_TARIH","ODEV_ICERIK","DERS_ADI","DERS_KONUSU","NOT_YUZDESI")
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)

        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=verileri_listele)
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",width=60, command=kayit_sil)
        button_sil.place(x=320, y=0)  
      
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      
def ogretmen_sikayet():
        clear_widgets(app)
        app.tkraise()
        def ogretmen_sikayet_ekle():
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="obs"
            )

            mycursor = mydb.cursor()

            olusturma=olusturma_tarih.get()
            sikayet=sikayet_icerik.get("1.0",'end-1c')
            yorum=yorumunuz.get("1.0",'end-1c')

            
            a=1
            
            # Herhangi bir boşalan varmı kontrol sağlar
            dizi = [olusturma, sikayet, yorum]
            
            for i in dizi:
                if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                    messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                    a += 1
                    break

            #Girilen şehir ismi ve boş bir alan yoksa kayıt eder    
            if a == 1 :
                insert1 = "INSERT INTO ogretmensikayet (OLUSTURMA_TARIH, SIKAYET_ICERIK, OGRETMEN_YORUM) VALUES (%s, %s, %s)"
                degerler1 = (olusturma, sikayet, yorum)
                mycursor.execute(insert1, degerler1)
                messagebox.showinfo("Bilgi", "Şikayetiniz başarıyla eklendi")
                mydb.commit()
                mydb.close()


        def verileri_listele():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="obs"
            )
            mycursor = mydb.cursor()

            # Veritabanındaki kayıtları seç
            join = "SELECT SIKAYET_ID, OLUSTURMA_TARIH, SIKAYET_ICERIK, OGRETMEN_YORUM FROM ogretmensikayet"
            mycursor.execute(join)
            kayıtlar = mycursor.fetchall()

            # Treeview'i temizle
            for row in tree.get_children():
                tree.delete(row)

            #mycursor kayıtları Treeview'e ekle
            for kayıtlar in kayıtlar:
                tree.insert("", "end", values=kayıtlar)

            mydb.close()



        def kayit_sil():
            selected_item = tree.selection()

            if not selected_item:
                messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
                return

            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="obs"
                )
                mycursor = mydb.cursor()

                # Seçilen kaydın KALKIS_SEHIR_ID değerini al
                
                selected_id = tree.item(selected_item, 'values')[0]

                # Kaydı sil
                mycursor.execute("DELETE FROM ogretmensikayet WHERE SIKAYET_ID = %s", (selected_id,))

                mydb.commit()
                mydb.close()

                # Kayıtları güncelle
                verileri_listele()
        
        
        

        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)


        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=489,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=271,corner_radius=10)
        frame_alt.place(x=350,y=600)

        logo()


        bilgi()

        button = customtkinter.CTkButton(frame_sol_alt, text="Ders konusu ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=ders)
        button.place(x=40,y=50)

        button2 = customtkinter.CTkButton(frame_sol_alt, text="Ödev ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=odev)
        button2.place(x=40,y=100)

        button3 = customtkinter.CTkButton(frame_sol_alt, text="Şikayet ekle", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=ogretmen_sikayet)
        button3.place(x=40,y=150)

        button4 = customtkinter.CTkButton(frame_sol_alt, text="Çıkış yap", anchor="w",width=220,hover_color="#1c1c1c",fg_color="#528b8b", command=giris_yap)
        button4.place(x=40,y=650)

        header=customtkinter.CTkLabel(frame_sag_alt,text="ŞİKAYET EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        olusturma_tarih_label = customtkinter.CTkLabel(frame_sag_alt, text="Oluşturma Tarihi :",font=('century gothic',17))
        olusturma_tarih_label.place(x=50, y=100)
        olusturma_tarih=customtkinter.CTkEntry(frame_sag_alt,width=380,border_color="white")
        olusturma_tarih.place(x=200,y=100)

        sikayet_icerik_label = customtkinter.CTkLabel(frame_sag_alt, text="Şikayet içeriği :",font=('century gothic',17))
        sikayet_icerik_label.place(x=50, y=150)
        sikayet_icerik=customtkinter.CTkTextbox(frame_sag_alt,width=380,height=120,border_color="white",border_width=2)
        sikayet_icerik.place(x=200,y=150)

        yorumunuz_label = customtkinter.CTkLabel(frame_sag_alt, text="Yorumunuz :",font=('century gothic',17))
        yorumunuz_label.place(x=50, y=300)
        yorumunuz=customtkinter.CTkTextbox(frame_sag_alt,width=380,height=120,border_color="white",border_width=2)
        yorumunuz.place(x=200,y=300)

        Button1=customtkinter.CTkButton(frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b", command=ogretmen_sikayet_ekle)
        Button1.place(x=435,y=450)

        tree_columns = ("SIKAYET_ID", "OLUSTURMA_TARIH", "SIKAYET_ICERIK", "OGRETMEN_YORUM")
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)

        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=verileri_listele)
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",width=60, command=kayit_sil)
        button_sil.place(x=320, y=0)

#--------------------müdür------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Memur_ekle():
        clear_widgets(app)
        app.tkraise()
      
        def insert():

            database_bagla()
            a = 1
            ad=Kullanici_adi.get()
            soyad=Kullaci_soyad.get()
            tel=Telefon.get()
            cins=Cinsiyet.get()

            dizi= [ad,soyad,tel,cins]
            for i in dizi:
        
                if i.strip() == '':
                    messagebox.showwarning('Uyarı', 'Lütfen Boş Alan Bırakmayın!')
                    a += 1
                    break

                insert_query = "INSERT INTO memur (OKUL_ID,MEMUR_AD,MEMUR_SOYAD,MEMUR_TEL, CINSIYET) VALUES (%s, %s, %s, %s, %s)"
                degerler=(1,ad,soyad,tel,cins)
                mycursor.execute(insert_query,degerler)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                mydb.commit()
                mydb.close()

        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
                        messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
                        return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
                        database_bagla()
                        mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            selected_id = tree.item(selected_item, 'values')[0]

            # Kaydı sil
            mycursor.execute("DELETE FROM memur WHERE MEMUR_ID = %s", (selected_id,))


            mydb.commit()
            mydb.close()
            verileri_listele(SQL1)        




        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)



        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=489,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=271,corner_radius=10)
        frame_alt.place(x=350,y=600)

        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150, 200,250,300,350,400,650]
        for button, y, fun in zip(buttons1, yb_konumu, func1):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------

        bilgi()

        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------
        header=customtkinter.CTkLabel(frame_sag_alt,text="MEMUR EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        yl_konumu = [100, 150, 200, 250]
        labels = ["Adınız :", "Soyadınız :","Telefon :", "Cinsiyet :"]

        for label, y in zip(labels, yl_konumu):
            create_label(frame_sag_alt,label,50,y)
            
    


        Kullanici_adi=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Kullanici_adi.place(x=200,y=100)

        Kullaci_soyad=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Kullaci_soyad.place(x=200,y=150)


        Telefon=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Telefon.place(x=200,y=200)
            

        Cinsiyet=customtkinter.CTkComboBox(master=frame_sag_alt,values=["K","E"],width=150,border_color="white")
        Cinsiyet.place(x=200,y=250)




        Button1=customtkinter.CTkButton(master=frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b",command=insert)
        Button1.place(x=435,y=450)


        # Treeview widget'i oluştur
        global tree
        tree_columns = ("MEMUR_ID","MEMUR_AD", "MEMUR_SOYAD","MEMUR_TEL" )
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)
        
        
        SQL1="SELECT MEMUR_ID,MEMUR_AD, MEMUR_SOYAD,MEMUR_TEL  FROM memur"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL1))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def Hademe_ekle():
        
        clear_widgets(app)
        app.tkraise()
        
        def insert():

            database_bagla()
            a = 1
            ad=Kullanici_adi.get()
            soyad=Kullaci_soyad.get()
            tel=Telefon.get()
            cins=Cinsiyet.get()

            dizi= [ad,soyad,tel,cins]
            for i in dizi:
        
                if i.strip() == '':
                    messagebox.showwarning('Uyarı', 'Lütfen Boş Alan Bırakmayın!')
                    a += 1
                    break

                insert_query = "INSERT INTO hademe (OKUL_ID,HADEME_AD,HADEME_SOYAD,HADEME_TEL, CINSIYET) VALUES (%s, %s, %s, %s, %s)"
                degerler=(1,ad,soyad,tel,cins)
                mycursor.execute(insert_query,degerler)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                mydb.commit()
                mydb.close()

        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
              messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
              return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
               database_bagla()
               mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            selected_id = tree.item(selected_item, 'values')[0]

            # Kaydı sil
            mycursor.execute("DELETE FROM hademe WHERE HADEME_ID = %s", (selected_id,))


            mydb.commit()
            mydb.close()
            verileri_listele(SQL2)        


        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)


        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=489,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=271,corner_radius=10)
        frame_alt.place(x=350,y=600)

        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150, 200,250,300,350,400,650]
        for button, y, fun in zip(buttons1, yb_konumu, func1):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------
        bilgi()
        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------
        header=customtkinter.CTkLabel(frame_sag_alt,text="HADEME EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        yl_konumu = [100, 150, 200, 250]
        labels = ["Adınız :", "Soyadınız :","Telefon :", "Cinsiyet :"]

        for label, y in zip(labels, yl_konumu):
            create_label(frame_sag_alt,label,50,y)
            
    


        Kullanici_adi=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Kullanici_adi.place(x=200,y=100)

        Kullaci_soyad=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Kullaci_soyad.place(x=200,y=150)


        Telefon=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Telefon.place(x=200,y=200)
            

        Cinsiyet=customtkinter.CTkComboBox(master=frame_sag_alt,values=["K","E"],width=150,border_color="white")
        Cinsiyet.place(x=200,y=250)




        Button1=customtkinter.CTkButton(master=frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b",command=insert)
        Button1.place(x=435,y=450)

        # Treeview widget'i oluştur
        global tree
        tree_columns = ("HADEME_ID","HADEME_AD", "HADEME_SOYAD","HADEME_TEL" )
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)
        
        
        SQL2="SELECT HADEME_ID,HADEME_AD, HADEME_SOYAD,HADEME_TEL  FROM hademe"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL2))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Ogretmen_ekle():
        clear_widgets(app)
        app.tkraise()

        def insert():

            database_bagla()
            a = 1
            ad=Kullanici_adi.get()
            soyad=Kullaci_soyad.get()
            mail=Mail.get()
            password=Sifre.get()
            tel=Telefon.get()
            cins=Cinsiyet.get()

            dizi= [ad,soyad,mail,password,tel,cins]
            for i in dizi:
        
                if i.strip() == '':
                    messagebox.showwarning('Uyarı', 'Lütfen Boş Alan Bırakmayın!')
                    a += 1
                    break

                insert_query = "INSERT INTO ogretmen (OKUL_ID, OGRETMEN_AD, OGRETMEN_SOYAD, OGRETMEN_MAIL, OGRETMEN_SIFRE, OGRETMEN_TEL, CINSIYET) VALUES (%s, %s, %s, %s, %s, %s,%s)"
                degerler=(1,ad,soyad,mail,password,tel,cins)
                mycursor.execute(insert_query,degerler)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                mydb.commit()
                mydb.close()

        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
              messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
              return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
                    database_bagla()
                    mycursor = mydb.cursor()

                    # Seçilen kaydın KALKIS_SEHIR_ID değerini al
                    selected_id = tree.item(selected_item, 'values')[0]

                    # Kaydı sil
                    mycursor.execute("DELETE FROM ogretmen WHERE OGRETMEN_ID = %s", (selected_id,))


                    mydb.commit()
                    mydb.close()
                    verileri_listele(SQL)
            



        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=489,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=271,corner_radius=10)
        frame_alt.place(x=350,y=600)

        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150, 200,250,300,350,400,650]
        for button, y, fun in zip(buttons1, yb_konumu, func1):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------
        bilgi()
        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------
        header=customtkinter.CTkLabel(frame_sag_alt,text="ÖGRETMEN EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        yl_konumu = [100, 150, 200, 250, 300, 350, 400]
        labels = ["Adınız :", "Soyadınız :", "Mail :","Şifre :", "Telefon :", "Cinsiyet :"]

        for label, y in zip(labels, yl_konumu):
            create_label(frame_sag_alt,label,50,y)
            
    


        Kullanici_adi=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Kullanici_adi.place(x=200,y=100)

        Kullaci_soyad=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Kullaci_soyad.place(x=200,y=150)

        Mail=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Mail.place(x=200,y=200)

        Sifre=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Sifre.place(x=200,y=250)

        Telefon=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Telefon.place(x=200,y=300)
            

        Cinsiyet=customtkinter.CTkComboBox(master=frame_sag_alt,values=["K","E"],width=150,border_color="white")
        Cinsiyet.place(x=200,y=350)




        Button1=customtkinter.CTkButton(master=frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b",command=insert)
        Button1.place(x=435,y=440)



        # Treeview widget'i oluştur
        global tree
        tree_columns = ("OGRETMEN_ID","OGRETMEN_AD", "OGRETMEN_SOYAD", "OGRETMEN_MAIL","OGRETMEN_SIFRE","OGRETMEN_TEL" )
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)
        
        
        SQL="SELECT OGRETMEN_ID,OGRETMEN_AD, OGRETMEN_SOYAD, OGRETMEN_MAIL,OGRETMEN_SIFRE,OGRETMEN_TEL  FROM ogretmen"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0)  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def Disiplin_ekle():
        clear_widgets(app)
        app.tkraise()
        def insert():
            

            database_bagla()
            a = 1
            ad=Kullanici_adi.get()
            soyad=Kullaci_soyad.get()
            ogrenci_no=No.get()
            suc=İşledigi_suc.get("1.0",'end-1c')
            ceza=Ceza.get()
        

            dizi= [ad,soyad,ogrenci_no,suc,ceza]
            for i in dizi:
        
                if i.strip() == '':
                    messagebox.showwarning('Uyarı', 'Lütfen Boş Alan Bırakmayın!')
                    a += 1
                    break

                insert_query = "INSERT INTO disiplin (OGRENCI_ID,OGRENCI_AD, OGRENCI_SOYAD,ISLEDIGI_SUC,CEZA) VALUES (%s, %s, %s, %s, %s)"
                degerler=(ogrenci_no,ad,soyad,suc,ceza)
                mycursor.execute(insert_query,degerler)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                mydb.commit()
                mydb.close()


        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
              messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
              return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
               database_bagla()
               mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            selected_id = tree.item(selected_item, 'values')[0]

            # Kaydı sil
            mycursor.execute("DELETE FROM disiplin WHERE DISIPLIN_ID = %s", (selected_id,))


            mydb.commit()
            mydb.close()
            verileri_listele(SQL3)        


        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=589,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=246,corner_radius=10)
        frame_alt.place(x=350,y=625)


        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150, 200,250,300,350,400,650]
        for button, y, fun in zip(buttons1, yb_konumu, func1):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------
        bilgi()
        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------
        header=customtkinter.CTkLabel(frame_sag_alt,text="DİSİPLİN EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        yl_konumu = [100, 150, 200,250,400]
        labels = ["Adınız :", "Soyadınız :","Ögrenci no :", "İşlediği suç :","Ceza :",]

        for label, y in zip(labels, yl_konumu):
            create_label(frame_sag_alt,label,50,y)
            
    


        Kullanici_adi=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Kullanici_adi.place(x=200,y=100)

        Kullaci_soyad=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Kullaci_soyad.place(x=200,y=150)

        No=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        No.place(x=200,y=200)

        İşledigi_suc=customtkinter.CTkTextbox(master=frame_sag_alt,width=380,height=120,border_color="white")
        İşledigi_suc.place(x=200,y=250)


        Ceza=customtkinter.CTkComboBox(master=frame_sag_alt,values=["15 gün okuldan uzaklaştrma","Kınama","Okuldan atılma","1 hafta okuldan uzaklaştırma"],width=380,border_color="white")
        Ceza.place(x=200,y=400)



        Button1=customtkinter.CTkButton(master=frame_sag_alt,text="Disipline yolla",hover_color="#1c1c1c",fg_color="#528b8b",command=insert)
        Button1.place(x=435,y=450)

        # Treeview widget'i oluştur
        global tree
        tree_columns = ("DISIPLIN_ID","OGRENCI_AD", "OGRENCI_SOYAD","CEZA" )
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)
        
        global SQL3
        SQL3="SELECT DISIPLIN_ID,OGRENCI_AD,OGRENCI_SOYAD,CEZA  FROM disiplin"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL3))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Sinif_ekle():
        clear_widgets(app)
        app.tkraise()
      
        def insert():

            database_bagla()
            a = 1
            kod=Sınıf_kod.get()
            ad=Sınıf_ad.get()
            acılıs=Sınıf_acılıs.get()
    

            dizi= [kod,ad,acılıs]
            for i in dizi:
        
                if i.strip() == '':
                    messagebox.showwarning('Uyarı', 'Lütfen Boş Alan Bırakmayın!')
                    a += 1
                    break

                

                insert_query = "INSERT INTO sinif (SINIF_KOD,SINIF_AD,SINIF_ACILIS) VALUES (%s, %s, %s)"
                degerler=(kod,ad,acılıs)
                mycursor.execute(insert_query,degerler)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt alındı")
                mydb.commit()
                mydb.close()

        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
              messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
              return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
               database_bagla()
               mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            selected_id = tree.item(selected_item, 'values')[0]

            # Kaydı sil
            mycursor.execute("DELETE FROM sinif WHERE SINIF_KOD = %s", (selected_id,))


            mydb.commit()
            mydb.close()
            verileri_listele(SQL4)        


        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=389,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=371,corner_radius=10)
        frame_alt.place(x=350,y=500)

        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150, 200,250,300,350,400,650]
        for button, y, fun in zip(buttons1, yb_konumu, func1):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------
        bilgi()
        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------
        header=customtkinter.CTkLabel(frame_sag_alt,text="SINIF EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        yl_konumu = [100, 150, 200]
        labels = ["Sınıf kod :", "Sınıf ad :","Sınıf açılış :"]

        for label, y in zip(labels, yl_konumu):
            create_label(frame_sag_alt,label,50,y)
            
    


        Sınıf_kod=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Sınıf_kod.place(x=200,y=100)

        Sınıf_ad=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Sınıf_ad.place(x=200,y=150)


        Sınıf_acılıs=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Sınıf_acılıs.place(x=200,y=200)
            

        Button1=customtkinter.CTkButton(master=frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b",command=insert)
        Button1.place(x=435,y=350)


        # Treeview widget'i oluştur
        global tree
        tree_columns = ("SINIF_KOD","SINIF_AD","SINIF_ACILIS")
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=400)
        
        global SQL4
        SQL4="SELECT SINIF_KOD,SINIF_AD,SINIF_ACILIS  FROM sinif"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL4))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Ogrenci_sinif_ekle():
        clear_widgets(app)
        app.tkraise()
      
        def insert():

            database_bagla()
            a = 1
            kod=Sınıf_kod.get()
            idm=ogrenci_id.get()
    

            dizi= [kod, idm]
            for i in dizi:
        
                if i.strip() == '':
                    messagebox.showwarning('Uyarı', 'Lütfen Boş Alan Bırakmayın!')
                    a += 1
                    break

                
                select = "SELECT SINIF_ID FROM sinif WHERE SINIF_KOD=%s"
                mycursor.execute(select, (kod, ))
                SINIF_IDIM=mycursor.fetchone()[0]

                insert_query = "INSERT INTO ogrencisinif (OGRENCI_ID,SINIF_ID) VALUES (%s, %s)"
                deger=(idm,SINIF_IDIM)
                mycursor.execute(insert_query,deger)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt alındı")
                mydb.commit()
                mydb.close()

        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
              messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
              return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
               database_bagla()
               mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            selected_id = tree.item(selected_item, 'values')[0]

            # Kaydı sil
            mycursor.execute("DELETE FROM ogrencisinif WHERE SINIF_ID = %s", (selected_id,))


            mydb.commit()
            mydb.close()
            verileri_listele(SQL5)        

        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=389,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=371,corner_radius=10)
        frame_alt.place(x=350,y=500)

        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150, 200,250,300,350,400,650]
        for button, y, fun in zip(buttons1, yb_konumu, func1):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------
        bilgi()
        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------
        header=customtkinter.CTkLabel(frame_sag_alt,text="ÖGRENCİYİ SINIFA EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        yl_konumu = [100, 150]
        labels = ["Öğrenci ID :", "Sınıf kod :"]

        for label, y in zip(labels, yl_konumu):
            create_label(frame_sag_alt,label,50,y)
            
    
        ogrenci_id=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        ogrenci_id.place(x=200,y=100)

        Sınıf_kod=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        Sınıf_kod.place(x=200,y=150)
            

        Button1=customtkinter.CTkButton(master=frame_sag_alt,text="Kayıt ekle",hover_color="#1c1c1c",fg_color="#528b8b",command=insert)
        Button1.place(x=435,y=350)


        # Treeview widget'i oluştur
        global tree
        tree_columns = ("OGRENCI_ID","SINIF KOD","SINIF AD","SINIF AÇILIŞ")
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=400)
        
        global SQL5
        SQL5="SELECT O.OGRENCI_ID, S.SINIF_KOD, S.SINIF_AD, S.SINIF_ACILIS FROM ogrencisinif O INNER JOIN sinif S ON S.SINIF_ID=O.SINIF_ID"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL5))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sikayet_goruntule_ogretmen():
        clear_widgets(app)
        app.tkraise()


        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
              messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
              return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
               database_bagla()
               mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            selected_id = tree.item(selected_item, 'values')[0]

            # Kaydı sil
            mycursor.execute("DELETE FROM ogretmensikayet WHERE SIKAYET_ID = %s", (selected_id,))


            mydb.commit()
            mydb.close()
            verileri_listele(SQL6)        


        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=790,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)




        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150, 200,250,300,350,400,650]
        for button, y, fun in zip(buttons1, yb_konumu, func1):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------
        bilgi()
        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------

        # Treeview widget'i oluştur
        global tree
        tree_columns = ("SIKAYET_ID","SIKAYET_ICERIK","OGRETMEN_YORUM","OLUSTURMA_TARIHI" )
        tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=790)
        
        global SQL6
        SQL6="SELECT SIKAYET_ID,SIKAYET_ICERIK,OGRETMEN_YORUM,OLUSTURMA_TARIH  FROM ogretmensikayet"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL6))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def sikayet_goruntule_ogrenci():
        clear_widgets(app)
        app.tkraise()


        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
              messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
              return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
               database_bagla()
               mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            selected_id = tree.item(selected_item, 'values')[0]

            # Kaydı sil
            mycursor.execute("DELETE FROM ogrencisikayet WHERE SIKAYET_ID = %s", (selected_id,))


            mydb.commit()
            mydb.close()
            verileri_listele(SQL7)        


        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)

        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=790,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)




        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150, 200,250,300,350,400,650]
        for button, y, fun in zip(buttons1, yb_konumu, func1):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------
        bilgi()
        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------

        # Treeview widget'i oluştur
        global tree
        tree_columns = ("SIKAYET_ID","SIKAYET_ICERIK","OGRENCI_YORUM","OLUSTURMA_TARIHI" )
        tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=790)
        
        global SQL7
        SQL7="SELECT SIKAYET_ID,SIKAYET_ICERIK,OGRENCI_YORUM,OLUSTURMA_TARIH  FROM ogrencisikayet"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL7))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0)

#-----------------ögrenci---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def Disiplin_kontrol():
        clear_widgets(app)
        app.tkraise()
        

            
        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)


        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=790,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)


        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150,650]
        for button, y, fun in zip(buttons, yb_konumu, func):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------

        bilgi()
        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------
    

            
    



        # Treeview widget'i oluştur
        global tree
        tree_columns = ("OGRENCI_ID","ISLEDIGI_SUC","CEZA")
        tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=790)
        
        global SQL9
        SQL9="SELECT OGRENCI_ID,ISLEDIGI_SUC,CEZA FROM disiplin WHERE OGRENCI_ID=%s"
        degerler = (id,)
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_sag_alt, text="Güncelle",width=110, command=lambda:verileri_listele2(SQL9,degerler))
        button_listele.place(x=0, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Odev_gor():
        clear_widgets(app)
        app.tkraise()


        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)


        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=790,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)


        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150,650]
        for button, y, fun in zip(buttons, yb_konumu, func):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------
        bilgi()


        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------

        # Treeview widget'i oluştur
        global tree
        tree_columns = ("OGRENCI ID","DERS ADI","VERILIS TARIH","TESLIM TARIH","ODEV ICERIK","ODEV KONUSU","NOT YUZDESI")
        tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=790)
        
        kullanici_()
        SQL="SELECT OGRENCI_ID,DERS_ADI,VERILIS_TARIH,TESLIM_TARIH,ODEV_ICERIK,ODEV_KONUSU,NOT_YUZDESI FROM odev WHERE OGRENCI_ID=%s"
        degerler = (id,)
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_sag_alt, text="Güncelle",width=110, command=lambda:verileri_listele2(SQL,degerler))
        button_listele.place(x=0, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def Şikayet_ekle():
        clear_widgets(app)
        app.tkraise()
        def insert():
            

            database_bagla()
            a = 1
            Tarih=tarih.get()
            Sikayet=sikayet.get("1.0",'end-1c')
            Yorum=yorumunuz.get("1.0",'end-1c')


            dizi= [Tarih,Sikayet,Yorum]
            for i in dizi:
        
                if i.strip() == '':
                    messagebox.showwarning('Uyarı', 'Lütfen Boş Alan Bırakmayın!')
                    a += 1
                    break

                insert_query = "INSERT INTO ogrencisikayet (OLUSTURMA_TARIH,SIKAYET_ICERIK,OGRENCI_YORUM) VALUES (%s, %s, %s)"
                degerler=(Tarih,Sikayet,Yorum)
                mycursor.execute(insert_query,degerler)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                mydb.commit()
                mydb.close()


        def kayit_sil():
        
            selected_item = tree.selection()

            if not selected_item:
              messagebox.showwarning("Uyarı", "Lütfen silinecek bir kayıt seçin.")
              return
 
            confirm = messagebox.askyesno("Onay", "Seçili kaydı silmek istiyor musunuz?")

            if confirm:
               database_bagla()
               mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            selected_id = tree.item(selected_item, 'values')[0]

            # Kaydı sil
            mycursor.execute("DELETE FROM ogrencisikayet WHERE SIKAYET_ID = %s", (selected_id,))


            mydb.commit()
            mydb.close()
            verileri_listele(SQL)        


        frame_sol_alt=customtkinter.CTkFrame(master=app,width=300,height=705,corner_radius=10)
        frame_sol_alt.place(x=25,y=170)


        frame_sag_alt=customtkinter.CTkFrame(master=app,width=725,height=589,corner_radius=10)
        frame_sag_alt.place(x=350,y=85)

        frame_alt=customtkinter.CTkFrame(master=app,width=725,height=246,corner_radius=10)
        frame_alt.place(x=350,y=625)


        #-------------------------------------------------------- frame sol ust ----------------------------------------------------------------------------------------------------------------------------------------
        logo()
        #-------------------------------------------------------- frame sol alt ----------------------------------------------------------------------------------------------------------------------------------------

        yb_konumu = [50,100, 150,650]
        for button, y, fun in zip(buttons, yb_konumu, func):
             [create_button(frame_sol_alt, button, 40, y, globals()[fun])]  
            

        #-------------------------------------------------------- frame sag ust ----------------------------------------------------------------------------------------------------------------------------------------

        bilgi()

        #-------------------------------------------------------- frame sag alt ----------------------------------------------------------------------------------------------------------------------------------------
        header=customtkinter.CTkLabel(frame_sag_alt,text="ŞİKAYET EKLE",font=('century gothic',17))
        header.place(x=325,y=40)

        yl_konumu = [100,200,360]
        labels = ["Oluşturma tarihi :", "Yorumunuz :","Şikayetiniz :"]

        for label, y in zip(labels, yl_konumu):
            create_label(frame_sag_alt,label,50,y)
            
    
        tarih=customtkinter.CTkEntry(master=frame_sag_alt,width=380,border_color="white")
        tarih.place(x=200,y=100)
        
        sikayet=customtkinter.CTkTextbox(master=frame_sag_alt,width=380,height=120,border_color="white",border_width=2)
        sikayet.place(x=200,y=200)

        yorumunuz=customtkinter.CTkTextbox(master=frame_sag_alt,width=380,height=120,border_color="white",border_width=2)
        yorumunuz.place(x=200,y=360)

        



        Button1=customtkinter.CTkButton(master=frame_sag_alt,text="Şikayet ekle",hover_color="#1c1c1c",fg_color="#528b8b",command=insert)
        Button1.place(x=440,y=500)

        # Treeview widget'i oluştur
        global tree
        tree_columns = ("SIKAYET_ID","SIKAYET_ICERIK","OGRENCI_YORUM","OLUSTURMA_TARIHI" )
        tree = ttk.Treeview(frame_alt, columns=tree_columns, show="headings",)

        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i paketle ve yerleştir
        tree.place(x=0, y=25, width=725, height=300)
        
        
        SQL="SELECT SIKAYET_ID,SIKAYET_ICERIK,OGRENCI_YORUM,OLUSTURMA_TARIH  FROM ogrencisikayet"
        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_alt, text="Verileri Listele",width=50, command=lambda:verileri_listele(SQL))
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_alt, text="Kayıt Sil",command=kayit_sil,width=60)
        button_sil.place(x=350, y=0)        

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

giris_yap()
app.mainloop()