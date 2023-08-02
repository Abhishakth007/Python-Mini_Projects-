import random
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', '|', '\\',
                 ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']


def password_generator():
    password_chars_list = []
    for i in range(3):
        small = random.choice(small_letters)
        password_chars_list.append(small)
        capital = random.choice(capital_letters)
        password_chars_list.append(capital)
        nums = str(random.choice(numbers))
        password_chars_list.append(nums)
        special = random.choice(special_chars)
        password_chars_list.append(special)
        random.shuffle(password_chars_list)
        final_password = ''.join(password_chars_list)
    generated_password.delete(0, END)
    generated_password.insert(0, "".join(password_chars_list))
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(password_chars_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_text_to_file():
    global website_entry
    global email_entry
    global password_entry
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=web, message=f"Email : {email} \nPassword : {password}\n Is is ok to save "
                                                      f"the details..?")
    if is_ok:
        with open("data.txt", 'a') as file:
            file.writelines(f"{website_entry.get()}   |   {email_entry.get()}   |   {password_entry.get()}\n")
            print("Text data successfully saved to", "data.txt")


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.minsize(width=620, height=520)
canvas = Canvas(width=500, height=500)

pic = PhotoImage(file="logo.png")
canvas.create_image(240, 180, image=pic)

window.config(pady=20, padx=20)

canvas.create_text(50, 300, text="Website:", font=("Arial", 11, "bold"), fill="black")
canvas.create_text(50, 340, text="Email_Id:", font=("Arial", 11, "bold"), fill="black")
canvas.create_text(50, 380, text="Password:", font=("Arial", 11, "bold"), fill="black")
canvas.create_text(220, 410, text="Generated_Password:", font=("Arial", 11, "bold"), fill="black")

website_entry = Entry(width=30)
website_entry.focus()
website_entry.place(x=130, y=290)

email_entry = Entry(width=30)
common_email = "abhishakth007@gmail.com"
email_entry.insert(INSERT, common_email)
email_entry.place(x=130, y=330)

password_entry = Entry(width=30)
password_entry.place(x=130, y=370)

password_save_button = Button(width=5, text="save", font=("Arial", 10, "bold"))
password_save_button.config(command=save_text_to_file)
password_save_button.place(x=250, y=450)

generate_password_button = Button(width=10, text="generate", font=("Arial", 10, "bold"))
generate_password_button.config(command=password_generator)
generate_password_button.place(x=350, y=365)

generated_password = Entry(width=30)
generated_password.place(x=349, y=400)

canvas.pack()

window.mainloop()
