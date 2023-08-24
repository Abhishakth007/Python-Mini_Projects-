from tkinter import *
import random
import pandas as pd


def flip_card():
    global text_1
    final_data = data_finder()
    for i in final_data:
        canvas.itemconfig(text_1_item, text="English")
        canvas.itemconfig(text_2_item, text=final_data[1])


def wrong_data_updater():
    global text_2
    final_data = data_finder()
    for i in final_data:
        canvas.itemconfig(text_1_item, text="French")
        canvas.itemconfig(text_2_item, text=final_data[0])
        timer = screen.after(3000, func=flip_card)


def data_updater():
    global text_2
    global random_number
    final_data = data_finder()
    for i in final_data:
        canvas.itemconfig(text_1_item, text="French")
        canvas.itemconfig(text_2_item, text=final_data[0])
        timer = screen.after(3000, func=flip_card)
        data_to_be_written_as_list = []
        data_to_be_written = {"French": final_data[0], "English": final_data[1]}
        data_to_be_written_as_list.append(data_to_be_written)
        df = pd.DataFrame(data_to_be_written_as_list)
        df.to_csv("known_data.txt", mode='a', index=False)
        return delete_row(final_data[0])


def delete_row(row_to_delete):
    df = pd.read_csv("C:/Users/Abhi/PycharmProjects/Flash_Card_Capestone/data/french_words.csv")
    df = df[df["French"] != row_to_delete]
    df.to_csv("C:/Users/Abhi/PycharmProjects/Flash_Card_Capestone/data/french_words.csv", index=False)
def data_finder():
    data_list = []
    global timer
    df = pd.read_csv("C:/Users/Abhi/PycharmProjects/Flash_Card_Capestone/data/french_words.csv")
    random_number = random.randint(0, len(df))
    random_french_row = df.iloc[random_number]
    random_french_word = random_french_row["French"]
    data_list.append(random_french_word)
    random_english_word = random_french_row["English"]
    data_list.append(random_english_word)
    return data_list


screen = Tk()
screen.title("Flash_Card")
screen.minsize(width=800, height=600)
screen.config(bg="#b4b8f6")
timer = screen.after(3000, func=flip_card)

wrong_image = PhotoImage(file="C:/Users/Abhi/OneDrive/Desktop/Pictures/cross_mark.png")
right_image = PhotoImage(file="C:/Users/Abhi/OneDrive/Desktop/Pictures/right_mark.png")

wrong_image_button = Button(screen, image=wrong_image, command=wrong_data_updater)
wrong_image_button.place(x=180, y=530)
right_image_button = Button(screen, image=right_image, command=data_updater)
right_image_button.place(x=550, y=530)
text_1 = "French"

canvas = Canvas(width=600, height=530)
canvas.config(bg="#a5edc6", highlightthickness=1)
text_1_item = canvas.create_text(300, 100, text=text_1, font=("Ariel", 30, "italic"))
text_2 = data_finder()
text_2_item = canvas.create_text(300, 200, text=text_2, font=("Agerian", 30, "bold"))
canvas.pack()

screen.mainloop()
