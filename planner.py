import PySimpleGUI as pg


class Planner:
    def __init__(self) -> None:
        self.matrix = [[None for j in range(12)] for i in range(7)]

    def __str__(self) -> str:
        # for day in self.matrix:
        #     for hour, value in enumerate(day):
        #         print(f"{9+(hour)}:00-{9+(hour+1)}:00", end=' ')
        #         #     pass
        #     print("-----")

        for hour, value in enumerate(self.matrix[0]):
            print(f"{9+(hour)}:00-{9+(hour+1)}:00")

    def main(self):
        layout = [[pg.Text(f"Column {i}")] for i in range(1, 8)]
        margins = (12*50, 7*50)

        window = pg.Window(title="Planner", layout=layout, margins=margins)

        while True:
            event, values = window.read()
            if event == pg.WIN_CLOSED:
                break


if __name__ == "__main__":
    planner = Planner()
    planner.main()
