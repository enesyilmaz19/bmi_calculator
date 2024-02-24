from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=10, pady=10)


def bmi_calculating():
    height = height_entry.get()
    weight = weight_entry.get()
    if weight == "" or height == "":
        bmi_label.config(text="Enter valid numbers please")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            bmi_string = write_bmi(bmi)
            bmi_label.config(text=bmi_string)
        except:
            bmi_label.config(text="Enter valid numbers please")


weight_label = Label(text="Enter your weight (kg)")
weight_label.pack()
weight_entry = Entry(width=15)
weight_entry.pack()
height_label = Label(text="Enter your height (cm)")
height_label.pack()
height_entry = Entry(width=15)
height_entry.pack()
calculate_button = Button(text="calculate", command=bmi_calculating)
calculate_button.pack()
bmi_label = Label()
bmi_label.pack()


def write_bmi(bmi):
    bmi_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi < 18.5:
        bmi_string += "underweight"
    elif 18.5 <= bmi < 25.0:
        bmi_string += "normal weight"
    elif 25.0 <= bmi < 40.0:
        bmi_string += "overweight"
    else:
        bmi_string += "obese"
    return bmi_string


window.mainloop()