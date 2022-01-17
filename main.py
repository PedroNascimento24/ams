import func

db = func.DataBase()
db.insertUser([1, 'admin', 'admin'])
db.insertUser([2, 'user', 'user'])
func.Menu._LoginMenu(db)