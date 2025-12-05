def decorator(func):
    def wrapper():
        func()
        print("Before")
        func()
        print("After")
        func()
    return wrapper

@decorator
def greet():
    print("Hello World!")
greet()