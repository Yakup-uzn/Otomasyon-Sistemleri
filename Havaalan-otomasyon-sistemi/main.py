import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

customtkinter.set_appearance_mode("white")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness() #farklı ekranlara geçince otomatik ölçeklendirmeyi iptal edebilmek için

app=customtkinter.CTk()
app.geometry("1000x700")
app.resizable(False,False)
app.title("Giriş yap")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clear_widgets(frame):
	for widget in frame.winfo_children():
		widget.destroy()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

global verilerim
global kullanici
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def database():
        global mydb
        global mycursor
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="havaalani"
      )  
        mycursor = mydb.cursor()
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def login_():
    
    clear_widgets(app)
    app.tkraise()
    def Giriş_yap():
            global verilerim
            database()
            E_mail=MAIL_.get()
            sifre=Sifre.get()
           
            yonetici=check_var.get()
            if yonetici=='on':
                mycursor=mydb.cursor()
                mycursor.execute("SELECT ID,KULLANICI_ADI,KULLANICI_SOYADI,E_MAIL,SIFRE FROM yoneticigiris WHERE E_MAIL=%s and SIFRE=%s",(E_mail,sifre))
        
                verilerim=mycursor.fetchall() 

                if verilerim:
                    sefer_()
                else:

                    messagebox.showerror("Hata", "Yanlış şifre veya kullanıcı adı!")

                
            else:
               mycursor=mydb.cursor()
               mycursor.execute("SELECT ID,KULLANICI_ADI,KULLANICI_SOYADI,E_MAIL,SIFRE FROM kayit WHERE E_MAIL=%s and SIFRE=%s",(E_mail,sifre))
               verilerim=mycursor.fetchall() 
               if verilerim:
                    bilet()    
               else:

                    messagebox.showerror("Hata", "Yanlış şifre veya kullanıcı adı!")

           
            
            
                
          
          


    img = Image.open("arka.jpg")
    img_resized = img.resize((1000, 700), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(img_resized)
    arkatema = tk.Label(master=app, image=img1)
    arkatema.pack()

    frame=customtkinter.CTkFrame(master=app,width=500,height=500,fg_color="white",corner_radius=20,bg_color="#aeb3b9")
    frame.place(x=450,y=100)



    label1=customtkinter.CTkLabel(master=frame,text="Hoşgeldiniz giriş yapınız",font=('century gothic',25),text_color="black")
    label1.place(x=110,y=40)



    MAIL_=customtkinter.CTkEntry(master=frame,width=380,placeholder_text="E-mail",border_color="#673d35",font=('Microsoft YaHei UI Lıght',20))
    MAIL_.place(x=60,y=130)


    Sifre=customtkinter.CTkEntry(master=frame,width=380,placeholder_text="Şifre",border_color="#673d35",font=('Microsoft YaHei UI Lıght',20),text_color="black")
    Sifre.place(x=60,y=180)

    Button3=customtkinter.CTkButton(master=frame,text="Şifrenizi mi unuttunuz?",width=50,fg_color="white",text_color="#820000",hover_color="white",font=('Microsoft YaHei UI Lıght',15))
    Button3.place(x=285,y=220)

    check_var = customtkinter.StringVar(value="off")
    checkbox = customtkinter.CTkCheckBox(master=frame, text="Yönetici girişi",variable=check_var, onvalue="on", offvalue="off",fg_color="#820000",hover_color="#673d35")
    checkbox.place(x=60,y=260)

    Button1=customtkinter.CTkButton(master=frame,text="Giriş yapınız",width=280,corner_radius=10,hover_color="#673d35",fg_color="#820000",font=('Microsoft YaHei UI Lıght',17),command=Giriş_yap)
    Button1.place(x=110,y=300)

    label2=customtkinter.CTkLabel(master=frame,text="Kullanıcı hesabınız yok mu?",font=('Microsoft YaHei UI Lıght',15),text_color="black")
    label2.place(x=135,y=350)

   

    Button2=customtkinter.CTkButton(master=frame,text="Kayıt ol",width=50,fg_color="white",text_color="#820000",hover_color="white",font=('Microsoft YaHei UI Lıght',15),command=kayit_)
    Button2.place(x=305,y=350)

    label3=customtkinter.CTkLabel(master=frame,text="YHY iyi yolculuklar diler...",font=('Microsoft YaHei UI Lıght',15),text_color="black")
    label3.place(x=300,y=450)


    app.mainloop()
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def kayit_():

    clear_widgets(app)
    app.tkraise()

    def Kayıt_ol():
        database()


        Ad=Kullanici_adi.get()
        Soyad=Kullaci_soyad.get()
        Password=Sifre.get()
        E_mail=Mail.get()
        Tel=Telefon.get()
        Dogum=Dogum_tarihi.get()
        Cins=Cinsiyet.get()
        Sehir=Il.get()
        ilce=Ilce.get()
        posta_kod=Posta_kodu.get()

      




        select="SELECT ID FROM kayit WHERE E_MAIL=%s"
        mycursor.execute(select,(E_mail,))
        kontrol= mycursor.fetchone()

        if kontrol:
              messagebox.showerror("Uyarı", "Bu e-posta adresi zaten kullanımda.")
        else:      
        

            dizi = [Ad,Soyad,Password,E_mail,Tel,Dogum,Cins,ilce,Sehir,posta_kod]

            a = 1

            for i in dizi:
                if  i.strip() == '': 
                 messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!') 
                 a += 1 
                 break

                select="SELECT ID FROM sehir WHERE SEHIR_ISMI=%s"
                mycursor.execute(select,(Sehir,))
                Sehir_kontrol= mycursor.fetchone()

                select="SELECT ID FROM ilce WHERE ILCE_ISMI=%s"
                mycursor.execute(select,(ilce,))
                Ilce_kontrol= mycursor.fetchone()
            
            
                if Sehir_kontrol is not None:
                    Sehir_id= Sehir_kontrol[0] 
                else:            
                    messagebox.showerror("Uyarı", "Bu isimde bir il bulunmamaktadır.")
                    a += 1 
                    break

                if Ilce_kontrol is not None:
                    Ilce_id= Ilce_kontrol[0] 
                else:            
                    messagebox.showerror("Uyarı", "Bu isimde bir ilçe bulunmamaktadır.")   
                    a += 1 
                    break   



            
                if a==1:  
                    insert2 = "INSERT INTO kayit (KULLANICI_ADI,KULLANICI_SOYADI,SIFRE,E_MAIL,CINSIYET,DOGUM_TARIHI,TELEFON) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    degerler2 = (Ad,Soyad,Password,E_mail,Cins,Dogum,Tel)
                    mycursor.execute(insert2, degerler2)
                    mydb.commit()
                    messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")


                    select="SELECT ID FROM kayit WHERE E_MAIL=%s"
                    mycursor.execute(select,(E_mail,))
                    id= mycursor.fetchone()[0]

                    insert1 = "INSERT INTO adres (KAYIT_ID,SEHIR_ID,ILCE_ID,POSTA_KOD,ULKE_ID) VALUES (%s, %s,%s,%s,%s)"
                    degerler1 = (id,Sehir_id,Ilce_id,posta_kod,1)
                    mycursor.execute(insert1, degerler1)
                    mydb.commit()    



    frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
    frame_sol.place(x=0,y=0)

    my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))
    image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
    image_label.place(x=30,y=20)




    label1=customtkinter.CTkLabel(master=frame_sol,text="Hoş geldiniz",font=('century gothic',23))
    label1.place(x=110,y=35)


  
    Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Giriş yap",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=login_)
    Btn_cıkıs.place(x=50,y=630)






    frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=700,fg_color="white")
    frame_sag_ust.place(x=300,y=0)

    label1=customtkinter.CTkLabel(master=frame_sag_ust,text="Hoşgeldiniz giriş yapınız",font=('century gothic',23),text_color="black")
    label1.place(x=200,y=35)


    Kullanici_adi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Adınız :",font=('century gothic',16),text_color="black")
    Kullanici_adi_label.place(x=50,y=100)
    Kullanici_adi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Kullanici_adi.place(x=200,y=100)

    Kullaci_soyad_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Soyadınız :",font=('century gothic',16),text_color="black")
    Kullaci_soyad_label.place(x=50,y=150)
    Kullaci_soyad=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Kullaci_soyad.place(x=200,y=150)

    Sifre_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Şifre :",font=('century gothic',16),text_color="black")
    Sifre_label.place(x=50,y=200)
    Sifre=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Sifre.place(x=200,y=200)

    Mail_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Mail :",font=('century gothic',16),text_color="black")
    Mail_label.place(x=50,y=250)
    Mail=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Mail.place(x=200,y=250)

    Telefon_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Telefon :",font=('century gothic',16),text_color="black")
    Telefon_label.place(x=50,y=300)
    Telefon=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Telefon.place(x=200,y=300)

    Dogum_tarihi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Dogum tarihiniz :",font=('century gothic',16),text_color="black")
    Dogum_tarihi_label.place(x=50,y=350)
    Dogum_tarihi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Dogum_tarihi.place(x=200,y=350)

    Cinsiyet_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Cinsiyet :",font=('century gothic',16),text_color="black")
    Cinsiyet_label.place(x=50,y=400)
    Cinsiyet=customtkinter.CTkComboBox(master=frame_sag_ust,values=["K","E"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    Cinsiyet.place(x=200,y=400)

    Il_label=customtkinter.CTkLabel(master=frame_sag_ust,text="İl :",font=('century gothic',16),text_color="black")
    Il_label.place(x=50,y=450)
    Il=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Il.place(x=180,y=450)

    Ilce_label=customtkinter.CTkLabel(master=frame_sag_ust,text="İlçe :",font=('century gothic',16),text_color="black")
    Ilce_label.place(x=50,y=500)
    Ilce=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Ilce.place(x=180,y=500)

    Posta_kodu_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Posta kodu :",font=('century gothic',16),text_color="black")
    Posta_kodu_label.place(x=50,y=550)
    Posta_kodu=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    Posta_kodu.place(x=180,y=550)


    Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Kayıt ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=Kayıt_ol)
    Button1.place(x=380,y=650)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sefer_():
            
            clear_widgets(app)
            app.tkraise()
            global kullanici
            for row in verilerim:  
              kullanici=row[1]+ " " +row[2]

            def sefer_olustur():
                database()
                mycursor = mydb.cursor()

                kalkis_nokta=Kalkıs_noktasi.get()
                varis_nokta=Varis_noktasi.get()
                yolcu=yolcu_sayisi.get()
                bilet_fiyat=Bilet_fiyati.get()
                kalkis_zamani=Tarih.get()
                kuyruk_numarasi=kuyruk_no.get()
                
                
                

                select="SELECT ID FROM sehir WHERE SEHIR_ISMI=%s"
                mycursor.execute(select,(kalkis_nokta,))
                Kalkis = mycursor.fetchone()
                mycursor.execute(select,(varis_nokta,))
                Varis=mycursor.fetchone()
                
                a=1
                i=0
                
                dizi = [yolcu,bilet_fiyat,kalkis_zamani,kuyruk_numarasi]
                
                for i in dizi:
                    if  i.strip() == '' or kalkis_nokta == "" or varis_nokta == "":
                      messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                    
                      a += 1
                      break
 
                if Kalkis is  None:
                    messagebox.showerror("Uyarı", "Kalkış şehrini kontrol ediniz")
                if Varis is  None:
                    messagebox.showerror("Uyarı", "Varış şehrini kontrol ediniz")

                

                
             
                if a == 1 :
                    insert = "INSERT INTO seferler (KALKIS_SEHIR_ID,VARIS_SEHIR_ID,KUYRUK_NO,KALKIS_ZAMANI,BILET_TUTARI,YOLCU_SAYISI) VALUES (%s, %s, %s, %s, %s, %s)"
                    degerler = (Kalkis[0],Varis[0],kuyruk_numarasi,kalkis_zamani,bilet_fiyat,yolcu)
                    mycursor.execute(insert, degerler)
                    messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                    mydb.commit()
                    mydb.close()

            def verileri_listele():
                database()
                mycursor = mydb.cursor()

                mycursor.execute("SELECT ID,KALKIS_SEHIR_ID, VARIS_SEHIR_ID, KUYRUK_NO, KALKIS_ZAMANI, BILET_TUTARI, YOLCU_SAYISI FROM seferler")
                kayıtlar = mycursor.fetchall()

              
                for row in tree.get_children():
                    tree.delete(row)

               
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
                    database()

               
                    selected_id = tree.item(selected_item, 'values')[0]

                  
                    mycursor.execute("DELETE FROM seferler WHERE ID = %s", (selected_id,))

                    mydb.commit()
                    mydb.close()

                  
                    verileri_listele()





            frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
            frame_sol.place(x=0,y=0)

            my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

            image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
            image_label.place(x=30,y=20)
            
            label_text = tk.StringVar()
            label_text.set(kullanici)    
            label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',23))
            label1.place(x=110,y=35)

            Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Sefer ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=sefer_)
            Btn_sefer.place(x=50,y=200)

            Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Uçak ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=ucak)
            Btn_ucak.place(x=50,y=260)

            Btn_economyclass=customtkinter.CTkButton(master=frame_sol,text="economyclass ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=economyclass)
            Btn_economyclass.place(x=50,y=320)

            Btn_calisan=customtkinter.CTkButton(master=frame_sol,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=calisan)
            Btn_calisan.place(x=50,y=380)

            Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
            Btn_cıkıs.place(x=50,y=630)





            frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
            frame_sag_ust.place(x=300,y=0)

            label1=customtkinter.CTkLabel(master=frame_sag_ust,text="SEFER OLUŞTUR",font=('century gothic',25),text_color="black")
            label1.place(x=300,y=5)


            Kalkıs_noktasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kalkış noktası :",font=('century gothic',16),text_color="black")
            Kalkıs_noktasi_label.place(x=50,y=50)
            Kalkıs_noktasi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            Kalkıs_noktasi.place(x=180,y=50)

            Varis_noktasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Varış noktası :",font=('century gothic',16),text_color="black")
            Varis_noktasi_label.place(x=50,y=100)
            Varis_noktasi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            Varis_noktasi.place(x=180,y=100)

            yolcu_sayisi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Yolcu Sayısı :",font=('century gothic',16),text_color="black")
            yolcu_sayisi_label.place(x=50,y=150)
            yolcu_sayisi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            yolcu_sayisi.place(x=180,y=150)

            Bilet_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Bilet fiyatı :",font=('century gothic',16),text_color="black")
            Bilet_label.place(x=50,y=200)
            Bilet_fiyati=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            Bilet_fiyati.place(x=180,y=200)

            Tarih_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kalkış zamanı:",font=('century gothic',16),text_color="black")
            Tarih_label.place(x=50,y=250)
            Tarih=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            Tarih.place(x=180,y=250)

            kuyruk_no_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kuyruk no:",font=('century gothic',16),text_color="black")
            kuyruk_no_label.place(x=50,y=300)
            kuyruk_no=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
            kuyruk_no.place(x=180,y=300)

            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Sefer ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=sefer_olustur)
            Button1.place(x=360,y=350)

            frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=300,fg_color="#e6e8e7",bg_color="#e6e8e7")
            frame_sag_alt.place(x=300,y=400)

            # ... Diğer arayüz elemanları ...

            # Treeview widget'i oluştur
            tree_columns = ("ID","KALKIS_SEHIR_ID", "VARIS_SEHIR_ID", "KUYRUK_NO", "KALKIS_ZAMANI", "BILET_TUTARI", "YOLCU_SAYISI")
            tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

            # Treeview kolon başlıklarını ayarla
            for col in tree_columns:
                tree.heading(col, text=col)
                tree.column(col, width=40)

            # Treeview'i economyclassle ve yerleştir
            tree.place(x=0, y=25, width=700, height=300)

            # "Verileri Listele" butonu
            button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
            button_listele.place(x=0, y=0)

            button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
            button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def odeme():
        clear_widgets(app)
        app.tkraise()
        global kullanici
        for row in verilerim:
            kullanici_idim = row[0]  
            kullanici=row[1]+ " " +row[2]
            

        
        def yonetici_kayit():
            database()
            BANKA=banka.get()
            KART_ISIM =isim.get()
            KART_NO =kart_no.get()
            AY= ay.get()
            YIL=yıl.get()
            CVV=cvv.get()

            a=1
            

            dizi = [KART_NO,KART_ISIM,BANKA,AY,YIL,CVV]
            
            for i in dizi:
                if  i.strip()=='': 
                 messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                
                 a += 1
                 break
            


                          

            

            if a == 1 :
                
                insert = "INSERT INTO odeme (KULLANICI_ID,KART_ISIM,KART_NO,KART_SON_AY,KART_SON_YIL,KART_CVV,BANKA) VALUES (%s,%s, %s, %s, %s,%s,%s)"
                degerler = (kullanici_idim,KART_ISIM,KART_NO,AY,YIL,CVV,BANKA)
                mycursor.execute(insert, degerler)
                messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
                mydb.commit()
                mydb.close()

        def verileri_listele():
            database()
            for row in verilerim:
                kullanici_idim = row[0]      

            # Veritabanındaki kayıtları seç
            mycursor.execute("SELECT ID,KULLANICI_ID,BANKA,KART_ISIM FROM odeme WHERE KULLANICI_ID=%s", (kullanici_idim, ))
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
                    database="havaalani"
                )
                mycursor = mydb.cursor()

                selected_id = tree.item(selected_item, 'values')[0]


                mycursor.execute("DELETE FROM odeme WHERE ID = %s", (selected_id,))

                mydb.commit()
                mydb.close()


                verileri_listele()


        frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
        frame_sol.place(x=0,y=0)

        my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

        image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
        image_label.place(x=30,y=20)
        
        label_text = tk.StringVar()
        label_text.set(kullanici)    

        label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
        label1.place(x=110,y=35)

        Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Bilet al",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=bilet)
        Btn_sefer.place(x=50,y=200)

        Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Ödeme bilgileri",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17))
        Btn_ucak.place(x=50,y=260)

        kargo1=customtkinter.CTkButton(master=frame_sol,text="Kargo ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=kargo)
        kargo1.place(x=50,y=320)


        Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17))
        Btn_cıkıs.place(x=50,y=630)

        #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
        #Bt1.place(x=70,y=10)



        frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
        frame_sag_ust.place(x=300,y=0)

        label1=customtkinter.CTkLabel(master=frame_sag_ust,text="KART BİLGİLERİNİZİ GİRİNİZ",font=('century gothic',25),text_color="black")
        label1.place(x=200,y=5)


        banka_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Banka :",font=('century gothic',16),text_color="black")
        banka_label.place(x=50,y=50)
        banka=customtkinter.CTkComboBox(master=frame_sag_ust,values=["Ziraat","Garanti","Kuveyt","Akbank","İş bankası","Yapıkredi","Denizbank","Vakıf bank","Finansbank"],width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20))
        banka.place(x=180,y=50)

        isim_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kart üzerindeki isim :",font=('century gothic',16),text_color="black")
        isim_label.place(x=50,y=100)
        isim=customtkinter.CTkEntry(master=frame_sag_ust,width=340,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
        isim.place(x=220,y=100)

        kart_no_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kart no :",font=('century gothic',16),text_color="black")
        kart_no_label.place(x=50,y=150)
        kart_no=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
        kart_no.place(x=180,y=150)

        tarih_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Son kullanım tarihi :",font=('century gothic',16),text_color="black")
        tarih_label.place(x=50,y=200)
        ay=customtkinter.CTkComboBox(master=frame_sag_ust,values=["01","02","03","04","05","06","07","08","09","10","11","12"],width=100,border_color="white",font=('Microsoft YaHei UI Lıght',20))
        ay.place(x=300,y=200)
        yıl=customtkinter.CTkComboBox(master=frame_sag_ust,values=["23","24","25","26","27","28","29","30","31","32"],width=100,border_color="white",font=('Microsoft YaHei UI Lıght',20))
        yıl.place(x=455,y=200)


        cvv_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Cvv :",font=('century gothic',16),text_color="black")
        cvv_label.place(x=50,y=250)
        cvv=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
        cvv.place(x=180,y=250)



        Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Kaydet",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=yonetici_kayit)
        Button1.place(x=360,y=350)


        frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
        frame_sag_alt.place(x=300,y=400)

        # ... Diğer arayüz elemanları ...

        # Treeview widget'i oluştur
        tree_columns = ("ID","KULLANICI_ID","BANKA","KART_ISIM")
        tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")
        # Treeview kolon başlıklarını ayarla
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=40)

        # Treeview'i economyclassle ve yerleştir
        tree.place(x=0, y=25, width=700, height=300)

        # "Verileri Listele" butonu
        button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
        button_listele.place(x=0, y=0)

        button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
        button_sil.place(x=350, y=0)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calisan():
 
    def calisan_ekle():
        database()
        calisanadi=calisan_ad.get()
        calisansoyadi=calisan_soyad.get()
        tel=telefon.get()
        cins=cinsiyet.get()
        poz=pozisyon.get()
        ucret=maas.get()
        

        a=1
        

        dizi = [calisanadi,calisansoyadi,tel,cins,ucret,poz]
        
        for i in dizi:
            if  i.strip() == '':
             messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın ve havaalanı seçin!')  
            
             a += 1
             break

        if a == 1 :
            select="SELECT ID FROM personelpozisyonu WHERE POZISYON_ADI=%s"
            mycursor.execute(select,(poz,))
            poz_id= mycursor.fetchone()
        
            insert1 = "INSERT INTO calisanlar (CALISAN_AD, CALISAN_SOYAD, TELEFON, CINSIYET, MAAS, HAVAALANI_ID,POZISYON_ID) VALUES (%s, %s, %s, %s, %s, %s,%s)"
            degerler1 = (calisanadi,calisansoyadi,tel,cins,ucret,havaalani_id,poz_id[0])
            mycursor.execute(insert1, degerler1)

            messagebox.showinfo("Bilgi", "economyclass başarıyla eklendi")
            mydb.commit()
            mydb.close()


    def verileri_listele():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="havaalani"
        )
        mycursor = mydb.cursor()


    
        join1="SELECT ID,HAVAALANI_AD,IL,ILCE FROM havaalanlari"
        mycursor.execute(join1)
        kayıtlar = mycursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)


        for kayıtlar in kayıtlar:
            tree.insert("", "end", values=kayıtlar)

        mydb.close()



    def havaalanlari():
        selected_item = tree.selection()

        if not selected_item:
            messagebox.showwarning("Uyarı", "Lütfen personelin ekleneceği havaalanını  seçin.")
            return

        confirm = messagebox.askyesno("Onay", "Seçili havaalanına eklemek istiyor musunuz")

        if confirm:
            database()

            global havaalani_id
            havaalani_id = tree.item(selected_item, 'values')[0]
            
           

            mydb.commit()
            mydb.close()


            





    frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
    frame_sol.place(x=0,y=0)

    my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

    image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
    image_label.place(x=30,y=20)
    label_text = tk.StringVar()
    label_text.set(kullanici)    
    label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
    label1.place(x=110,y=35)

    Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Sefer ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=sefer_)
    Btn_sefer.place(x=50,y=200)

    Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Uçak ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=ucak)
    Btn_ucak.place(x=50,y=260)

    Btn_economyclass=customtkinter.CTkButton(master=frame_sol,text="economyclass ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=economyclass)
    Btn_economyclass.place(x=50,y=320)

    Btn_calisan=customtkinter.CTkButton(master=frame_sol,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=calisan)
    Btn_calisan.place(x=50,y=380)

    Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
    Btn_cıkıs.place(x=50,y=630)


    frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
    frame_sag_ust.place(x=300,y=0)

    label1=customtkinter.CTkLabel(master=frame_sag_ust,text="CALISAN EKLE",font=('century gothic',25),text_color="black")
    label1.place(x=300,y=5)


    calisan_ad_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Çalışan ad :",font=('century gothic',16),text_color="black")
    calisan_ad_label.place(x=50,y=50)
    calisan_ad=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    calisan_ad.place(x=180,y=50)

    calisan_soyad_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Çalışan soyad :",font=('century gothic',16),text_color="black")
    calisan_soyad_label.place(x=50,y=100)
    calisan_soyad=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    calisan_soyad.place(x=180,y=100)

    telefon_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Telefon :",font=('century gothic',16),text_color="black")
    telefon_label.place(x=50,y=150)
    telefon=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    telefon.place(x=180,y=150)

    cinsiyet_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Cinsiyet :",font=('century gothic',16),text_color="black")
    cinsiyet_label.place(x=50,y=200)
    cinsiyet=customtkinter.CTkComboBox(master=frame_sag_ust,values=["K","E"],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    cinsiyet.place(x=180,y=200)

    pozisyon_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Pozisyon :",font=('century gothic',16),text_color="black")
    pozisyon_label.place(x=50,y=250)
    pozisyon=customtkinter.CTkComboBox(master=frame_sag_ust,values=['Pilot','Yardımcı Pilot','Kabin Memuru (Hostes)','Havaalanı Yöneticisi','Gümrük Memuru','Bagaj Memuru','Güvenlik Yöneticisi''Hava Trafik Kontrol Kulesi Operatörü','Yer Hizmetleri Memuru','Hava Trafik Kontrolörü','Güvenlik Görevlisi','Check-in Memuru','Yolcu Hizmetleri Görevlisi','Havaalanı Mühendisi','Havaalanı İletişim Memuru'],width=150,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    pozisyon.place(x=180,y=250)

    maas_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Maaş :",font=('century gothic',16),text_color="black")
    maas_label.place(x=50,y=300)
    maas=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    maas.place(x=180,y=300)


    Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17), command=calisan_ekle)
    Button1.place(x=360,y=350)

    frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=300,fg_color="#e6e8e7",bg_color="#e6e8e7")
    frame_sag_alt.place(x=300,y=400)

    # ... Diğer arayüz elemanları ...

    # Treeview widget'i oluştur
    tree_columns = ("ID", "HAVAALANI AD", "İL", "İLÇE")
    tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

    # Treeview kolon başlıklarını ayarla
    for col in tree_columns:
        tree.heading(col, text=col)
        tree.column(col, width=60)

    # Treeview'i economyclassle ve yerleştir
    tree.place(x=0, y=25, width=700, height=300)

    # "Verileri Listele" butonu
    button_listele = tk.Button(frame_sag_alt, text="Havaalanlarını Listele",width=50, command=verileri_listele)
    button_listele.place(x=0, y=0)

    button_sec = tk.Button(frame_sag_alt, text="Havaalanı seç",command=havaalanlari,width=50)
    button_sec.place(x=350, y=0)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def economyclass():
    def economyclass_ekle():
        database()

        packet=economyclass_adi.get()
        koltuk=businessclass.get()
        bagaj=firstclass.get()
        d_ozellik=diger.get()
        ikram=premium.get()
        
        
    
        
        a=1
        

        dizi = [packet,koltuk,bagaj,ikram]
        
        for i in dizi:
            if  i.strip() == '': 
             messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
            
             a += 1
             break


        if a == 1 :
            insert1 = "INSERT INTO economyclassdetay (economyclass_ADI, premium, firstclass, KOLTUK_SECIMI,DIGER_AVANTAJLAR) VALUES (%s, %s, %s, %s, %s)"
            degerler1 = (packet,ikram,bagaj,koltuk,d_ozellik)
            mycursor.execute(insert1, degerler1)

            messagebox.showinfo("Bilgi", "economyclass başarıyla eklendi")
            mydb.commit()
            mydb.close()


    def verileri_listele():
        database()

  
        join = "SELECT * FROM economyclassdetay"
        mycursor.execute(join)
        kayıtlar = mycursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)

  
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
            database()
            mycursor = mydb.cursor()


            
            selected_id = tree.item(selected_item, 'values')[0]


            mycursor.execute("DELETE FROM economyclassdetay WHERE ID = %s", (selected_id,))
        

            mydb.commit()
            mydb.close()
            verileri_listele()





    frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
    frame_sol.place(x=0,y=0)

    my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

    image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
    image_label.place(x=30,y=20)

    label_text = tk.StringVar()
    label_text.set(kullanici)    

    label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
    label1.place(x=110,y=35)

    Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Sefer ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=sefer_)
    Btn_sefer.place(x=50,y=200)

    Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Uçak ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=ucak)
    Btn_ucak.place(x=50,y=260)

    Btn_economyclass=customtkinter.CTkButton(master=frame_sol,text="economyclass ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=economyclass)
    Btn_economyclass.place(x=50,y=320)

    Btn_calisan=customtkinter.CTkButton(master=frame_sol,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=calisan)
    Btn_calisan.place(x=50,y=380)

    Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
    Btn_cıkıs.place(x=50,y=630)

    #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
    #Bt1.place(x=70,y=10)



    frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
    frame_sag_ust.place(x=300,y=0)

    label1=customtkinter.CTkLabel(master=frame_sag_ust,text="economyclass EKLE",font=('century gothic',25),text_color="black")
    label1.place(x=300,y=5)


    economyclass_adi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="economyclass Adı :",font=('century gothic',16),text_color="black")
    economyclass_adi_label.place(x=50,y=50)
    economyclass_adi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    economyclass_adi.place(x=180,y=50)

    firstclass_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Bagaj Hakkı :",font=('century gothic',16),text_color="black")
    firstclass_label.place(x=50,y=100)
    firstclass=customtkinter.CTkComboBox(master=frame_sag_ust,values=["Geniş Bagaj Hakkı","Sınırlı Bagaj Hakkı"],width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    firstclass.place(x=180,y=100)

    businessclass_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Koltuk Seçimi :",font=('century gothic',16),text_color="black")
    businessclass_label.place(x=50,y=150)
    businessclass=customtkinter.CTkComboBox(master=frame_sag_ust,values=["Standart koltuk","Daha geniş koltuklar","Recliner Koltuk","Tam Düzleşebilen Koltuk"],width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    businessclass.place(x=180,y=150)


    premium_label=customtkinter.CTkLabel(master=frame_sag_ust,text="İkram Servis :",font=('century gothic',16),text_color="black")
    premium_label.place(x=50,y=250)
    premium=customtkinter.CTkComboBox(master=frame_sag_ust,values=["Özel Menü Seçenekleri","Özel Yemek Servisi","Gelişmiş Yemek Seçenekleri","Standart İkramlar"],width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20))
    premium.place(x=180,y=250)

    diger_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Diger özellikler :",font=('century gothic',16),text_color="black")
    diger_label.place(x=50,y=200)
    diger=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    diger.place(x=180,y=200)

    Button1=customtkinter.CTkButton(master=frame_sag_ust,text="economyclass ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17), command=economyclass_ekle)
    Button1.place(x=360,y=350)

    frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=300,fg_color="#e6e8e7",bg_color="#e6e8e7")
    frame_sag_alt.place(x=300,y=400)

    # ... Diğer arayüz elemanları ...

    # Treeview widget'i oluştur
    tree_columns = ("ID", "economyclass ADI", "KOLTUK TÜRÜ", "IKRAM SERVIS", "BAGAJ HAKKI", "DİGER AVANTAJLAR")
    tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

    # Treeview kolon başlıklarını ayarla
    for col in tree_columns:
        tree.heading(col, text=col)
        tree.column(col, width=40)

    # Treeview'i economyclassle ve yerleştir
    tree.place(x=0, y=25, width=700, height=300)

    # "Verileri Listele" butonu
    button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
    button_listele.place(x=0, y=0)

    button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
    button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ucak():
    def ucak_ekle():
        database()

        marka=marka_ID.get()
        hız=ucus.get()
        ilk_ucus_t=ilk_ucus.get()
        son_ucus_t=son_ucus.get()
        maksimum_menzil=maks.get()
        kuyruk_no=kuyruk.get()
    
        
        a=1
        

        dizi = [marka,kuyruk_no,maksimum_menzil,hız,ilk_ucus_t,son_ucus_t]
        
        for i in dizi:
            if  i.strip() == '': 
             messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
            
             a += 1
             break


        if a == 1 :
            insert1 = "INSERT INTO ucaklar (MARKA_ID,KUYRUK_NUMARASI,UCUS_MENZILI,MAKS_HIZ,ILK_UCUS_TARIHI,EMEKLILIK_TARIHI) VALUES (%s, %s,%s,%s,%s,%s)"
            degerler1 = (marka,kuyruk_no,maksimum_menzil,hız,ilk_ucus_t,son_ucus_t)
            mycursor.execute(insert1, degerler1)



            messagebox.showinfo("Bilgi", "economyclass başarıyla eklendi")
            mydb.commit()
            mydb.close()

            
    def verileri_listele():
        database()


        join = "SELECT UCAK_ID, UCAK_MARKA, UCAK_MODEL,YOLCU_KAPASITESI, YAKIT_TURU FROM havaalani.ucak_bilgi"
        mycursor.execute(join)
        kayıtlar = mycursor.fetchall()


        for row in tree.get_children():
            tree.delete(row)

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
                database="havaalani"
            )
            mycursor = mydb.cursor()

            # Seçilen kaydın KALKIS_SEHIR_ID değerini al
            
            selected_id = tree.item(selected_item, 'values')[0]
            
            selected_id2 = tree.item(selected_item, 'values')[1]

            # Kaydı sil
            mycursor.execute("DELETE FROM ucaklar WHERE ID = %s", (selected_id,))
            mycursor.execute("DELETE FROM ucakmarka WHERE ID = %s", (selected_id2,))

            mydb.commit()
            mydb.close()

            # Kayıtları güncelle
            verileri_listele()





    frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
    frame_sol.place(x=0,y=0)

    my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

    image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
    image_label.place(x=30,y=20)
    label_text = tk.StringVar()
    label_text.set(kullanici)    
    label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
    label1.place(x=110,y=35)

    Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Sefer ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=sefer_)
    Btn_sefer.place(x=50,y=200)

    Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Uçak ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=ucak)
    Btn_ucak.place(x=50,y=260)

    Btn_economyclass=customtkinter.CTkButton(master=frame_sol,text="economyclass ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=economyclass)
    Btn_economyclass.place(x=50,y=320)

    Btn_calisan=customtkinter.CTkButton(master=frame_sol,text="Çalışan ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=calisan)
    Btn_calisan.place(x=50,y=380)

    Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
    Btn_cıkıs.place(x=50,y=630)

    #Bt1=customtkinter.CTkButton(master=frame_sol,width=250,height=30,text="Bora Altun",compound="left",text_color="white",bg_color="#1f2021",fg_color="#1f2021",hover_color="#1f2021")
    #Bt1.place(x=70,y=10)



    frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=400,fg_color="white")
    frame_sag_ust.place(x=300,y=0)

    label1=customtkinter.CTkLabel(master=frame_sag_ust,text="UCAK EKLE",font=('century gothic',25),text_color="black")
    label1.place(x=340,y=5)


    marka_ID_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Marka-model ID :",font=('century gothic',16),text_color="black")
    marka_ID_label.place(x=50,y=50)
    marka_ID=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    marka_ID.place(x=220,y=50)

    kuyruk_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kuyruk numarası :",font=('century gothic',16),text_color="black")
    kuyruk_label.place(x=50,y=100)
    kuyruk=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    kuyruk.place(x=220,y=100)

    ucus_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Uçuş hızı :",font=('century gothic',16),text_color="black")
    ucus_label.place(x=50,y=150)
    ucus=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    ucus.place(x=220,y=150)

    maks_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Maksımum menzil :",font=('century gothic',16),text_color="black")
    maks_label.place(x=50,y=200)
    maks=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    maks.place(x=220,y=200)

    ilk_ucus_label=customtkinter.CTkLabel(master=frame_sag_ust,text="İlk uçuş tarihi :",font=('century gothic',16),text_color="black")
    ilk_ucus_label.place(x=50,y=250)
    ilk_ucus=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    ilk_ucus.place(x=220,y=250)

    son_ucus_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Emeklilik tarihi :",font=('century gothic',16),text_color="black")
    son_ucus_label.place(x=50,y=300)
    son_ucus=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',20),fg_color="#b2b2b2")
    son_ucus.place(x=220,y=300)


    Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Uçak ekle",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17), command=ucak_ekle)
    Button1.place(x=360,y=400)

    frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=300,fg_color="#e6e8e7",bg_color="#e6e8e7")
    frame_sag_alt.place(x=300,y=400)

    # ... Diğer arayüz elemanları ...

    # Treeview widget'i oluştur
    tree_columns = ("UCAK_ID", "UCAK_MARKA", "UCAK_MODEL","YOLCU KAPASITESI", "YAKIT_TURU")
    tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

    # Treeview kolon başlıklarını ayarla
    for col in tree_columns:
        tree.heading(col, text=col)
        tree.column(col, width=60)

    # Treeview'i economyclassle ve yerleştir
    tree.place(x=0, y=25, width=700, height=300)

    # "Verileri Listele" butonu
    button_listele = tk.Button(frame_sag_alt, text="Verileri Listele",width=50, command=verileri_listele)
    button_listele.place(x=0, y=0)

    button_sil = tk.Button(frame_sag_alt, text="Kayıt Sil",command=kayit_sil,width=50)
    button_sil.place(x=350, y=0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def bilet():
            clear_widgets(app)
            app.tkraise()
            global kullanici
            for row in verilerim:  
              kullanici=row[1]+ " " +row[2]
              ID=row[0]


            def bilet_al():
                    database()



                    insert2 = "INSERT INTO biletler (YOLCU_ID,SEFER_ID,UCRET) VALUES (%s, %s, %s)"
                    degerler2 = (ID,selected_id,hes5)
                    mycursor.execute(insert2, degerler2)
                    mydb.commit()
                    messagebox.showinfo("Bilgi", "Bilet alındı")
           
 

            def verileri_listele():
                database()
                sql='''
                    SELECT s.ID, s1.SEHIR_ISMI AS KALKIS_SEHIR, s2.SEHIR_ISMI AS VARIS_SEHIR, s.KUYRUK_NO, s.KALKIS_ZAMANI, s.BILET_TUTARI, s.YOLCU_SAYISI
                    FROM seferler AS s
                    JOIN sehir s1 ON s1.ID = s.KALKIS_SEHIR_ID
                    JOIN sehir s2 ON s2.ID = s.VARIS_SEHIR_ID
                  ;


                    '''


                mycursor.execute(sql)
                kayıtlar = mycursor.fetchall()

                for row in tree.get_children():
                    tree.delete(row)

                for kayıtlar in kayıtlar:
                    tree.insert("", "end", values=kayıtlar)

                mydb.close()



            def filtre():
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="havaalani"
                )
                mycursor = mydb.cursor()
                kalkis_nokta=Kalkıs_noktasi.get()
                varis_nokta=Varis_noktasi.get()
                
                
                

                select="SELECT ID FROM sehir WHERE SEHIR_ISMI=%s"
                mycursor.execute(select,(kalkis_nokta,))
                Kalkis = mycursor.fetchone()
                mycursor.execute(select,(varis_nokta,))
                Varis=mycursor.fetchone()


                if Kalkis is  None:
                    messagebox.showerror("Uyarı", "Kalkış şehrini kontrol ediniz")
                if Varis is  None:
                    messagebox.showerror("Uyarı", "Varış şehrini kontrol ediniz")


                sql='''
                    SELECT s.ID, s1.SEHIR_ISMI AS KALKIS_SEHIR, s2.SEHIR_ISMI AS VARIS_SEHIR, s.KUYRUK_NO, s.KALKIS_ZAMANI, s.BILET_TUTARI, s.YOLCU_SAYISI
                    FROM seferler AS s
                    JOIN sehir s1 ON s1.ID = s.KALKIS_SEHIR_ID
                    JOIN sehir s2 ON s2.ID = s.VARIS_SEHIR_ID
                    WHERE s.KALKIS_SEHIR_ID = %s AND s.VARIS_SEHIR_ID = %s;


                    '''
                deger=(Kalkis[0],Varis[0])
                mycursor.execute(sql,deger)
                kayıtlar = mycursor.fetchall()

                 


                for row in tree.get_children():
                    tree.delete(row)


                for kayıtlar in kayıtlar:
                    tree.insert("", "end", values=kayıtlar)

                mydb.close()

            def sefer_sec():
                selected_item = tree.selection()

                if not selected_item:
                    messagebox.showwarning("Uyarı", "Lütfen sefer seçin.")
                    return

                confirm = messagebox.askyesno("Onay", "Bu seferi seçmek istediğinizden emin misiniz ?")

                if confirm:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="havaalani"
                    )
                    mycursor = mydb.cursor()

              
                    global selected_id
                    selected_id = tree.item(selected_item, 'values')[0]

               
                    mycursor.execute("SELECT BILET_TUTARI FROM seferler WHERE ID = %s", (selected_id,))
                    global tutar
                    tutar=mycursor.fetchone()


                    mydb.commit()
                    mydb.close()

                    verileri_listele()



            

            frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
            frame_sol.place(x=0,y=0)

            my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

            image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
            image_label.place(x=30,y=20)
            
            label_text = tk.StringVar()
            label_text.set(kullanici)    
            label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
            label1.place(x=110,y=35)

            Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Bilet al",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=bilet)
            Btn_sefer.place(x=50,y=200)

            Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Ödeme bilgileri",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=odeme)
            Btn_ucak.place(x=50,y=260)

            kargo1=customtkinter.CTkButton(master=frame_sol,text="Kargo ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=kargo)
            kargo1.place(x=50,y=320)

            Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
            Btn_cıkıs.place(x=50,y=630)

            def hesapla():

                hes1=firstclass_label.get()
                hes2=businessclass_label.get()
                hes3=premium_label.get()
                hes4=economyclass_label.get()
                global hes5
                hes5=hes1+hes2+hes3+hes4+tutar[0]
                label_text = customtkinter.IntVar()
                label_text.set(hes5)    
                label1=customtkinter.CTkLabel(master=frame_sag_ust,textvariable=label_text,font=('century gothic',17),fg_color="#808080",width=300,corner_radius=10,bg_color="white")
                label1.place(x=400,y=350)




            frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=500,fg_color="white")
            frame_sag_ust.place(x=300,y=200)


            Kalkıs_noktasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kalkış nokta :",font=('century gothic',16),text_color="black")
            Kalkıs_noktasi_label.place(x=5,y=50)
            Kalkıs_noktasi=customtkinter.CTkEntry(master=frame_sag_ust,width=210,border_color="white",font=('Microsoft YaHei UI Lıght',16),fg_color="#b2b2b2")
            Kalkıs_noktasi.place(x=105,y=50)

            Varis_noktasi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Varış nokta :",font=('century gothic',16),text_color="black")
            Varis_noktasi_label.place(x=330,y=50)
            Varis_noktasi=customtkinter.CTkEntry(master=frame_sag_ust,width=210,border_color="white",font=('Microsoft YaHei UI Lıght',16),fg_color="#b2b2b2")
            Varis_noktasi.place(x=430,y=50)

            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="S",width=40,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',16),command=filtre)
            Button1.place(x=650,y=50)

            label1=customtkinter.CTkLabel(master=frame_sag_ust,text="Ek Özellikler",font=('century gothic',25),text_color="black")
            label1.place(x=300,y=100)
            

            firstclass_label=customtkinter.IntVar(value=0)
            firstclass=customtkinter.CTkCheckBox(master=frame_sag_ust,text="First class (+2000)",variable=firstclass_label, onvalue=2000, offvalue=0,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            firstclass.place(x=80,y=150)

            businessclass_label=customtkinter.IntVar(value=0)
            businessclass=customtkinter.CTkCheckBox(master=frame_sag_ust,text="Business class (+1500)",variable=businessclass_label, onvalue=1500, offvalue=0,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            businessclass.place(x=80,y=200)

            premium_label=customtkinter.IntVar(value=0)
            premium=customtkinter.CTkCheckBox(master=frame_sag_ust,text="Premium economy class (+1000)",variable=premium_label, onvalue=1000, offvalue=0,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            premium.place(x=80,y=250)

            economyclass_label=customtkinter.IntVar(value=0)
            economyclass=customtkinter.CTkCheckBox(master=frame_sag_ust,text="Economy class (+500)",variable=economyclass_label, onvalue=500, offvalue=0,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17))
            economyclass.place(x=80,y=300)

            label1=customtkinter.CTkLabel(master=frame_sag_ust,text=" 0 TL ",font=('century gothic',17),fg_color="#808080",width=300,corner_radius=10,bg_color="white")
            label1.place(x=400,y=350)

            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Hesapla",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=hesapla)
            Button1.place(x=100,y=400)

            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Ödeme yap",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=bilet_al)
            Button1.place(x=400,y=400)


            frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=200,fg_color="#e6e8e7",bg_color="#e6e8e7")
            frame_sag_alt.place(x=300,y=0)

            # ... sefer seç ...

            # Treeview widget'i oluştur
            tree_columns = ("ID","KALKIS_SEHIR_ID", "VARIS_SEHIR_ID", "KUYRUK_NO", "KALKIS_ZAMANI", "BILET_TUTARI", "YOLCU_SAYISI")
            tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

            # Treeview kolon başlıklarını ayarla
            for col in tree_columns:
                tree.heading(col, text=col)
                tree.column(col, width=40)

            # Treeview'i economyclassle ve yerleştir
            tree.place(x=0, y=25, width=700, height=300)

            # "Verileri Listele" butonu

            button_sil = tk.Button(frame_sag_alt, text="Sefer seç",command=sefer_sec,width=100)
            button_sil.place(x=0, y=0)

            verileri_listele()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def kargo():
            clear_widgets(app)
            app.tkraise()
            global kullanici
            for row in verilerim:  
              kullanici=row[1]+ " " +row[2]
              ID=row[0]

            def kargo_ekle():
                    database()
                    gonderen_ad=gonderici.get()
                    alici_ad=alici.get()
                    kargo_ad=kargo_adi.get()
                    kargo_kg=kargo_agirlik.get()
                    icerik=kargo_icerik.get("1.0",'end-1c')

                
                    
                    a=1
                    

                    dizi = [gonderen_ad,alici_ad,kargo_ad,kargo_kg,icerik]
                    
                    for i in dizi:
                        if  i.strip() == '': 
                          messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!')  
                          a += 1
                          break
  
                    if a == 1 :
                        insert1 = "INSERT INTO kargo (GONDEREN_ID,GONDERICI_ISMI,ALICI_ISMI,KARGO_ADI,KARGO_AGIRLIK,KARGO_ICERIK) VALUES (%s, %s,%s,%s,%s,%s)"
                        degerler1 = (ID,gonderen_ad,alici_ad,kargo_ad,kargo_kg,icerik)
                        mycursor.execute(insert1, degerler1)



                        messagebox.showinfo("Bilgi", "Kargo başarıyla eklendi")
                        mydb.commit()
                        mydb.close()
            

            def verileri_listele():
                database()


                mycursor.execute("SELECT GONDERICI_ISMI,ALICI_ISMI,KARGO_ADI,KARGO_AGIRLIK,KARGO_ICERIK FROM kargo WHERE GONDEREN_ID=%s",(ID,))
                kayıtlar = mycursor.fetchall()

 
                for row in tree.get_children():
                    tree.delete(row)

                for kayıtlar in kayıtlar:
                    tree.insert("", "end", values=kayıtlar)

                mydb.close()






            

            frame_sol=customtkinter.CTkFrame(master=app,width=300,height=700,fg_color="#6b6b6b",bg_color="#6b6b6b")
            frame_sol.place(x=0,y=0)

            my_image = customtkinter.CTkImage(dark_image=Image.open("profil.png"), size=(60, 60))

            image_label = customtkinter.CTkLabel(app, image=my_image,text="",bg_color="#6b6b6b")
            image_label.place(x=30,y=20)
            
            label_text = tk.StringVar()
            label_text.set(kullanici)    
            label1=customtkinter.CTkLabel(master=frame_sol,textvariable=label_text,font=('century gothic',17))
            label1.place(x=110,y=35)

            Btn_sefer=customtkinter.CTkButton(master=frame_sol,text="Bilet al",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=bilet)
            Btn_sefer.place(x=50,y=200)

            Btn_ucak=customtkinter.CTkButton(master=frame_sol,text="Ödeme bilgileri",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=odeme)
            Btn_ucak.place(x=50,y=260)

            kargo1=customtkinter.CTkButton(master=frame_sol,text="Kargo ekle",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=kargo)
            kargo1.place(x=50,y=320)

            Btn_cıkıs=customtkinter.CTkButton(master=frame_sol,text="Çıkış yap",width=200,corner_radius=10,hover_color="#b2b2b2",fg_color="#808080",font=('Microsoft YaHei UI Lıght',17),command=login_)
            Btn_cıkıs.place(x=50,y=630)

        

            frame_sag_ust=customtkinter.CTkFrame(master=app,width=700,height=500,fg_color="white")
            frame_sag_ust.place(x=300,y=0)

            label1=customtkinter.CTkLabel(master=frame_sag_ust,text="KARGO YOLLA",font=('century gothic',25),text_color="black")
            label1.place(x=330,y=30)

            gonderici_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Gönderici adı :",font=('century gothic',16),text_color="black")
            gonderici_label.place(x=50,y=100)
            gonderici=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',16),fg_color="#b2b2b2")
            gonderici.place(x=220,y=100)

            alici_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Alıcı adı :",font=('century gothic',16),text_color="black")
            alici_label.place(x=50,y=150)
            alici=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',16),fg_color="#b2b2b2")
            alici.place(x=220,y=150)

            kargo_adi_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kargo adı :",font=('century gothic',16),text_color="black")
            kargo_adi_label.place(x=50,y=200)
            kargo_adi=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',16),fg_color="#b2b2b2")
            kargo_adi.place(x=220,y=200)

            kargo_agirlik_label=customtkinter.CTkLabel(master=frame_sag_ust,text="Kargo ağırlık :",font=('century gothic',16),text_color="black")
            kargo_agirlik_label.place(x=50,y=250)
            kargo_agirlik=customtkinter.CTkEntry(master=frame_sag_ust,width=380,border_color="white",font=('Microsoft YaHei UI Lıght',16),fg_color="#b2b2b2")
            kargo_agirlik.place(x=220,y=250)  

            kargo_icerik_label = customtkinter.CTkLabel(frame_sag_ust, text="Kargo içeriği :",font=('century gothic',17))
            kargo_icerik_label.place(x=50, y=300)
            kargo_icerik=customtkinter.CTkTextbox(frame_sag_ust,width=380,height=120,border_color="white",border_width=2,fg_color="#b2b2b2")
            kargo_icerik.place(x=220,y=300)
          
            Button1=customtkinter.CTkButton(master=frame_sag_ust,text="Tamamla",width=200,corner_radius=10,hover_color="#808080",fg_color="#6b6b6b",font=('Microsoft YaHei UI Lıght',17),command=kargo_ekle)
            Button1.place(x=400,y=450)

            frame_sag_alt=customtkinter.CTkFrame(master=app,width=700,height=200,fg_color="#e6e8e7",bg_color="#e6e8e7")
            frame_sag_alt.place(x=300,y=500)



            # Treeview widget'i oluştur
            tree_columns = ("GONDERICI_ISMI","ALICI_ISMI","KARGO_ADI","KARGO_AGIRLIK","KARGO_ICERIK")
            tree = ttk.Treeview(frame_sag_alt, columns=tree_columns, show="headings")

            # Treeview kolon başlıklarını ayarla
            for col in tree_columns:
                tree.heading(col, text=col)
                tree.column(col, width=40)

            # Treeview'i economyclassle ve yerleştir
            tree.place(x=0, y=25, width=700, height=300)

            # "Verileri Listele" butonu

            button = tk.Button(frame_sag_alt, text="KARGOLARIMI GÖSTER",width=100,command=verileri_listele)
            button.place(x=0, y=0)

            verileri_listele()                         

login_()
app.mainloop()    



