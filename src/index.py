from tkinter import Tk
from ui.ui_view import UI


def main():
    window = Tk()
    window.title("Wood storage")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
