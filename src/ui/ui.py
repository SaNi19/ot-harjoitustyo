from tkinter import Tk
from ui.login_view import LoginView
from ui.storage_view import StorageView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_storage(self):
        self._show_storage_view()

    def _handle_login(self):
        self._show_login_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_storage
        )

        self._current_view.pack()

    def _show_storage_view(self):
        self._hide_current_view()

        self._current_view = StorageView(
            self._root,
            self._handle_login
        )

        self._current_view.pack()

