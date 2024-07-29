from tkinter import*
from tkinter import messagebox
import mysql.connector
import login
import randevu
from PIL import Image, ImageTk

def kayıt_():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="users"
  )

  mycursor = mydb.cursor()



  def Giriş_ekranı():
    master.destroy()
    login.login_() 

  def on_entry_leave(event, entry_widget, default_text):
        if entry_widget.get() == '':
            entry_widget.insert(0, default_text)
            entry_widget.config(fg='grey')  

  def on_entry_click(event, entry_widget, default_text):
        if entry_widget.get() == default_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg='black')

  
    
              

  master=Tk()
  master.title("Login")
  canvas=Canvas(master,height=700,width=1000,bg='white')
  canvas.pack()
  master.resizable(False,False)





  def kayıt_yap():
      
        
    Ad_soyad=kullanici.get()
    kullanici_AD=kullanici_adi.get()
    sifre_=Parola.get()
    posta_=E_posta.get()

    dizi = [Ad_soyad, kullanici_AD, sifre_, posta_]

    a = 1

    for i in dizi:
      if  i.strip() == '': #strip() fonksiyonu: bir kelime alıyor sağındaki ve solundaki boşlukları siliyor yaptığı bu 
        messagebox.showwarning('Uyarı','Lütfen Boş Alan Bırakmayın!') 
        a += 1 
        break
    if a == 1:
      yeni=mydb.cursor()
      insert1 = "INSERT INTO kullanici (kullanici_adi, kullanici_sifre) VALUES (%s, %s)"
      degerler1 = (kullanici_AD,sifre_)
      yeni.execute(insert1, degerler1)
      

      yeni2=mydb.cursor()
      insert2 = "INSERT INTO kayit (kullanici_adi_soyadi, kullanici_AD, kullanici_sifre, kullanici_posta) VALUES (%s, %s, %s, %s)"
      degerler2 = (Ad_soyad, kullanici_AD, sifre_, posta_)
      yeni2.execute(insert2, degerler2)
      mydb.commit()
      messagebox.showinfo("Bilgi", "Başarıyla kayıt olundu")
      
      Giriş_ekranı()  

  


  # Resmi yükle
  resim=Image.open("jpg/kayit.jpg")
  # Resmi yeniden boyutlandır
  org_genislik, org_yukseklik = resim.size
  hedef_genislik = 400
  hedef_yukseklik = int((org_yukseklik / org_genislik) * hedef_genislik)

  resim.thumbnail((hedef_genislik, hedef_yukseklik), Image.LANCZOS)  # Resmi yeniden boyutlandır

  # Resmi ImageTk.PhotoImage ile işle
  img = ImageTk.PhotoImage(resim)

  # Label içerisinde resmi göster
  label = Label(master, image=img, bg='white')
  label.place(x=62,y=170)



  frame=Frame(master,width=500,height=500,background="white")
  frame.place(x=500,y=100)
  frame.lift() #frame fonksiyonunu öne çıkartır yani üst katman yapar

  #header bölümü
  header = Label(frame,text="KAYIT OLUNUZ",fg='dark slate gray',bg='white',font=('Microsoft YaHei UI Lıght',23,'bold'))
  header.place(x=110,y=0)


  #ad soyad alma
  
  
  kullanici=Entry(frame,width=250,fg='black',border=0,font=('Microsoft YaHei UI Lıght',11))
  kullanici.place(x=70,y=110)
  kullanici.insert(0,"Ad-soyad")
  kullanici.bind('<FocusIn>', lambda event: on_entry_click(event, kullanici, "Ad-soyad"))
  kullanici.bind('<FocusOut>', lambda event: on_entry_leave(event, kullanici, "Ad-soyad"))
  
  Frame(frame,width=460,height=2,bg='black').place(x=20,y=140)


  # kullanıcı adını alma 
  
  kullanici_adi=Entry(frame,width=250,fg='black',border=0,font=('Microsoft YaHei UI Lıght',11))
  kullanici_adi.place(x=70,y=180)
  kullanici_adi.insert(0,"Kullanıcı adı ")
  kullanici_adi.bind('<FocusIn>', lambda event: on_entry_click(event, kullanici_adi, "Kullanıcı adı "))
  kullanici_adi.bind('<FocusOut>', lambda event: on_entry_leave(event, kullanici_adi, "Kullanıcı adı "))
  
  Frame(frame,width=460,height=2,bg='black').place(x=20,y=210)

  #E-posta alma  
  E_posta=Entry(frame,width=250,fg='black',border=0,font=('Microsoft YaHei UI Lıght',11))
  E_posta.place(x=70,y=250)
  E_posta.insert(0,"E-posta ")
  E_posta.bind('<FocusIn>', lambda event: on_entry_click(event, E_posta, "E-posta "))
  E_posta.bind('<FocusOut>', lambda event: on_entry_leave(event, E_posta, "E-posta "))
  
  Frame(frame,width=460,height=2,bg='black').place(x=20,y=280)


  #Parola alma  
  Parola=Entry(frame,width=250,fg='black',border=0,font=('Microsoft YaHei UI Lıght',11))
  Parola.place(x=70,y=320)
  Parola.insert(0,"Parola ")
  Parola.bind('<FocusIn>', lambda event: on_entry_click(event, Parola, "Parola "))
  Parola.bind('<FocusOut>', lambda event: on_entry_leave(event, Parola, "Parola "))

  Frame(frame,width=460,height=2,bg='black').place(x=20,y=350)

  #button bölümü

  Button(frame,width=50,pady=7,text='Kayıt ol',fg='white',bg='dark slate gray',border=0,font=('Microsoft YaHei UI Lıght',9),command=kayıt_yap).place(x=70,y=410)

  #hesap açma

  Label(frame,text="Kullanıcı hesabınız var mı ?",fg='black',bg='white',font=('Microsoft YaHei UI Lıght',9)).place(x=135,y=460)
  Button(frame,text='Giriş yap',fg='dark slate gray',bg='white',border=0,font=('Microsoft YaHei UI Lıght',9),command=Giriş_ekranı).place(x=290,y=460)

  

  master.mainloop()