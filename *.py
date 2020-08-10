#看，这货又没写注释
import tkinter as tk
import math
def func():
    color="red"
    def setcolor():
        nonlocal color
        color=dr_e_c.get()
        print("color set "+color)
        dr_log.insert("1.0","color set "+color+'\n')
    def dr():
        nonlocal color
        nonlocal dr_cn_
        _c__=color
        _dr=dr_e_.get()
        if _dr[0:7]=='circle ':
            dr_cn_.create_oval(int(_dr.split()[1])+int(_dr.split()[3]),int(_dr.split()[2])+int(_dr.split()[3]),int(_dr.split()[1])-int(_dr.split()[3]),int(_dr.split()[2])-int(_dr.split()[3]),fill=_c__)
            print("circle:x "+_dr.split()[1]+',y '+_dr.split()[2]+',r '+_dr.split()[3])
            dr_log.insert("1.0","circle:x "+_dr.split()[1]+',y '+_dr.split()[2]+',r '+_dr.split()[3]+"\n")
        if _dr[0:7]=="square ":
            dr_cn_.create_rectangle(_dr.split()[1],_dr.split()[2],_dr.split()[3],_dr.split()[4],fill=_c__)
            print("rectangle:x1 "+_dr.split()[1]+',y1 '+_dr.split()[2]+',x2 '+_dr.split()[3]+',y2 '+_dr.split()[4])
            dr_log.insert("1.0","rectangle:x1 "+_dr.split()[1]+',y1 '+_dr.split()[2]+',x2 '+_dr.split()[3]+',y2 '+_dr.split()[4]+"\n")
        if _dr[0:6]=='funca ':
            for dr_i in range(201):
                dr_j=0.0
                dr_j=dr_i*0.1-10.0
                dr_res=eval(_dr.split()[1].replace('X','('+str(dr_j)+')'))
                dr_cn_.create_oval(3.6*dr_i+3,403-14.4*dr_res,3.6*dr_i-3,397-14.4*dr_res,fill=_c__)
            print("Y="+_dr.split()[1])
            dr_log.insert("1.0","Y="+_dr.split()[1]+"\n")
        if _dr[0:6]=='funcb ':
            for dr_i in range(201):
                dr_j=0.0
                dr_j=dr_i*0.1-10.0
                dr_res=eval(_dr.split()[1].replace('X','('+str(dr_j)+')'))
                dr_cn_.create_oval(3.6*dr_i+3,400-14.4*dr_res,3.6*dr_i-3,0,fill=_c__)
            print("Y="+_dr.split()[1])
            dr_log.insert("1.0","_Y="+_dr.split()[1]+"\n")
        if _dr[0:6]=='funcc ':
            for dr_i in range(201):
                dr_j=0.0
                dr_j=dr_i*0.1-10.0
                dr_res=eval(_dr.split()[1].replace('X','('+str(dr_j)+')'))
                dr_cn_.create_oval(3.6*dr_i+3,400-14.4*dr_res,3.6*dr_i-3,800,fill=_c__)
            print("Y="+_dr.split()[1])
            dr_log.insert("1.0",".Y="+_dr.split()[1]+"\n")
        if _dr[0:5]=='line ':
            dr_cn_.create_line(_dr.split()[1],_dr.split()[2],_dr.split()[3],_dr.split()[4],fill=_c__)
            print("line,from:"+_dr.split()[1]+','+_dr.split()[2]+'  to:'+_dr.split()[3]+','+_dr.split()[4])
            dr_log.insert("1.0","line,from:"+_dr.split()[1]+','+_dr.split()[2]+'  to:'+_dr.split()[3]+','+_dr.split()[4]+"\n")
        if _dr[0:6]=="lines ":
            for i in range(int((math.sqrt((int(_dr.split()[1])-int(_dr.split()[3]))**2+(int(_dr.split()[2])-int(_dr.split()[4]))**2))/8.0)+1):
                x__x__=int((math.sqrt((int(_dr.split()[1])-int(_dr.split()[3]))**2+(int(_dr.split()[2])-int(_dr.split()[4]))**2))/8.0)
                linesx=(x__x__-i)*1.0/x__x__*int(_dr.split()[1])+i*1.0/x__x__*int(_dr.split()[3])
                linesy=(x__x__-i)*1.0/x__x__*int(_dr.split()[2])+i*1.0/x__x__*int(_dr.split()[4])
                dr_cn_.create_oval(linesx+3,linesy+3,linesx-3,linesy-3,fill=_c__)
            print("lines,from:"+_dr.split()[1]+','+_dr.split()[2]+'  to:'+_dr.split()[3]+','+_dr.split()[4])
            dr_log.insert("1.0","lines,from:"+_dr.split()[1]+','+_dr.split()[2]+'  to:'+_dr.split()[3]+','+_dr.split()[4]+"\n")
        if _dr[0:7]=="func+a ":
            for dr_i in range(201):
                dr_j=0.0
                dr_j=dr_i*0.1-10.0
                try:
                    dr_res=eval(_dr.split()[1].replace('X','('+str(dr_j)+')'))
                    dr_cn_.create_oval(3.6*dr_i+3,403-14.4*dr_res,3.6*dr_i-3,397-14.4*dr_res,fill=_c__)
                except:
                    dr_i=dr_i
            print(" Y="+_dr.split()[1])
            dr_log.insert("1.0"," Y="+_dr.split()[1]+"\n")
        if _dr[0:7]=="func+b ":
            for dr_i in range(201):
                dr_j=0.0
                dr_j=dr_i*0.1-10.0
                dr_k=dr_j-0.1
                try:
                    dr_res=eval(_dr.split()[1].replace('X','('+str(dr_j)+')'))
                except:
                    dr_res=False
                try:
                    dr_resk=eval(_dr.split()[1].replace('X','('+str(dr_k)+')'))
                except:
                    dr_resk=False
                if dr_res!=False:
                    if dr_resk!=False:
                        dr_cn_.create_line(3.6*dr_i,400-14.4*dr_res,3.6*dr_i-3.6,400-14.4*dr_resk,fill=_c__)
            print("*Y="+_dr.split()[1])
            dr_log.insert("1.0"," *Y="+_dr.split()[1]+"\n")
    tk_c=tk.Tk()
    tk_c.geometry("720x800")
    dr_title=tk.Label(tk_c,text='720*800ggb(假的)', bg='aqua', font=('Arial', 12), width=30, height=2)
    dr_e_ = tk.Entry(tk_c,show=None, font=('Arial', 14))
    dr_e_c = tk.Entry(tk_c,show=None, font=('Arial', 14))
    dr_b_c=tk.Button(tk_c,text='set color', width=10,height=2, command=setcolor)
    dr_b_ = tk.Button(tk_c,text='draw', width=10,height=2, command=dr)
    dr_cn_= tk.Canvas(tk_c,bg="aqua",confine=True,height=540,width=720)
    dr_log=tk.Text(tk_c,height=5)
    dr_title.pack()
    dr_e_.pack()
    dr_b_.pack()
    dr_cn_.pack()
    dr_e_c.pack()
    dr_b_c.pack()
    dr_log.pack()
    tk_c.mainloop()
func()
