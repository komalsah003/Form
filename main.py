from tkinter import *
root = Tk()
root.geometry("500x500")

def getvals():
    print("Successfully submitted")

Label(root, text="Webdev registration form", font="ar 18 bold").grid(row=0, column=3)

Name = Label(root, text="Name")
Email = Label(root, text="Email")
Phone = Label(root, text="Phone")
Gender = Label(root, text="Gender")
paymentmood = Label(root, text="Payment Mood")

Name.grid(row=1, column=2)
Email.grid(row=2, column=2)
Phone.grid(row=3, column=2)
Gender.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

Namevalue = StringVar
Emailvalue = StringVar
Phonevalue = StringVar
Gendervalue = StringVar
paymentMoodvalue = StringVar
checkvalue = IntVar

Nameentry = Entry(root, textvariable=Namevalue)
Emailentry = Entry(root, textvariable=Emailvalue)
Phoneentry = Entry(root, textvariable=Phonevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
paymentmoodentry = Entry(root, textvariable=paymentmood)

Nameentry.grid(row=1, column=3)
Emailentry.grid(row=2, column=3)
Phoneentry.grid(row=3, column=3)
Genderentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

checkbtn=Checkbutton(text="I agree with the rules", variable=checkvalue)
checkbtn.grid(row=6, column=3)

Button(text="Submit", font="18", command=getvals).grid(row=7, column=3)
root.mainloop()