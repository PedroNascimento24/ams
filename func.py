class DataBase:

    def init(self):
        self.user = []
        self.add = []
        self.order = []

    def insertUser(self, data):
        # UserID | Username | Password
        self.user.append(data)

    def insertAdd(self, data):
        # addID | userID  | Nome | desc | preco | status
        self.add.append(data)

    def ChangeAdd(self, data):
        i = 0
        for value in self.add:
            if value[0] == data[0]:
                self.add[i] = data
            i += 1

    def insertOrder(self, data):
        # OrderID | UserID | addid
        self.order.append(data)

    def getAdd(self):
        return self.add.copy()

    def getuser(self):
        return self.user.copy()

    def getOrder(self):
        return self.order.copy()

class Menu:
    options = {
        "1": lambda args: Menu._login(args),
        "2": lambda args: Menu._UserRegister(args),
        "3": lambda args: exit("See you later"),
        "a1": lambda args: Menu._GertCart(args),
        "a2": lambda args: Menu._ListAdd(args),
        "a3": lambda args: Menu._RegisterAdd(args),
        "a4": lambda args: exit("See you later"),
    }

    @staticmethod
    def _login(db):
        print("User Login")
        nome = input('Enter your name:')
        password = input('Enter your password:')

        for k in db.getuser():
            if nome in k:
                if password in k:
                    print("Successfully logged in.")
                    return [True, k[0]]

        print("Unsuccessfully logged in.")

    @staticmethod
    def _UserRegister(db):
        print("User Register")
        nome = input('Enter your name:')
        password = input('Enter your password:')

        for k in db.getuser():
            if nome in k:
                Menu._UserRegister()

        db.insertUser([len(db.getuser()) + 1, nome, password])
        print("Successfully registered.", )

    @staticmethod
    def _LoginMenu(db):
        print("+-----------------------------------------------------------------------------------+")
        print("|                       [1] -> Login                                                |")
        print("|                       [2] -> Register                                             |")
        print("|                       [3] -> Exit the program                                     |")
        print("+-----------------------------------------------------------------------------------+")
        while True:
            try:
                choice = input("What is the option? -> ")
                if int(choice) > 0 and int(choice) < 4:
                    return Menu.options[choice](db)
                else:
                    print("The value entered is not valid")

            except Exception as e:
                raise Exception(e)
