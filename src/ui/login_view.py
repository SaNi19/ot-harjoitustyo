from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_storage):
        self.__users = {}
        self._root = root
        self._handle_storage = handle_storage
        self._frame = None
        self._login_username_entry = None
        self._login_password_entry = None


        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)
        login_heading_label = ttk.Label(master=self._frame, text="Login")

        login_username_label = ttk.Label(master=self._frame, text="Username")
        login_username_entry = ttk.Entry(master=self._frame)

        login_password_label = ttk.Label(master=self._frame, text="Password")
        login_password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_storage)

        create_heading_label = ttk.Label(
            master=self._frame, text="Create a new account")

        create_username_label = ttk.Label(master=self._frame, text="Username")
        create_username_entry = ttk.Entry(master=self._frame)

        create_password1_label = ttk.Label(master=self._frame, text="Password")
        create_password1_entry = ttk.Entry(master=self._frame)

        create_password2_label = ttk.Label(
            master=self._frame, text="Confirm password")
        
        create_password2_entry = ttk.Entry(master=self._frame)

        create_button = ttk.Button(master=self._frame, text="Registration", command=self._handle_storage)

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

    def _login_handle(self):
       username = self._login_username_entry
    
       if not username in self.__users:
            return None
    

    def _create_user(self, username: str, password: str):
        if not username in self.__users:
            self.__users[username] = []

        self.__users[username].append(password)

       
