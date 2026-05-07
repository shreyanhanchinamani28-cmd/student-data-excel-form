from tkinter import *
import pandas as pd
import os

myw = Tk()
myw.geometry('500x500+500+200')
myw.title('Student Data Form')
myw.configure(bg='pink')

def save_to_excel():
    usn = tf_usn.get()
    sem = tf_sem.get()
    branch = tf_branch.get()
    college = tf_college.get()
    username = tf_user.get()
    password = tf_pass.get()

    if usn=="" or sem=="" or branch=="" or college=="" or username=="" or password=="":
        print("Please fill all fields")
        return

    new_data = pd.DataFrame({
        'USN': [usn],
        'Semester': [sem],
        'Branch': [branch],
        'College': [college],
        'Username': [username],
        'Password': [password]
    })

    file_name = "students.xlsx"

    try:
        if os.path.exists(file_name):
            old_data = pd.read_excel(file_name)
            final_data = pd.concat([old_data, new_data], ignore_index=True)
        else:
            final_data = new_data

        final_data.to_excel(file_name, index=False)

        print("Data saved successfully")

        # clear fields
        tf_usn.delete(0, END)
        tf_sem.delete(0, END)
        tf_branch.delete(0, END)
        tf_college.delete(0, END)
        tf_user.delete(0, END)
        tf_pass.delete(0, END)

        os.startfile(file_name)

    except PermissionError:
        print("❌ Close Excel file and try again")

# UI Labels & Entries

Label(myw, text='USN', fg='red').place(x=10, y=20)
tf_usn = Entry(myw)
tf_usn.place(x=150, y=20)

Label(myw, text='Semester', fg='red').place(x=10, y=60)
tf_sem = Entry(myw)
tf_sem.place(x=150, y=60)

Label(myw, text='Branch', fg='red').place(x=10, y=100)
tf_branch = Entry(myw)
tf_branch.place(x=150, y=100)

Label(myw, text='College', fg='red').place(x=10, y=140)
tf_college = Entry(myw)
tf_college.place(x=150, y=140)

Label(myw, text='Username', fg='red').place(x=10, y=180)
tf_user = Entry(myw)
tf_user.place(x=150, y=180)

Label(myw, text='Password', fg='red').place(x=10, y=220)
tf_pass = Entry(myw, show='*')
tf_pass.place(x=150, y=220)

Button(myw, text='SAVE TO EXCEL', fg='red', bg='beige', command=save_to_excel).place(x=120, y=270)

myw.mainloop()