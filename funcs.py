import matplotlib.pyplot as plt
import xlsxwriter as xw
import tkinter.messagebox as msgbox

def Calculate(p,pr) :
    amnt = 0
    try:
        cons = int(pr) - int(p)


        if cons <= 110 :
            amnt = cons * 50
        elif cons > 110 & cons <= 400 :
            amnt = cons * 79
        elif cons > 400 & cons <= 800 :
            amnt = cons * 79
        elif cons > 800 & cons <= 2000 :
            amnt = cons * 79

        if cons > 220 :
            amnt += 0.1925*amnt
        else :
            pass

    except ValueError as e:
        msgbox.showinfo("Error", "Enter integers only as previous and present reading !!! ")

    return amnt

def get_text(t_name) :
    s = ""
    from DBAdapter import retreive_for_draw,connect
    try:
        rows = retreive_for_draw(connect(),t_name)

        for row in rows :
            s+=str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+'\n'

    except Exception as e :
        msgbox.showinfo("Error", e)

    return s

def graph_data(t_name) :
    from DBAdapter import retreive_for_draw, connect
    try :
        data = retreive_for_draw(connect(), t_name)

        months = []
        cons = []

        for row in data[::-1] :
            months.append(row[0])
            cons.append(row[1])

        plt.grid()
        plt.xlabel("Month")
        plt.ylabel("Consumption")
        plt.plot(months, cons)
        plt.show()

    except Exception as e :
        msgbox.showinfo("Error",e)


def excel_output(name,residence,month,prev,pres):

    from DBAdapter import retreive, connect
    data = retreive(connect(), name+"_"+residence)


    try:
        wb = xw.Workbook('my_excel_file.xlsx')

        ws = wb.add_worksheet()

        ws.write('A2','Electric Bill App Output')

        ws.write('A5','Client Name : ')

        ws.write('C5',name )

        ws.write('A8','Client Residence : ')

        ws.write('C8',residence)

        ws.write('A10', 'Month/Year : ')

        ws.write('C10',month)

        ws.write('E10','Previous Reading : ')

        ws.write('G10', prev)

        ws.write('I10', 'Present Reading : ')

        ws.write('K10', pres)

        ws.write('A12','Month')

        ws.write('C12','Consumption')

        ws.write('E12','Amount')

        i = 14

        for row in data :
            ws.write('A'+str(i),row[0])
            ws.write('C'+str(i), row[1])
            ws.write('E'+str(i), row[2])
            i+=2

        wb.close()

    except Exception as e:
        msgbox.showinfo("Error", e)