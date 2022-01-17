class DataBase:

    def init(self):
        self.user = []
        self.add = []
        self.order = []

    def insertUser(self, data):
        # UserID | Usernme | Password
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