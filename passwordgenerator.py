import random
import string
import PySimpleGUI as sg
import tkinter as tk

# Create a Tkinter window for hover effect
hover_root = tk.Tk()
hover_root.withdraw()  # Hide the Tkinter window

sg.theme('Dark Amber 5')
sg.set_options(font='verdana 15')

layout = [
    [sg.Text('Password Length:')],
    [sg.InputText(default_text='Enter Password Length', size=(20, 1), key='-LENGTH-', justification='center')],
    [sg.Button('Generate', key='-GENERATE-'), sg.Button('Exit', key='-EXIT-')],
    [sg.Text('Password'), sg.Multiline(size=(15, 3), no_scrollbar=True, disabled=True, key='-PASS-')],
]

window = sg.Window('Password Generator', layout)

# Change the cursor for the entire window
window.finalize()
window.TKroot.config(cursor='hand2')

def on_button_hover(event):
    # Change button color or style when hovering
    if event.widget == window['-GENERATE-'].Widget:
        window['-GENERATE-'].update(button_color=('white', 'black'))
    elif event.widget == window['-EXIT-'].Widget:
        window['-EXIT-'].update(button_color=('white', 'red'))

def on_button_leave(event):
    # Restore button color or style when not hovering
    if event.widget == window['-GENERATE-'].Widget:
        window['-GENERATE-'].update(button_color=('black', 'white'))
    elif event.widget == window['-EXIT-'].Widget:
        window['-EXIT-'].update(button_color=('blue', 'white'))

# Bind hover events to the "Generate" and "Exit" buttons
window['-GENERATE-'].Widget.bind("<Enter>", on_button_hover)
window['-GENERATE-'].Widget.bind("<Leave>", on_button_leave)
window['-EXIT-'].Widget.bind("<Enter>", on_button_hover)
window['-EXIT-'].Widget.bind("<Leave>", on_button_leave)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-EXIT-':
        break

    if event == '-GENERATE-':
        try:
            length = int(values['-LENGTH-'])  # Get the desired password length
            # Define character sets
            uppercase_chars = string.ascii_uppercase
            lowercase_chars = string.ascii_lowercase
            digit_chars = string.digits
            symbol_chars = string.punctuation
            # Create the combined character set
            all_chars = uppercase_chars + lowercase_chars + digit_chars + symbol_chars
            # Generate the password
            password = ''.join(random.choice(all_chars) for _ in range(length))
            window['-PASS-'].update(password)
        except ValueError:
            window['-PASS-'].update("No valid number")

window.close()






