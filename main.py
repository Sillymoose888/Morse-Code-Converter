from morse_dict import Morse
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from pydub import AudioSegment

# ------------------------------- CONSTANTS ------------------------------- #
SAGE = '#A4B494'
ASH_GRAY = '#BEC5AD'
FELDGRAU = '#3B5249'
SEA_GREEN = '#519872'
RAISIN_BLACK = '#34252F'
FONT_NAME = 'Ariel'
DOT = AudioSegment.from_wav('morse-audio/dot.wav')
DASH = AudioSegment.from_wav('morse-audio/dash.wav')
SILENT = AudioSegment.from_wav('morse-audio/silent_long.wav')


# ------------------------------- CONVERT FUNCTION ------------------------------- #
def convert_message():
    global morse_text
    message = Morse(input_box.get('1.0', 'end'))
    morse_string = message.to_morse()
    morse_text.config(text=f"{morse_string}")

    morse_audio = SILENT
    for char in morse_string:
        if char == '.':
            morse_audio = morse_audio + DOT
        elif char == '-':
            morse_audio = morse_audio + DASH
        elif char == '/':
            morse_audio = morse_audio + SILENT + SILENT + SILENT + SILENT + SILENT + SILENT + SILENT
        else:
            morse_audio = morse_audio + SILENT + SILENT + SILENT

    remove_char = [",", "\n", ":", "?", "!", ".", ";", "+", "-", "/", "="]
    filename = message.message[:25].replace(" ", "_")
    for char in remove_char:
        if char in filename:
            filename = filename.replace(char, '')
    morse_audio.export(f"audio-messages/{filename}.wav", format='wav')

    morse_audio.export(f"audio-messages/{filename}.wav", format='wav')


# ------------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Morse Code Converter")
window.config(padx=25, pady=25, bg=SAGE)

title_label = Label(text="MORSE CODE CONVERTER", font=(FONT_NAME, 20, 'bold'), bg=SAGE, fg=FELDGRAU)
title_label.grid(column=0, row=0, columnspan=2)

input_box = Text(bg=ASH_GRAY, font=(FONT_NAME), height=10, width=50, highlightthickness=0)
input_box.grid(column=0, row=1, columnspan=2)

convert_button = Button(text='CONVERT', command=convert_message)
convert_button.grid(column=0, row=3, columnspan=2)

morse_text = Label(height=10, width=50, text="", fg=RAISIN_BLACK, bg=SAGE, font=(FONT_NAME, 15, 'bold'), wraplength=500, justify='center')
morse_text.grid(column=0, row=2, columnspan=2)

# # App main loop
# app_active = True
# while app_active:
#     message = Message(input("message: "))
#     print(message.to_morse())

window.mainloop()

# TODO - create message to text conversion
# TODO - Create interface
# TODO - interface text interface
# TODO - Create message to audio conversion
# TODO - store audio file for later retrieval
