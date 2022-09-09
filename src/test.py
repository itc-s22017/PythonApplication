import io
import json
import tkinter
import tkinter as tk
from urllib.request import urlopen
import string
import random
import requests
from PIL import ImageTk,ImageOps,ImageFilter
import tkinter.ttk as ttk
from tkinter import *
import PIL.Image
from tkinter import messagebox
from yt_dlp import YoutubeDL



class Tube:

    def __init__(self):
        self.root = tk.Tk()
        self.mp3 = MP3(self.root)
        self.root.bind("<KeyPress-Return>",self.ext)
        self.root.title("Youtube")
        self.root.geometry("1280x820+1000+0")
        self.root.resizable(width=False, height=False)

        self.txt = tkinter.Entry(width=30,cursor='xterm',bd=1,relief='solid',highlightcolor='blue')
        self.txt.place(x=400, y=765)
        
        self.btn = tk.Button(self.root, text="送信", command=self.submit,cursor='hand2',relief='solid')
        self.btn.place(x=660, y=760)

        self.btn2 = tk.Button(self.root, text="保存",command=self.save,cursor="hand2",relief='solid')
        self.btn2.place(x=715, y=760)
        
        self.btn3 = tk.Button(self.root, text="mp3",command=self.mp3.mp,cursor="hand2",relief='solid')
        self.btn3.place(x=770, y=760)
        
        self.count = 0
        
        self.v = StringVar()
        self.words = ["オリジナル","反転","ネガポジ反転","MinFilter","ぼかし","EMBOSS","COUNTER"]
        self.combobox = ttk.Combobox(self.root,width=10,values=self.words,textvariable=self.v,state='readonly')
        self.combobox.bind('<<ComboboxSelected>>', self.p)    
        self.combobox.current(0)
        self.combobox.place(x=840,y=765)
        
        self.canvas = tk.Canvas(self.root,height=720,width=1280,borderwidth=3)
        self.canvas.pack() 
        
        self.abel1 = tk.Label(self.root, text='URL:',font=('Bold',12))
        self.abel1.place(x=355,y=763)
                      
     
    def packncho(self,imgurl):
        
        self.root.update_idletasks()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
                
        self.u = urlopen(imgurl)
        self.rawdata = self.u.read()
        self.u.close()
        
        self.photo = ImageTk.PhotoImage(data=self.rawdata)
        self.label1 = self.canvas.create_image(self.canvas_width/2,self.canvas_height/2,image=self.photo,tag='li')
        self.canvas.pack()  
        
        self.ch()
        

    def dig(self,val):
        self.img = self.data["items"][0]["snippet"]["thumbnails"][val]["url"]
        self.packncho(self.img)
        
    def submit(self):
        
        self.val = self.txt.get()
        if not self.val.startswith("https://www.youtube.com/watch?") or self.val.count('https') >= 2:
            return
        
        if self.count != 0:
            self.canvas.delete('li')  
        self.count +=1
        
        self.id = self.txt.get()
        indx = self.id.find("=")
        id2 = self.id[indx +1:]
        
        self.url =f"https://www.googleapis.com/youtube/v3/videos?id={id2}&key=AIzaSyAVfs8wkC9EspUgkOEwgsCc8i4pT0HA-Z8&part=snippet"
            
        
        res = requests.get(self.url)
        self.data = res.json()
        

        if "maxres" in self.data["items"][0]["snippet"]["thumbnails"]:
            self.dig('maxres')
        elif "standard" in self.data["items"][0]["snippet"]["thumbnails"]:
            self.dig('standard')
        elif "high" in self.data["items"][0]["snippet"]["thumbnails"]:
            self.dig('high')
        elif "medium" in self.data["items"][0]["snippet"]["thumbnails"]:
            self.dig('medium')
        elif "default" in self.data["items"][0]["snippet"]["thumbnails"]:
            self.dig('default')

        #self.txt.delete(0, tkinter.END)
            


    def save(self):
        if not self.val.startswith("https://www.youtube.com/watch?") or self.val.count('https') >= 2:
            return
        
        path = string.ascii_lowercase
        a_z = "".join(random.sample(path,12))
        
        comb = self.combobox.get()
        self.val = self.txt.get() 
        
        file = io.BytesIO(
        urlopen(self.img).read()
        )
        img1 = PIL.Image.open(file)
        
                
        def aa(imges,word="オリジナル"):
            if comb == word:
                imges.save(f"/home/s22017/Desktop/try/PythonApplication/src/image/{a_z}.jpg",quality=95)
                
        Messagebox = tkinter.messagebox.askquestion('確認','本当に保存しますか？', icon='warning')
        if Messagebox == 'yes': 
            aa(img1)
            aa(img1.convert("L"),"反転")
            aa(ImageOps.invert(img1),"ネガポジ反転")
            aa(img1.filter(ImageFilter.MinFilter),"MinFilter")
            aa(img1.filter(ImageFilter.GaussianBlur(3)),"ぼかし")
            aa(img1.filter(ImageFilter.EMBOSS),"EMBOSS")
            aa(img1.filter(ImageFilter.CONTOUR),"COUNTER")
            self.saved('SAVED✓')
        else:
            tk.messagebox.showinfo('戻る','アプリケーション画面に戻ります')

        
            
    def saved(self,word):
        self.text = tk.Label(self.root,text=word,font=("Bold",10))
        self.text.pack()
        self.root.after(3000,self.delete)
        
    def delete(self):
        self.text.pack_forget()
        
    def cmb(self,word,ky):
        if self.V == word:
            self.conv = self.img1
            self.T = ImageTk.PhotoImage(ky)
            self.label1 = self.canvas.create_image(self.canvas_width/2,self.canvas_height/2,image=self.T,tag='li')
            self.canvas.pack() 
        
    def ch(self):
        
        self.val = self.txt.get() 
        if not self.val.startswith("https://www.youtube.com/watch?") or self.val.count('https') >= 2:
            return
        
        self.V = self.v.get()
        
        file = io.BytesIO(
        urlopen(self.img).read()
        )
        self.img1 = PIL.Image.open(file)
        self.conv=self.img1
       
        self.cmb("オリジナル",self.conv)
        self.cmb("反転",self.conv.convert("L"))
        self.cmb("ネガポジ反転",ImageOps.invert(self.conv))
        self.cmb("MinFilter",self.conv.filter(ImageFilter.MinFilter))
        self.cmb("ぼかし",self.conv.filter(ImageFilter.GaussianBlur(3.0)))
        self.cmb("EMBOSS",self.conv.filter(ImageFilter.EMBOSS))
        self.cmb("COUNTER",self.conv.filter(ImageFilter.CONTOUR))
        
    def p(self,evt): 
        self.ch()  
    
    def ext(self,evt):
        exit()
    
    def main(self):
        tk.mainloop()
        
        
class MP3:
    def __init__(self,root):
        self.root = root
        
    def mp(self):
        self.val = tube.txt.get()
        if not self.val.startswith("https://www.youtube.com/watch?") or self.val.count('https') >= 2:
            return
        
        ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':  "/home/s22017/Desktop/try/PythonApplication/src/music/" + '%(title)s'+'.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
         'preferredquality': '192'},
        {'key': 'FFmpegMetadata'},
    ],
}
        self.ydl = YoutubeDL(ydl_opts)
        
        Messagebox = tkinter.messagebox.askquestion('確認','本当に保存しますか？', icon='warning')
        if Messagebox == 'yes': 
            self.info_dict = self.ydl.extract_info(tube.id, download=True)  
            tube.saved('Downloaded✓')
        else:
            tk.messagebox.showinfo('戻る','アプリケーション画面に戻ります')
            
        
    
tube = Tube()
tube.main()

