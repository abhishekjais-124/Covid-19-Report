import tkinter as tk
from covid import Covid

covid = Covid(source = "worldometers")
countries = covid.list_countries()
t_act = covid.get_total_active_cases()
t_cnfrm = covid.get_total_confirmed_cases()
t_rec = covid.get_total_recovered()
t_dth = covid.get_total_deaths()

def start(event):
    ask()

def ask():
    e.focus_set()
    country = str(e.get()).lower()
    if country not in countries:
        e.delete(0, tk.END)
        label.config(fg='red', text= str(country) + " not found!!")
    else:
        res1 = covid.get_status_by_country_name(country)
        a = res1['country'];b = res1['confirmed'];c = res1['new_cases']
        aa = res1['deaths'];bb = res1['recovered'];cc = res1['active']
        aaa = res1['critical'];bbb = res1['total_tests']
        text1 = "Country: " + str(a) + "\n" + "Confirmed Cases: " + str(b) + '\n' +"New Cases: " + str(c) + '\n' +"Total deaths: " + str(aa) + '\n' + "Total recovered: " + str(bb) + '\n' +"Active Cases: " + str(cc) + '\n' +"Critical Cases: " + str(aaa) + '\n' +"Total Tests: " + str(bbb)
        e.delete(0, tk.END)
        label.config(fg='blue', text= text1)



##############################################################################################################################################################
root = tk.Tk()
root.title("Covid Data")
root.geometry("1000x700")

instructions =  tk.Label(root,text = "Search for your Country Here!",font = ('Helvetica',22))
instructions.pack(ipady = 10)

instr2 = tk.Label(root,text = "Press enter to search", font = ('Helvetica',12,'bold'))
instr2.pack(ipady = 5)

e = tk.Entry(root)

root.bind('<Return>',start)
e.pack(ipady = 5,ipadx = 30)



text2 = "Total Active Cases: " + str(t_act) + '\n'+  "Total Confirmed Cases: " + str(t_cnfrm) + '\n' + "Total recovered worldwide: " + str(t_rec) + '\n' + "Total Deaths: " + str(t_dth)
label = tk.Label(root,text = text2, font = ('Helvetica',30))
label.pack(ipady = 50)



e.focus_set() #set focus to the entry box

root.mainloop()