import tkinter


window = tkinter.Tk()
window.title("bmi hesaplama")
window.config(padx=40, pady=40)
window.configure(background="rosy brown")


def calculator_bmi(height_input=None, weight_input=None):
    height = height_input.get()
    weight = weight_input.get()
    

    if weight == "" or height == "":
        result_label.config(text="Boyunuzu ve kilonuzu giriniz")

    else:
        try:
            bmi = float(weight) / (float(height)) ** 2
            result_label.config(text=f"1Your bmi: {bmi}")
        except:
            result_label.config(text="Enter a Valid number")

height_label = tkinter.Label(text="boyunuzu Giriniz (cm)")
height_label.pack()
height_label.configure(background="Light pink")
height_label = tkinter.Entry(width=20)
height_label.pack()

weight_label = tkinter.Label(text="Kilonuzu Giriniz")
weight_label.configure(background="Light pink")
weight_label.pack()

weight_label = tkinter.Entry(width=20)
weight_label.pack()

calculator_button = tkinter.Button(text="Calculator",command=calculator_bmi)
calculator_button.configure(background="light pink")
calculator_button.pack()

result_label = tkinter.Label()
result_label.pack()


def write_result(bmi):
    result_string = f"your BMI is: {bmi}. you are"
    if bmi <= 16:
        result_string += "severely thin"
    elif bmi > 16 and bmi <=17:
        result_string += "moderately thin"
    elif bmi > 17 and bmi <=18:
        result_string += "mild thin"
    elif bmi > 18.5 and bmi <=25:
        result_string += "normal"
    elif bmi > 25 and bmi <=30:
        result_string += "overweight"
    elif bmi > 30 and bmi <=35:
        result_string += "obese classs 1"
    elif bmi > 35 and bmi <=40:
        result_string += "obese classs 2"
    else:
        result_string += "obese classs 3"
    return result_string




window.mainloop()