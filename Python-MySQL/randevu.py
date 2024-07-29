from tkinter import*
from tkinter import messagebox
import mysql.connector

def randevu_():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="users"
    )


    mycursor = mydb.cursor()


    master=Tk()
    master.title("Login")
    canvas=Canvas(master,height=700,width=1000,bg='dark slate gray')
    canvas.pack()
    master.resizable(False,False)

    def on_entry_leave(event, entry_widget, default_text):
        if entry_widget.get() == '':
            entry_widget.insert(0, default_text)
            entry_widget.config(fg='grey')  

    def on_entry_click(event, entry_widget, default_text):
        if entry_widget.get() == default_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg='black')


    def randevu_al():
        kullanici_adii = kullanici.get()
        tckimlik = TC.get()
        telefon = tel.get()
        gun = Gün.get()
        ay = Ay.get()
        yil = Yıl.get()

        dizi = [kullanici_adii, tckimlik, telefon, gun, ay, yil]

        a = 1

        for i in dizi:
            if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
                messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!') 
                a += 1 
                break
        if a == 1:
            yeni=mydb.cursor()
            insert = "INSERT INTO randevu (kullanici_adi, tckimlik, telefon, gun, ay, yil) VALUES (%s, %s, %s, %s, %s, %s)"
            degerler = (kullanici_adii, tckimlik, telefon, gun, ay, yil)
            yeni.execute(insert, degerler)
            mydb.commit()
            
            messagebox.showinfo("Bilgi", "Randevunuz başarı ile alınmıştır")
            master.destroy()
        

    frame=Frame(master,width=500,height=500,background="white")
    frame.place(x=250,y=100)
    frame.lift()

    header=Label(frame,text="Safa Hastanesi",fg='black',bg='white',font=('Microsoft YaHei UI Lıght',23,'bold'))
    header.place(x=130,y=20)

    #ad soyad alma
    kullanici=Entry(frame,width=250,fg='black',border=0,font=('Microsoft YaHei UI Lıght',11))
    kullanici.place(x=70,y=110)
    kullanici.insert(0,"Ad-soyad")
    kullanici.bind('<FocusIn>', lambda event: on_entry_click(event, kullanici, "Ad-soyad"))
    kullanici.bind('<FocusOut>', lambda event: on_entry_leave(event, kullanici, "Ad-soyad"))

    Frame(frame,width=460,height=2,bg='black').place(x=20,y=140)


    # TC kimlik
    
    TC=Entry(frame,width=250,fg='black',border=0,font=('Microsoft YaHei UI Lıght',11))
    TC.place(x=70,y=180)
    TC.insert(0,"TC kimlik")
    TC.bind('<FocusIn>', lambda event: on_entry_click(event, TC, "TC kimlik"))
    TC.bind('<FocusOut>', lambda event: on_entry_leave(event, TC, "TC kimlik"))

    Frame(frame,width=460,height=2,bg='black').place(x=20,y=210)

    #Telefon numarası 
    tel=Entry(frame,width=250,fg='black',border=0,font=('Microsoft YaHei UI Lıght',11))
    tel.place(x=70,y=250)
    tel.insert(0,"Telefon numarası")
    tel.bind('<FocusIn>', lambda event: on_entry_click(event, tel, "Telefon numarası"))
    tel.bind('<FocusOut>', lambda event: on_entry_leave(event, tel, "Telefon numarası"))

    Frame(frame,width=460,height=2,bg='black').place(x=20,y=280)



    #Tarih seçme 
    Gün= StringVar(frame) #DEFAULT bir değer atamak için kullanıyoruz
    Gün.set("Gün")
    Gün_menu =OptionMenu(frame,Gün,"Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar")
    Gün_menu.place(x=20,y=320)


    Ay= StringVar(frame) #DEFAULT bir değer atamak için kullanıyoruz
    Ay.set("Ay")
    Ay_menu =OptionMenu(frame,Ay,"Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık")
    Ay_menu.place(x=150,y=320)


    Yıl= StringVar(frame) #DEFAULT bir değer atamak için kullanıyoruz
    Yıl.set("YIL")
    Yıl_menu =OptionMenu(frame,Yıl,"2023","2024","2025")
    Yıl_menu.place(x=250,y=320)
    #button bölümü

    Button(frame,width=50,pady=7,text='Rendevu al',fg='white',bg='dark slate gray',border=0,font=('Microsoft YaHei UI Lıght',9),command=randevu_al).place(x=70,y=410)

    master.mainloop() 