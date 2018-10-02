def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("starting decorator...")
        result = func(*args, **kwargs)
        print("finishing decorator...")
        result.append("mydecorator")
        return result
    return wrapper

@mydecorator
def mydecorated_function(arg):
    return [arg]

if __name__ == "__main__":
    print(mydecorated_function("hello decorated function!"))
