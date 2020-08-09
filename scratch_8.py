

from PIL import Image,ImageOps
from PIL import ImageEnhance,ImageFilter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m
dub,image="",""
# n=0
count=0

win=tk.Tk()###to create our GUI window
win.title("SHUBHAM")
win1=ttk.LabelFrame(win)
win1.grid(row=0,column=0,padx=500,pady=100)
label1=tk.Label(win1,text="Image Editor",fg="Red")
label1.grid(row=0,columnspan=6,padx=120,pady=10)
label2=tk.Label(win1,text="Provide Image path :",fg="#48B5B5")
label2.grid(row=1,column=0,columnspan=2,sticky=tk.W)
IP=tk.StringVar()
entry1=ttk.Entry(win1,width=30,textvariable=IP)
entry1.grid(row=1,column=1,columnspan=3,padx=2)
entry1.focus()
label3=tk.Label(win1,text="Image Enhancer :",fg="#B548A7")
label3.grid(row=2,columnspan=2,sticky=tk.W,pady=10)
label4=tk.Label(win1,text="operation :",fg="#9348B5")
label4.grid(row=3,column=0,sticky=tk.W)
op=tk.StringVar()
op1=ttk.Combobox(win1,width=10,state="readonly",textvariable=op)
op1["values"]=("Sharpness","Brightness")
op1.current(1)
op1.grid(row=3,column=1)
label5=tk.Label(win1,text="Range :",fg="#9348B5")
label5.grid(row=3,column=2)
R=tk.StringVar()
val=(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2)
r1=tk.Spinbox(win1,from_=0.0,to=2.0,width=5,textvariable=R,values=val)
# r1["values"]=("1","2")
r1.grid(row=3,column=3)
##################################################################################################

def show():
    global dub
    global image
    global count
    # count+=1
    # path=IP.get()+".jpg"
    if count==0:
        count+=1
        path = IP.get() + ".jpg"
        try:
            image = Image.open(path)
        except FileNotFoundError:
            path = IP.get() + ".png"
            image = Image.open(path)
        dub = image.copy()

    O=op.get()
    v=float(R.get())
    # try:
    #     img=Image.open(path)
    # except FileNotFoundError:
    #     path = IP.get() + ".png"
    #     img = Image.open(path)
    if O == "Sharpness":
        dub = ImageEnhance.Sharpness(dub)
        dub=dub.enhance(v)
        dub.show()
    if O == "Brightness":
        dub = ImageEnhance.Brightness(dub)
        dub=dub.enhance(v)
        dub.show()

submitBtn=ttk.Button(win1,text="SHOW",command=show)
submitBtn.grid(row=4,column=1,columnspan=3,padx=50,pady=10)

###########################################################################################

label6=tk.Label(win1,text="Image Filter :",fg="#B548A7")
label6.grid(row=5,columnspan=2,sticky=tk.W,pady=10)
label4=tk.Label(win1,text="operation :",fg="#9348B5")
label4.grid(row=6,column=0,sticky=tk.W)
OP=tk.StringVar()
op2=ttk.Combobox(win1,width=15,state="readonly",textvariable=OP)
op2["values"]=("GaussianBlur","BoxBlur","UnsharpMask")
op2.current(0)
op2.grid(row=7,column=1)
label7=tk.Label(win1,text="Radius :",fg="#9348B5")
label7.grid(row=7,column=2)
RR=tk.StringVar()
r2=tk.Spinbox(win1,width=6,from_=0,to=1000,textvariable=RR)
r2.grid(row=7,column=3)

###################################################################################

def detail():
    global dub
    global image
    global count

    if count == 0:
        count += 1
        path = IP.get() + ".jpg"
        try:
            image = Image.open(path)
        except FileNotFoundError:
            path = IP.get() + ".png"
            image = Image.open(path)
        dub = image.copy()

    detail="TYPE -->{}\n SIZE -->{}\nMODE -->{}".format(image.format,image.size,image.mode)
    l = tk.Label(win1, text=detail, fg="Black")
    l.grid(row=1, column=4,columnspan=3, padx=120, pady=10)

submitBt=ttk.Button(win1,text="Show Detail",command=detail)
submitBt.grid(row=1,column=2,columnspan=3,padx=50,pady=10)

###############################################################################################################


def show1():
    global dub
    global image
    global count
    OO= OP.get()
    vl = float(RR.get())
    if count==0:
        count+=1
        path = IP.get() + ".jpg"
        try:
            image = Image.open(path)
        except FileNotFoundError:
            path = IP.get() + ".png"
            image = Image.open(path)
        dub = image.copy()
    w, h = dub.size

    if vl<w and vl<h:
        if OO == "GaussianBlur":
            dub=dub.filter(ImageFilter.GaussianBlur(radius=vl))
            dub.show()
        if OO== "BoxBlur":
            dub=dub.filter(ImageFilter.BoxBlur(radius=vl))
            dub.show()
        if OO== "UnsharpMask":
            img1=image.filter(ImageFilter.UnsharpMask(radius=vl,percent=100, threshold=10))
            img1.show()
    else:
        m.showerror("error","radius out of size")

submitBtn=ttk.Button(win1,text="SHOW",command=show1)
submitBtn.grid(row=8,column=1,columnspan=3,padx=50,pady=10)

#############################################################################################################


label8=tk.Label(win1,text="Special operation :",fg="#9348B5")
label8.grid(row=9,column=0,columnspan=2, sticky=tk.W)
OP1=tk.StringVar()
op3=ttk.Combobox(win1,width=15,state="readonly",textvariable=OP1)
op3["values"]=("EDGE_ENHANCE","CONTOUR","BLUR","MirrorView","Flip","Border","EMBOSS","FIND_EDGES","SMOOTH","SMOOTH_MORE","SHARPEN")
op3.current(0)
op3.grid(row=10,column=1)

