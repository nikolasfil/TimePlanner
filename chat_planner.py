import PySimpleGUI as sg


class ExcelSheetApp:
    def __init__(self):
        self.num_rows = 12
        self.num_cols = 7
        self.layout = [
            [sg.Button("Clear", key='-CLEAR-'),
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
                # Handle the previous button click
                # You can implement the logic for navigation here
                pass
            elif event == '-CHECK-':
                # Handle the next button click
                # You can implement the logic for navigation here
                print('Check')
            else:
                self.check_and_color_input(event)

        self.window.close()

    def check_and_color_input(self, event):
        try:
            row, col = event
            value = self.window[event].get()
            if value == '1':
                self.window[event].update(background_color='blue')
            else:
                self.window[event].update(background_color='white')
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    app = ExcelSheetApp()
    app.run()
