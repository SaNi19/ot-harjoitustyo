from tkinter import ttk, constants

class StorageView:
    def __init__(self, root, handle_hello):
        self._root = root
        self._handle_hello = handle_hello
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)

        add_heading_label = ttk.Label(master=self._frame, text="Add firewood to the storage")
        
        add_label = ttk.Label(master=self._frame, text="Add")
        add_entry = ttk.Entry(master=self._frame)

        add_button = ttk.Button(
            master=self._frame, text="Add", command=self._handle_hello
        )
        
        take_headin_label = ttk.Label(master=self._frame, text="Sells firewood from storage")
        
        take_label = ttk.Label(master=self._frame, text="Take")
        take_entry = ttk.Entry(master=self._frame)

        take_button = ttk.Button(
            master=self._frame, text="Take", command=self._handle_hello
        )
        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_hello
        )
        add_heading_label.grid(row=0, column=1, columnspan=10, sticky=(
            constants.E, constants.W), padx=7, pady=7)

        add_label.grid(
            row=1, column=0, sticky=constants.W, padx=5, pady=5)
        
        add_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)


        add_button.grid(row=3, column=1, columnspan=2,
                          sticky=constants.W, padx=5, pady=5)

        take_headin_label.grid(row=4, column=1, columnspan=10, sticky=(
            constants.E, constants.W), padx=7, pady=7)

        take_label.grid(row=5, column=0, sticky=constants.W, padx=5, pady=5)

        take_entry.grid(row=5, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        take_button.grid(row=6, column=1, columnspan=2, sticky=constants.W, padx=5, pady=5)

        logout_button.grid(row=7, column=1, columnspan=2, sticky=constants.W, padx=5, pady=5)

        '''button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_hello
        )'''

        #add_label.grid(row=0, column=0)
        #button.grid(row=1, column=0)