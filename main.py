import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
from funcs import *
from DBAdapter import *


def OnOKButtonClick(name, residence, prev, pres, mnth ):
    if len(name)==0 or len(residence)==0 or len(prev)==0 or len(pres)==0 :
        messagebox.showinfo("Error","Fill all fields")
    else :
        out_label['text'] = "Amount to be Paid : "+str(Calculate(prev,pres))+" FCFA"
        create_table(connect(),name+"_"+residence)
        try:
            insert(connect(), name + "_" + residence, mnth, int(pres) - int(prev), Calculate(prev, pres))
            l_label = tk.Label(frame2, text=get_text(name + "_" + residence))
            l_label.place(rely=0.55, relwidth=1)
            excel_output(name, residence, mnth, prev, pres)

        except ValueError:
            pass


root = tk.Tk()
root.title("Electric Bill App")

canvas = tk.Canvas(root,height=500,width=500)
canvas.pack()

frame = tk.Frame(root,bg='midnightblue',bd=5)
frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.3,anchor='n')

img = Image.open("downloadfile.jpg").resize((130, 130), Image.ANTIALIAS)
tof = ImageTk.PhotoImage(img)

logo_label = tk.Label(frame,image=tof)
logo_label.place(relwidth=0.275,relheight=1)

mbr_label = tk.Label(frame,text="Author :\t Yamsi Tchuisseu Joy Sylver\nThis is a simple electric billing app.\nIt " 
                                   "stores the different values given per \nmonth per user in a database.It graphs " 
                                   "consumptions \nper month for a given user for the last six months.\nIt outputs an excel" 
                                   "file containing \nsome relevant information.\n Have fun using it.")
mbr_label.place(relx=0.283,relwidth=0.724,relheight=1)

frame2 = tk.Frame(root,bg='midnightblue',bd=5)
frame2.place(relx=0.5,rely=0.31,relwidth=1,relheight=0.68,anchor='n')

from datetime import datetime as dt
month = dt.now().month
year = dt.now().year
values = []
for i in range(1, 13, 1):
    values.append(str(i)+"/"+str(year))
    i += 1

mnth_box = ttk.Combobox(frame2,values=values, state="readonly")
mnth_box.place(relx=0.7, relheight=0.1, relwidth=0.3)

current = None
for m in values:
    if str(m.split("/")[0]) == str(month) :
        current = values.index(m)
mnth_box.current(current)

name_label = tk.Label(frame2,text="Name :")
name_label.place(rely=0.11,relwidth = 0.3,relheight=0.1)

name_entry = tk.Entry(frame2,bg='white')
name_entry.place(rely=0.11,relx=0.31,relwidth=0.69,relheight=0.1)

res_label = tk.Label(frame2,text="Residence :")
res_label.place(rely=0.22,relwidth = 0.3,relheight=0.1)

res_entry = tk.Entry(frame2,bg='white')
res_entry.place(rely=0.22,relx=0.31,relwidth=0.69,relheight=0.1)

prev_label = tk.Label(frame2,text="Previous :")
prev_label.place(rely=0.33,relwidth = 0.2,relheight=0.1)

prev_entry = tk.Entry(frame2,bg='white')
prev_entry.place(rely=0.33,relx=0.21,relwidth=0.3,relheight=0.1)

pres_label = tk.Label(frame2,text="Present :")
pres_label.place(relx=0.52,rely=0.33,relwidth = 0.2,relheight=0.1)

pres_entry = tk.Entry(frame2,bg='white')
pres_entry.place(rely=0.33,relx=0.73,relwidth=0.27,relheight=0.1)

ok_button = tk.Button(frame2,text="OK", command = lambda : OnOKButtonClick(name_entry.get(),
                                                                           res_entry.get(),prev_entry.get(),
                                                                           pres_entry.get(),mnth_box.get()))
ok_button.place(rely=0.44,relheight=0.1,relwidth=0.14)

graph_button = tk.Button(frame2,text="Graph",command = lambda : graph_data(str(name_entry.get())+"_"+str(res_entry.get()))
                                        if len(name_entry.get())!=0 and len(res_entry.get())!=0 else  messagebox.showinfo("Error",""
                                                                            "Fill at least name and residence fields !!!") )
graph_button.place(relx=0.15,rely=0.44,relheight=0.1,relwidth=0.14)

out_label = tk.Label(frame2)
out_label.place(rely=0.44,relx=0.30,relheight=0.1,relwidth=0.70)

root.resizable(False,False)
root.mainloop()
