def awesome(func):
    def wrapper():
        func()
        print("no you are awesome")
    return wrapper
#@awesome

def ordinary():
    print('i am ordinary')

extra_ordinary = awesome(ordinary)
print(extra_ordinary)