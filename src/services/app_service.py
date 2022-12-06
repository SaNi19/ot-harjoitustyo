from entities.user import User
from repositories import user_repository
from ui.login_view import LoginView



class AppService:
    def __init__(self):
        self.__list = LoginView()
        self.__file = user_repository("data.txt")

        for username, usernames in self.__file.load().items():
            for username in list:
                self.__list.create_user(username) 
       
    def add(self):
        username = "abc"
        password = "123"
        self.__list._create_user(username)

    def get_user(self):
        username = "abc"
        if not username in self.__list:
            return None

        
  

app_service = AppService()
