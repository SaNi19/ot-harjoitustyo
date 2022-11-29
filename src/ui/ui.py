from tkinter import Tk, constants, ttk


class UI:
    def __init__(self, root):
        self._root = root
        self._entry = None

    def start(self):

        login_heading_label = ttk.Label(master=self._root, text="Login")

        login_username_label = ttk.Label(master=self._root, text="Username")
        login_username_entry = ttk.Entry(master=self._root)

        login_password_label = ttk.Label(master=self._root, text="Password")
        login_password_entry = ttk.Entry(master=self._root)

        login_button = ttk.Button(
            master=self._root, text="Login", command=self.__handle_button_click)

        create_heading_label = ttk.Label(
            master=self._root, text="Create a new account")

        create_username_label = ttk.Label(master=self._root, text="Username")
        create_username_entry = ttk.Entry(master=self._root)

        create_password1_label = ttk.Label(master=self._root, text="Password")
        create_password1_entry = ttk.Entry(master=self._root)

        create_password2_label = ttk.Label(
            master=self._root, text="Confirm password")
        create_password2_entry = ttk.Entry(master=self._root)

        create_button = ttk.Button(master=self._root, text="Registration")

        login_heading_label.grid(row=0, column=1, columnspan=2, sticky=(
            constants.E, constants.W), padx=7, pady=7)

        login_username_label.grid(
            row=1, column=0, sticky=constants.W, padx=5, pady=5)
        login_username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        login_password_label.grid(
            row=2, column=0, sticky=constants.W, padx=5, pady=5)
        login_password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        login_button.grid(row=3, column=1, columnspan=2,
                          sticky=constants.W, padx=5, pady=5)

        create_heading_label.grid(row=4, column=1, columnspan=2, sticky=(
            constants.E, constants.W), padx=7, pady=7)

        create_username_label.grid(
            row=5, column=0, sticky=constants.W, padx=5, pady=5)
        create_username_entry.grid(row=5, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_password1_label.grid(
            row=6, column=0, sticky=constants.W, padx=5, pady=5)
        create_password1_entry.grid(row=6, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_password2_label.grid(
            row=7, column=0, sticky=constants.W, padx=5, pady=5)
        create_password2_entry.grid(row=7, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_button.grid(row=8, column=1, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        self._root.grid_columnconfigure(1, weight=1)

    def __handle_button_click(self):
        entry_value = self._entry.get()
        print(f"Value of entry is: {entry_value}")


window = Tk()
window.title("Wood storage")

ui = UI(window)
ui.start()

window.mainloop()
