import func

db = func.DataBase()
db.insertUser([1, 'admin', 'admin'])
db.insertUser([2, 'user', 'user'])

db.insertAdd([1, 2, "1 Lorem ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 15.0, 1])
db.insertAdd([2, 2, "2 Lorem ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 15.0, 1])
db.insertAdd([3, 1, "3 Lorem ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 15.0, 1])
db.insertAdd([4, 1, "4 Lorem ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 15.0, 0])
db.insertAdd([5, 2, "5 Lorem ipsum", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 15.0, 1])

db.insertOrder([1, 1, 1])
db.insertOrder([2, 1, 2])
db.insertOrder([3, 2, 3])

Login = [False, 0]
while True:
    if Login[0] == False:
        res = func.Menu._LoginMenu(db)
        if type(res) == list:
            Login = res
    else:
        func.Menu._MenuAdd([db, Login[1]])