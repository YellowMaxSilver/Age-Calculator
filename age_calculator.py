from tkinter import *
from tkinter.ttk import *
import datetime

data = datetime.date.today()

finalStr = ""

# year = int(input("Whats your year?: "));
# month = int(input("Whats your mouth?: "));
# day = int(input("Whats your day?: "));

def calc_date(year, month, day):
    global data
    global finalStr
    # return data;

    if len(str(year)) != 4:
        print('yearError')
        erroFunc('Invalid year value')
        
    elif len(str(month)) > 2 or len(str(month)) < 1:
        print('monthError')
        erroFunc('Invalid month value')

    elif len(str(day)) > 2 or len(str(day)) < 1:
        print('dayError')
        erroFunc('Invalid day value')
    else:
        try:
            current_day = data.day
            current_mouth = data.month
            current_year = data.year

            bole_mouth = TRUE
            bole_year = TRUE
            final_mouth = (current_mouth - month)
            final_year = (current_year - year)

            if (current_day - day) < 0:
                # not aniversary mouth - 1;2007
                bole_mouth = FALSE
            else:
                bole_mouth = TRUE

            if (current_mouth - month) < 0:
                # not aniversay year mouth
                bole_year = FALSE
            else:
                bole_year = TRUE

            if bole_mouth == FALSE:
                final_mouth = (current_mouth - month) - 1

            if final_mouth < 0:
                bole_year = FALSE

            if bole_year == FALSE:
                final_year = (current_year - year) - 1
            elif bole_year == TRUE:
                final_year = (current_year - year)

            print("you have: ", final_year)
            ao_year = str(final_year)
            finalStr = 'you have: '+ao_year+' years old'
            print(finalStr)

        except:
            erroFunc('404 erro')
            print("erroInFunc")


def get_values():
    try:
        year = int(yk_text_box_year.get())
        month = int(yk_text_box_mouth.get())
        day = int(yk_text_box_day.get())

        calc_date(year, month, day)
        erro_menssage.set("")
        faca.set(finalStr)
    except:
        erroFunc('Invalid Value')


def erroFunc(status):
    print("error"+status)
    erro_menssage.set(status)
    faca.set("")

# calc_date(year,month,day)
window = Tk()
window.title("Data Nascimento")
window.geometry("600x400")

label1 = Label(window, text="Calcule sua data de nascimento:")
label1.grid(column=1, row=1)

yk_label_box_year = Label(text="Year")
yk_label_box_year.grid(column=1, row=2, padx=20)

yk_label_box_month = Label(text="Month")
yk_label_box_month.grid(column=2, row=2, padx=20)

yk_label_box_month = Label(text="Day")
yk_label_box_month.grid(column=3, row=2, padx=20)

yk_text_box_year = Entry()
yk_text_box_year.grid(column=1, row=3, padx=20)

yk_text_box_mouth = Entry()
yk_text_box_mouth.grid(column=2, row=3)

yk_text_box_day = Entry()
yk_text_box_day.grid(column=3, row=3, padx=20)

yk_next_button = Button(text="Next", command=get_values)
yk_next_button.grid(column=2, row=4, pady=(20, 0))

faca = StringVar()
erro_menssage = StringVar()

yk_label_erro = Label(textvariable=erro_menssage, foreground='red')
yk_label_erro.grid(column=2, row=5)

yk_label_result = Label(textvariable=faca, foreground='blue')
yk_label_result.grid(column=2, row=5)

window.mainloop()