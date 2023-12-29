import sqlite3

import SDks


class User():
    def __init__(self, name, amount):
        print('account created')
        self.name = name
        self.amount = amount

    def __repr__(self):
        return  self.__str__()

    def __str__(self):
        return   (f"{self.name} has {self.amount} Naira")


def cursor():
    return sqlite3.connect(':memory:').cursor()


c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS user (name TEXT, amount INTEGER)')
c.connection.close()


def add_user(user):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO user VALUES (?, ?)', (user.name, user.amount))
    return c.lastrowid
    c.connection.close()


print('Note: This will only show once 😀')
print("What is the name of your account? 😏")
name = print(input())
print('How much do u want to credit your account with?🤑')
amount = print(input())

users = User(name, amount)
add_user(users)
def print_menu():
    print('welcome to MTN data services')
    print('''
             1.Data plans
             2.Get 700MB + 3
             voice mins for N500
             3.Social Bundles
             4.Chat with Zigi
             5. Get 1.5GB for
             N300
             ''')
print_menu()
while True:
    response = int(input())
    if response == 1:
            SDks.data_plans(1)
            data_res = int(input())
            SDks.data_plans_1(data_res)
    if response == 2:
        SDks.data_view(500, '700MB', '700MB + 3 voice mins')
    if response == 3:
        SDks.socials()
    if response == 5:
        print('''
        Y'ello! Need Help?
        Chat with Zigi on
        your preferred
        channels:
        WhatsApp,
        Facebook 
        Messeger, Web 
        and Telegram.
        Details via SMS.
        ''')
    if response == 6:
        SDks.data_view(300, '1.5GB', 'Weekly Bundle 4Me')
    break



