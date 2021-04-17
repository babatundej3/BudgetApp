database = {food}


class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    def deposit(amount, bal):
        bal += amount
        return bal

    def withdraw(user, amount, bal):
        bal -= amount
        return bal
    
    def balance(db):
        for categ, bal in db.items():
            print(categ, bal)

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(value2) + amount
        return db

    def init():
        print('=== ***BTJ Budget App*** ===\n')
        menu()

    def menu():
        try:

            user = int(input('\n=== ***What would you like to do?*** ===\nPress (1) To create Budget\nPress (2) To deposit\nPress (3) To Withdraw'))
        except:
            print('invalid input')
            menu()

        if (user == 1):
            Create_Budget()
        elif (user == 2):
            credit()
        elif (user == 3):
            debit()
        elif (user == 4):
            balance()
        elif (user == 5):
            transfer()
        elif (user == 6):
            sign_out()
        else:
            print('invalid input\n')
            menu()
    