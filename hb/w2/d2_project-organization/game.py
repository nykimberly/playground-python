"""Module containing one function for user.py"""

def greet_user() :
    user = input('Who are you? ')
    print("Hello, {}".format(user))

# if we run this program, then call greet_user();
# otherwise, don't call greet_user if we are just importing
if __name__ == '__main__':
    greet_user()
