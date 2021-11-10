class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def __str__(self):
        return self._name

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def do_something(self):
        print("Hi from " + str(self))

users = [ User("Testuser", "testmail@mail.com"), User("User2", "user2@mail.com") ]

for user1 in users:
    for user2 in users:
        user1.do_something()
        user2.do_something()
