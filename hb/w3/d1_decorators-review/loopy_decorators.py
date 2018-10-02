def loopy_decorator_with_args(arg):
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            print("starting _wrapper...")
            result = []
            for i in range(arg):
                print(f"Loop {i}")
                print(f"result={func(*args, **kwargs)}")
                result.extend(func(*args, **kwargs))
            result.append("_wrapper")
            print("finishing _wrapper...")
            return result
        return _wrapper
    return wrapper

@loopy_decorator_with_args(4)
def loopy_decorated_function(arg):
    return [arg]

if __name__ == "__main__":
    print(loopy_decorated_function("hello loopy"))
