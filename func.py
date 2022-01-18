
class DataBase:

    def __init__(self):
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


    @staticmethod
    def _MenuAdd(args):
        print("+-----------------------------------------------------------------------------------+")
        print("|                       [1] -> Cart                                                 |")
        print("|                       [2] -> list of ads                                          |")
        print("|                       [3] -> Register ad                                          |")
        print("|                       [4] -> Exit the program                                     |")
        print("+-----------------------------------------------------------------------------------+")
        while True:
            try:
                choice = input("What is the option? -> ")
                if int(choice) > 0 and int(choice) < 5:
                    value = "a"+choice

                    return Menu.options[value](args)
                    break
                else:
                    print("The value entered is not valid")

            except Exception as e:
                print(e)


    @staticmethod
    def _GertCart(args):
        for k in args[0].getOrder():
            if args[1] == k[1]:
                for a in args[0].getAdd():
                    if k[2] == a[0]:
                       print(*a)


    @staticmethod
    def _ListAdd(args):
        i = 1
        arrayAdd = []

        for k in args[0].getAdd():
            if k[5] == 0:
                arrayAdd.append(k)

        for line in arrayAdd:
            print(*line)

        if len(arrayAdd) > 0:
            while True:
                try:
                    choice = input("\n Write EXIT to exit.\n To choose the add just type the first int of the line\n What is the add to by? -> ")
                    if choice.lower() != "exit":
                        valid = False
                        for add in arrayAdd:
                            if int(choice) == int(add[0]):

                                args[0].insertOrder([len(args[0].getOrder()) + 1, args[1], int(choice)])
                                add[5] = 1
                                args[0].ChangeAdd(add)
                                print("Successfully purchased")
                                valid = True
                        if valid == False:
                            print("The value entered is not valid")
                        else:
                            break
                    else:
                        break
                except Exception as e:
                    raise Exception(e)
        else:
            print("There is no add")

    @staticmethod
    def _RegisterAdd(args):
        print("Add Register")
        nome = input('Enter your name ad:')
        des = input('Enter your description ad:')
        price = input('Enter your ad price:')
        args[0].insertAdd([len(args[0].getAdd()) + 1, args[1], nome, des, price, 0 ])

        print("Successfully registered.", )