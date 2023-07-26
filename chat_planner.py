import PySimpleGUI as sg


class ExcelSheetApp:
    def __init__(self):
        self.num_rows = 12
        self.num_cols = 8
        self.layout = [
            [sg.Button("Clear", key='-CLEAR-'), sg.Text('Navigation'),
             sg.Button("Check", key='-CHECK-')],
        ]
        self.create_input_fields()

    def create_input_fields(self):
        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        time_slots = ['09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00',
                      '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00', '20:00-21:00']

        # Add days of the week to the first row
        header_row = [sg.Text('', size=(10, 1))]
        header_row.extend(
            [sg.Text(day, size=(10, 1), justification='center') for day in days_of_week])
        self.layout.append(header_row)

        for row in range(self.num_rows):
            row_layout = []
            # Add time slots to the first column
            row_layout.append(
                sg.Text(time_slots[row], size=(10, 1), justification='center'))

            for col in range(1, self.num_cols):
                row_layout.append(
                    sg.Input(size=(10, 1), key=(row, col), enable_events=True))
            self.layout.append(row_layout)

    def run(self):
        self.window = sg.Window("Excel Sheet", self.layout, finalize=True)
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == '-CLEAR-':
                self.clear_input_fields()
            elif event == '-CHECK-':
                self.check_and_color_inputs()

        self.window.close()

    def clear_input_fields(self):
        for row in range(self.num_rows):
            for col in range(1, self.num_cols):
                self.window[(row, col)].update('')
                self.window[(row, col)].update(background_color='white')

    def check_and_color_inputs(self):
        for row in range(1, self.num_rows):  # Exclude the header row
            for col in range(1, self.num_cols):
                value = self.window[(row, col)].get()
                if value == '1':
                    self.window[(row, col)].update(background_color='blue')
                else:
                    self.window[(row, col)].update(background_color='white')


if __name__ == "__main__":
    app = ExcelSheetApp()
    app.run()
