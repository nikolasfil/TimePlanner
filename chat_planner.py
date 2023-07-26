import PySimpleGUI as sg


class ExcelSheetApp:
    def __init__(self):
        self.num_rows = 12
        self.num_cols = 7
        self.layout = [
            [sg.Button("Clear", key='-CLEAR-'), sg.Text('Navigation'),
             sg.Button("Check", key='-CHECK-')],
        ]
        self.create_input_fields()

    def create_input_fields(self):
        for row in range(self.num_rows):
            row_layout = []
            for col in range(self.num_cols):
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
            for col in range(self.num_cols):
                self.window[(row, col)].update('')

    def check_and_color_inputs(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                value = self.window[(row, col)].get()
                if value == '1':
                    self.window[(row, col)].update(background_color='blue')
                else:
                    self.window[(row, col)].update(background_color='white')


if __name__ == "__main__":
    app = ExcelSheetApp()
    app.run()
