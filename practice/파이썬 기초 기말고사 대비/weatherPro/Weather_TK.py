#-*- coding:utf-8 -*-
import tkinter as tk
from urllib.request import urlopen
import urllib.request, json
from PIL import ImageTk,Image


class Window:
    def __init__(self):
        self.url1 = "http://api.openweathermap.org/data/2.5/weather?id="
        self.url2 = "&APPID=2ae88b3ec4b4537d15165fca377a3ca9"
        self.window = tk.Tk()
        self.window.geometry("640x480")
        self.window.resizable(False, False)
        self.window.title("Weather Pro")

        self.f1 = tk.Frame(self.window, bd=2, padx=5, pady=5)
        self.f2 = tk.Frame(self.window, bd=2, padx=5, pady=5)

        file2 = open("city.list.json", encoding='utf-8-sig').read()
        cities = json.loads(file2)

        listbox = tk.Listbox(self.f1, selectmode='extended', height=0)

        self.nameID = {}
        for city in cities:
            if city['country'] == 'KR':
                self.nameID[city['name']] = city['id']

        cityList  = ['Yeoju','Yanggu','Mungyeong','Kurye','Chinchon','Hamyang','yeoncheongun','Yangpyong','Yangju','Wanju','Waegwan','Vijongbu','Puan','Asan','Munsan','Kwangju','Kuri','Kumi','Gimcheon']
        cityList += ['Gapyeong','Hwaseong','Hwacheon','Hongsung','Hongchon','jin-angun','Tonghae','Seongnam','Hwado','Changnyeong','Taian','Songwon','Kosong','Kijang','Imsil','Sinan','Andong']
        cityList += ['Ulsan','Busan','Ansan','Daegu','Kimhae','Munemi','Wonju','Masan','Iksan','Yongin','Pyongtak','Chinju','Bucheon','Gwangju','Jeju','Yangsan','Cheongju','Chuncheon','Goyang']
        cityList += ['Yanggok','Tenan','Yesan','Kongju','Chinhae','Kunsan','Moppo','Anyang','Jeonju','Reisui','Sogcho','Hanam','Kang-neung','Sunchun','Miryang','Hadong','Sangju']
        cityList += ['Suisan','Osan','Ichon','Kimje','Nonsan','Inje','Yangyang','Goseong','Muju','Nangen','Haenam','Muan','Hwasun','Naju','Kyonju','Namhae','Kwangmyong','Kochang','Taebaekv']
        cityList += ['Koesan','Pyeong','Ulchin','Namyang','Tangjin','Kanghwa','Daejeon','Suigen','Seoul','Incheon','Changwon','Anseong','Wabu']
        cityList.sort()
        i = 0
        for city in cityList:
            listbox.insert(i,city)
            i += 1

        listbox.bind("<<ListboxSelect>>", self.selected)
        listbox.pack()
        self.imgLabel = tk.Label(self.f2, width=210, height=150, relief=tk.RAISED, pady=50)
        self.imgLabel.pack()
        img = Image.open("./weatherIcon/open1.jpg")
        image = ImageTk.PhotoImage(img)
        self.imgLabel.config(image=image)
        img.close()

        self.label1 = tk.Label(self.f2, text="날씨: " , width=30, height=5, fg="red", relief=tk.RAISED, pady=25)
        self.label2 = tk.Label(self.f2, text="온도: " , width=30, height=5, fg="red", relief=tk.RAISED, pady=25)
        self.label3 = tk.Label(self.f2, text="습도: " , width=30, height=5, fg="red", relief=tk.RAISED, pady=25)
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.f1.pack(side="left")
        self.f2.pack()
        self.window.mainloop()

    def selected(self,event):
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        url = self.url1 + str(self.nameID[value]) + self.url2
        file1 = urllib.request.urlopen(url)
        s = json.loads(file1.read())
        # print(s)
        # print(s['weather'][0]['description'], s['weather'][0]['icon'])
        # print(s['main']['temp'] - 273.15, s['main']['humidity'] )
        iconURL = 'http://openweathermap.org/img/w/' + s['weather'][0]['icon'] +'.png'
        image = Image.open(urlopen(iconURL))

        if image.size[1] > image.size[0]:
            hSize = int((200 * image.size[0] / image.size[1]))
            vSize = 200
        else:
            hSize = 200
            vSize = int((200 * image.size[1] / image.size[0]))

        image = image.resize((hSize,vSize), Image.ANTIALIAS)
        _image = ImageTk.PhotoImage(image)
        self.imgLabel.config(image=_image)
        image.close()
        self.label1.configure(text = "날씨: " + s['weather'][0]['description'])
        self.label2.configure(text = "온도: " + str(int(s['main']['temp'] - 273.15)))
        self.label3.configure(text = "습도: " + str(s['main']['humidity']))
        self.window.mainloop()

a = Window()

