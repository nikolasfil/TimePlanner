import PySimpleGUI as sg


class ExcelSheetApp:
    def __init__(self):
        self.num_rows = 12
        self.num_cols = 8
        # Size of the input fields and days of the week
        self.field_size = (15, 1)
        self.layout = [
            [sg.Button("Clear Color", key='-CLEAR-COLOR-'), sg.Button("Clear All",
                                                                      key='-CLEAR-ALL-'), sg.Text('Navigation'), sg.Button("Check", key='-CHECK-')],
        ]
        self.create_input_fields()

    def create_input_fields(self):
        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        time_slots = ['09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00',
                      '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00', '20:00-21:00']

        # Add days of the week to the first row
        header_row = [sg.Text('', size=self.field_size)]
        header_row.extend([sg.Text(day, size=self.field_size,
                          justification='center') for day in days_of_week])
        self.layout.append(header_row)

        for row in range(self.num_rows):
            row_layout = []
            # Add time slots to the first column
            row_layout.append(
                sg.Text(time_slots[row], size=self.field_size, justification='center'))

            for col in range(1, self.num_cols):
                row_layout.append(
                    sg.Input(size=self.field_size, key=(row, col), enable_events=True))
            self.layout.append(row_layout)

    def run(self):
        self.window = sg.Window("Excel Sheet", self.layout, finalize=True)
        self.window.bind('<q>', '+Q')  # Bind the 'q' key to the close event
        self.window.bind('<c>', '-CHECK-')
        self.window.bind('<C>', '-CLEAR-ALL-')
        self.window.bind('<l>', '-CLEAR-COLOR-')

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == '+Q':
                break
            elif event == '-CLEAR-COLOR-':
                self.clear_cell_colors()
            elif event == '-CLEAR-ALL-':
                self.clear_all()

            elif event == '-CHECK-':
                self.check_and_color_inputs()

        self.window.close()

    def clear_cell_colors(self):
        for row in range(self.num_rows):  # Exclude the header row
            for col in range(1, self.num_cols):
                self.window[(row, col)].update(background_color='white')

    def clear_all(self):
        for row in range(self.num_rows):
            for col in range(1, self.num_cols):
                self.window[(row, col)].update('')
                self.window[(row, col)].update(background_color='white')

    def check_and_color_inputs(self):
        self.check_population()
        for row in range(self.num_rows):  # Exclude the header row
            for col in range(1, self.num_cols):
                value = self.window[(row, col)].get()
                if value == '1':
                    self.window[(row, col)].update(background_color='blue')
                else:
                    self.window[(row, col)].update(background_color='white')

    def check_population(self):
        dic = {}
        for row in range(self.num_rows):
            for col in range(1, self.num_cols):
                value = self.window[(row, col)].get()
                if len(value) not in dic.keys():
                    dic[len(value)] = 0
                dic[len(value)] += 1
        print(dic)


if __name__ == "__main__":
    app = ExcelSheetApp()
    app.run()