#############################################################################################################################################


def apply():
    global dub
    global image
    global count

    OO= OP1.get()
    if count==0:
        count+=1
        path = IP.get() + ".jpg"
        try:
            image = Image.open(path)
        except FileNotFoundError:
            path = IP.get() + ".png"
            image = Image.open(path)
        dub = image.copy()
    if OO == "EDGE_ENHANCE":
        dub=dub.filter(ImageFilter.EDGE_ENHANCE())
        dub.show()
    if OO== "BLUR":
        dub=dub.filter(ImageFilter.BLUR())
        dub.show()
    if OO== "CONTOUR":
        img2=image.filter(ImageFilter.CONTOUR())
        img2.show()
    if OO == "MirrorView":
        dub=ImageOps.mirror(dub)
        dub.show()
    if OO == "Flip":
        dub=ImageOps.flip(dub)
        dub.show()
    if OO == "Border":
        dub=ImageOps.expand(dub,border=20,fill="black")
        dub.show()
    if OO == "EMBOSS":
        img2=image.filter(ImageFilter.EMBOSS)
        img2.show()
    if OO == "FIND_EDGES":
        img2=image.filter(ImageFilter.FIND_EDGES)
        img2.show()
    if OO == "SHARPEN":
        dub=dub.filter(ImageFilter.SHARPEN)
        dub.show()
    if OO == "SMOOTH":
        dub=dub.filter(ImageFilter.SMOOTH)
        dub.show()
    if OO == "SMOOTH_MORE":
        dub=dub.filter(ImageFilter.SMOOTH_MORE)
        dub.show()

submitBtn1=ttk.Button(win1,text="APPLY",command=apply)
submitBtn1.grid(row=10,column=2,columnspan=2,padx=50,pady=10)

###############################################################################################################

def apply1():
    global dub
    global image
    global count
    d= dgr.get()
    if count==0:
        count+=1
        path = IP.get() + ".jpg"
        try:
            image = Image.open(path)
        except FileNotFoundError:
            path = IP.get() + ".png"
            image = Image.open(path)
        dub = image.copy()
    dub=dub.rotate(d)
    dub.show()


label9=tk.Label(win1,text="Rotation :",fg="#9348B5")
label9.grid(row=11,column=0,columnspan=2,sticky=tk.W)
label10=tk.Label(win1,text="Degree :",fg="#9348B5")
label10.grid(row=12,column=1,sticky=tk.W)
dgr=tk.IntVar()
r3=tk.Spinbox(win1,width=6,from_=0,to=360,textvariable=dgr)
r3.grid(row=12,column=2)

submitBtn2=ttk.Button(win1,text="ROTATE",command=apply1)
submitBtn2.grid(row=12,column=4,padx=50,pady=10)

########################################################################################################


label11=tk.Label(win1,text="change color :",fg="#9348B5")
label11.grid(row=13,column=0,columnspan=2,sticky=tk.W)
label11=tk.Label(win1,text="format :",fg="#9348B5")
label11.grid(row=13,column=2,sticky=tk.W)
OP3=tk.StringVar()
op4=ttk.Combobox(win1,width=10,state="readonly",textvariable=OP3)
op4["values"]=("BnW","(r,g,b)","(r,b,g)","(b,r,g)","(g,r,b)","(g,b,r)","(b,g,r)")
op4.current(0)
op4.grid(row=13,column=3)

def apply2():
    global dub
    global image
    global count

    if count == 0:
        count += 1
        path = IP.get() + ".jpg"
        try:
            image = Image.open(path)
        except FileNotFoundError:
            path = IP.get() + ".png"
            image = Image.open(path)
        dub = image.copy()
    clr= OP3.get()

    r,g,b=dub.split()
    if clr=="(r,g,b)":
        dub=Image.merge("RGB",(r,g,b))
        dub.show()
    if clr=="(r,b,g)":
        dub=Image.merge("RGB",(r,b,g))
        dub.show()
    if clr=="(b,r,g)":
        dub=Image.merge("RGB",(b,r,g))
        dub.show()
    if clr=="(g,r,b)":
        dub=Image.merge("RGB",(g,r,b))
        dub.show()
    if clr=="(g,b,r)":
        dub=Image.merge("RGB",(g,b,r))
        dub.show()
    if clr=="(b,g,r)":
        dub=Image.merge("RGB",(b,g,r))
        dub.show()
    if clr =="BnW":
        image.convert('L').show()

submitBtn3=ttk.Button(win1,text="APPLY",command=apply2)
submitBtn3.grid(row=13,column=4,padx=50,pady=10)

################################################################################################

def reset():
    global count
    if count>0:
        count=0
        m.showinfo("Info", "Reset Successfully!")
    else:
        m.showerror("error", "No changes made yet")

submitBtn4=ttk.Button(win1,text="RESET",command=reset)
submitBtn4.grid(row=15,column=1,padx=50,pady=10)

##################################################################################################

def save():
    global count
    global dub
    i=0

    if count==0:
        m.showerror("error", "Nothing to save")
    else:
        p=IP.get()
        dub.save("{}{}{}".format(p,count,".jpg"))
        i+=1
        m.showinfo("Info", "Saved Successfully!")

submitBtn5=ttk.Button(win1,text="SAVE",command=save)
submitBtn5.grid(row=15,column=3,padx=50,pady=10)
win.mainloop()