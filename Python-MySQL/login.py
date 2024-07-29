from tkinter import*
from tkinter import messagebox
import mysql.connector
import kayıt
import randevu
from PIL import Image, ImageTk

def login_(): 

     mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="1234",
     database='users'
     
     )

     mycursor = mydb.cursor()



     def kayıt_ol():
          master.destroy()
          kayıt.kayıt_()

     def randevu_giriş():
          master.destroy()
          randevu.randevu_() 

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







     def Giriş_yap():
          
          kullanici_adi=kullanici.get()
          sifre_=şifre.get()
          
          yeni=mydb.cursor()
          yeni.execute("SELECT kullanici_adi, kullanici_sifre FROM kullanici")
          verilerim=yeni.fetchall() 

          yeni.execute("SELECT COUNT(*) AS ToplamVeriSayisi FROM kullanici")
          ikincisorgu = yeni.fetchone()
          kayitsayisi = int(ikincisorgu[0])
          
          a = 1
          i = 0 
          while i < kayitsayisi:
               if kullanici_adi == verilerim[i][0] and sifre_ == verilerim[i][1]:
                    a = a + 1
                    randevu_giriş()
                    
                    break
               i = i + 1
          if a == 1:
               messagebox.showerror("Uyarı", "Yanlış Şifre veya Kullanıcı adı")
               
          
               
     


     # Resmi yükle
     resim = Image.open("jpg/giris.jpg")

     # Resmi yeniden boyutlandır
     org_genislik, org_yukseklik = resim.size
     hedef_genislik = 450
     hedef_yukseklik = int((org_yukseklik / org_genislik) * hedef_genislik)

     resim.thumbnail((hedef_genislik, hedef_yukseklik), Image.LANCZOS)  # Resmi yeniden boyutlandır

     # Resmi ImageTk.PhotoImage ile işle
     img = ImageTk.PhotoImage(resim)

     # Label içerisinde resmi göster
     label = Label(master, image=img, bg='white')
     label.place(x=70,y=110)




     frame=Frame(master,width=500,height=500,background="white")
     frame.place(x=500,y=100)
     frame.lift() #frame fonksiyonunu öne çıkartır yani üst katman yapar

     #header bölümü
     header = Label(frame,text="Giriş yapınız",fg='dark slate gray',bg='white',font=('Microsoft YaHei UI Lıght',23,'bold'))
     header.place(x=110,y=30)

     #kullanıcı adını alma
       

     kullanici=Entry(frame,width=250,fg='black',border=0,font=('Microsoft YaHei UI Lıght',11))
     kullanici.place(x=30,y=110)
     kullanici.insert(0,"Kullanıcı adınızı giriniz")
     kullanici.bind('<FocusIn>', lambda event: on_entry_click(event, kullanici, "Kullanıcı adınızı giriniz"))
     kullanici.bind('<FocusOut>', lambda event: on_entry_leave(event, kullanici, "Kullanıcı adınızı giriniz"))

     Frame(frame,width=400,height=2,bg='black').place(x=20,y=140)



     #şifre alma 
     şifre=Entry(frame,width=250,fg='black',border=0,show='*',font=('Microsoft YaHei UI Lıght',11))
     şifre.place(x=30,y=180)
     şifre.insert(0,"Şifrenizi giriniz")
     şifre.bind('<FocusIn>', lambda event: on_entry_click(event, şifre, "Şifrenizi giriniz"))
     şifre.bind('<FocusOut>', lambda event: on_entry_leave(event, şifre, "Şifrenizi giriniz"))
     Frame(frame,width=400,height=2,bg='black').place(x=20,y=210)


     #button bölümü

     Button(frame,width=50,pady=7,text='Giriş yapınız',fg='white',bg='dark slate gray',border=0,font=('Microsoft YaHei UI Lıght',9),command=Giriş_yap).place(x=45,y=250)

     #hesap açma

     Label(frame,text="Kullanıcı hesabınız yok mu ?",fg='black',bg='white',font=('Microsoft YaHei UI Lıght',9)).place(x=110,y=300)
     Button(frame,text='Kayıt ol',fg='dark slate gray',bg='white',border=0,font=('Microsoft YaHei UI Lıght',9),command=kayıt_ol).place(x=270,y=300)




     master.mainloop()
