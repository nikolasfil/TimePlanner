import PySimpleGUI as sg

# Define the layout for the window
layout = [
    [sg.Button("Previous", key='-PREV-'), sg.Text('Navigation'),
     sg.Button("Next", key='-NEXT-')],
]

# Add 12 input fields and arrange them in 7 columns
num_rows = 12
num_cols = 7
for row in range(num_rows):
    row_layout = []
    for col in range(num_cols):
        row_layout.append(sg.Input(size=(10, 1), key=(row, col)))
    layout.append(row_layout)

# Create the window
window = sg.Window("Excel Sheet", layout, finalize=True)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == '-PREV-':
        # Handle the previous button click
        # You can implement the logic for navigation here
        pass
    elif event == '-NEXT-':
        # Handle the next button click
        # You can implement the logic for navigation here
        pass

window.close()
